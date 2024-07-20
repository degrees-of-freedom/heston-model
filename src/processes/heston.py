#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""\
This module provides a framework for defining various heston process. 
This class inherit methods from the parent class `StochasticProcess`, 
providing a consistent framework for heston process.
"""

__author__ = None
__copyright__ = None


from processes.base import StochasticProcess
from engines.heston import HestonEngine
import numpy as np


class HestonProcess(StochasticProcess):
    @staticmethod
    def paths(
        engine: HestonEngine, n_paths: int, n_steps: int, horizon: float, **kwargs
    ):
        """
        Simulate paths for the Heston process.

        @param (HestonEngine) engine - The Heston engine instance.
        @param (int) n_paths - Number of paths to simulate.
        @param (int) n_steps - Number of time steps.
        @param (float) horizon - Time horizon for the simulation.
        **kwargs: Additional keyword arguments.

        @returns Tuple[np.ndarray, np.ndarray, np.ndarray] Transposed arrays of asset prices,
        volatilities, and adjusted correlations.
        """
        dt = horizon / n_steps
        sqrt_dt = np.sqrt(dt)

        # Get optional parameters or use defaults
        discretization = kwargs.get("discretization", "truncation")
        scheme = kwargs.get("scheme", "milstein")
        measure = kwargs.get("measure", "rn")

        # Validate parameters
        assert discretization in ("truncation", "reflection")
        assert scheme in ("milstein", "euler")
        assert measure in ("rn", "rw")
        assert isinstance(engine, HestonEngine)

        zs = np.zeros((n_steps + 1, n_paths))
        s = np.zeros((n_steps + 1, n_paths))
        v = np.zeros((n_steps + 1, n_paths))
        rho_adj = np.zeros((n_steps + 1, n_paths))

        # Initialize starting values
        rho_adj[0, :] = engine.rho
        v[0, :] = engine.v0
        s[0, :] = engine.s0

        zv_adj = 0.0
        zs_adj = 0.0

        for t_step in range(1, n_steps + 1):
            zv_t = np.random.randn(n_paths)
            zs_t = np.random.randn(n_paths)

            if scheme == "euler":
                v[t_step] = (
                    v[t_step - 1]
                    + engine.kappa * (engine.theta - v[t_step - 1]) * dt
                    + engine.sigma * np.sqrt(v[t_step - 1]) * (sqrt_dt * zv_t + zv_adj)
                )
            elif scheme == "milstein":
                v[t_step] = (
                    v[t_step - 1]
                    + engine.kappa * (engine.theta - v[t_step - 1]) * dt
                    + engine.sigma * np.sqrt(v[t_step - 1]) * (sqrt_dt * zv_t + zv_adj)
                    + 1 / 4 * engine.sigma**2 * dt * ((zv_t + zv_adj) ** 2 - 1)
                )

            if discretization == "reflection":
                v[t_step] = np.abs(v[t_step])
            elif discretization == "truncation":
                v[t_step] = np.maximum(v[t_step], 0.00001)

            phi_t = engine.phi
            if engine.phi == 0:
                rho_adj[t_step] = engine.rho
            else:
                rho_adj[t_step] = engine.rho * np.sqrt(v[t_step] / (v[t_step] + phi_t))

            zs[t_step] = (rho_adj[t_step - 1]) * zv_t + np.sqrt(
                1 - (rho_adj[t_step - 1]) ** 2
            ) * zs_t
            if measure == "rn":
                s[t_step] = s[t_step - 1] * np.exp(
                    (engine.risk_free_rate - engine.dividend_yield - v[t_step - 1] / 2)
                    * dt
                    + np.sqrt(v[t_step - 1] + phi_t) * sqrt_dt * zs[t_step]
                )
            elif measure == "rw":
                s[t_step] = s[t_step - 1] * np.exp(
                    (engine.mu - engine.dividend_yield - v[t_step - 1] / 2) * dt
                    + np.sqrt(v[t_step - 1] + phi_t) * (sqrt_dt * zs[t_step] + zs_adj)
                )

        return np.transpose(s), np.transpose(np.sqrt(v)), np.transpose(rho_adj)
