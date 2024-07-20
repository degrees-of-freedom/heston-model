#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""\
This module provides a framework for defining various heston process. 
This class inherit methods from the parent class `StochasticProcess`, 
providing a consistent framework for heston process.
"""

__author__      = None
__copyright__   = None


import numpy as np
import scipy.stats as ss
cimport numpy as np  
cimport cython
from libc.math cimport isnan

cdef extern from "math.h":
    double sqrt(double m)
    double exp(double m)
    double log(double m)
    double fabs(double m)


@cython.boundscheck(False)    # turn off bounds-checking for entire function
@cython.wraparound(False)     # turn off negative index wrapping for entire function
cpdef paths \
(
    int n_steps, 
    int n_paths, 
    double horizon, 
    double s0, 
    double v0, 
    double mu, 
    double rho, 
    double kappa, 
    double theta, 
    double sigma,
    double risk_free_rate,
    str discretization,
    str scheme,
    str measure
):
    cdef double dt = horizon/n_steps
    cdef double sqrt_dt = np.sqrt(dt)

    assert discretization in ("truncation", "reflection")
    assert scheme in ("milstein", "euler")
    assert measure in ("rn", "rw")

    cdef double[:] zs = np.zeros((n_steps+1, n_paths))
    cdef double[:] s = np.zeros((n_steps+1, n_paths))
    cdef double[:] v = np.zeros((n_steps+1, n_paths))
    cdef double[:] rho_adj = np.zeros((n_steps+1, n_paths))
    
    rho_adj[0,:] = rho
    s[0,:] = s0
    v[0,:] = v0
    
    cdef double zv_adj = 0.
    cdef double zs_adj = 0.

    for t_step in range(1, n_steps+1):

        cdef double[:] zv_t = np.random.randn(n_paths)
        cdef double[:] zs_t = np.random.randn(n_paths)

        if scheme == 'euler':
            v[t_step] = v[t_step-1] + kappa*(theta-v[t_step-1])*dt + \
                sigma*np.sqrt(v[t_step-1])*(sqrt_dt*zv_t + zv_adj)
        elif scheme == 'milstein':
            v[t_step] = v[t_step-1] + kappa*(theta-v[t_step-1])*dt + \
                sigma*np.sqrt(v[t_step-1])*(sqrt_dt*zv_t + zv_adj) + 1/4*sigma**2*dt*((zv_t + zv_adj)**2 -1)

        if discretization == 'reflection':
            v[t_step] = np.abs(v[t_step])
        elif discretization == 'truncation':
            v[t_step] = np.maximum(v[t_step], 0.00001)

        cdef double phi_t = phi
        if phi == 0:
            rho_adj[t_step] = rho
        else:
            rho_adj[t_step] = rho*np.sqrt(v[t_step]/(v[t_step]+phi_t))

        zs[t_step] = (rho_adj[t_step-1])*zv_t + np.sqrt(1-(rho_adj[t_step-1])**2)*zs_t
        if measure == 'rn':
            s[t_step] = s[t_step-1] * np.exp((risk_free_rate - dividend_yield - \
                v[t_step-1]/2)*dt + np.sqrt(v[t_step-1] + phi_t)*sqrt_dt*zs[t_step])
        elif measure == 'rw':
            s[t_step] = s[t_step-1] * np.exp((mu - dividend_yield - \
                v[t_step-1]/2)*dt + np.sqrt(v[t_step-1] + phi_t)*(sqrt_dt*zs[t_step] + zs_adj))

    return np.transpose(s), np.transpose(np.sqrt(v)), np.transpose(rho_adj)
