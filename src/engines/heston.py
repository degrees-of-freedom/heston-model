#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""\
This module provides a framework for defining Heston engine. 
This class inherit methods from the parent class `Engine`, 
providing a consistent framework for heston pricing.
"""

__author__ = None
__copyright__ = None


from instruments.option import EuropeanVanillaOption
from scipy.integrate import quad_vec
from engines.base import Engine
import numpy as np
import cmath
import typing


class HestonEngine(Engine):

    """
    Heston Engine Class

    This class represents an engine for pricing options using the Heston model.
    """

    def __init__(
        self,
        theta: float,
        kappa: float,
        sigma: float,
        rho: float,
        phi: float,
        v0: float,
        s0: float,
        mu: float = 0.0,
        risk_free_rate: float = 0.0,
        dividend_yield: float = 0.0,
    ):
        """
        Constructor method for HestonEngine.

        @param {float} theta - Heston model parameter.
        @param {float} kappa - Heston model parameter.
        @param {float} sigma - Heston model parameter.
        @param {float} rho - Heston model parameter.
        @param {float} phi - Heston model parameter.
        @param {float} v0 - Initial volatility.
        @param {float} s0 - Initial asset price.
        @param {float} [mu=0.0] - Drift term.
        @param {float} [risk_free_rate=0.0] - Risk-free interest rate.
        @param {float} [dividend_yield=0.0] - Dividend yield.
        """
        # Heston++ params
        self.dividend_yield = dividend_yield
        self.risk_free_rate = risk_free_rate
        self.sigma = sigma
        self.kappa = kappa
        self.theta = theta
        self.rho = rho
        self.phi = phi
        self.mu = mu
        self.s0 = s0
        self.v0 = v0

    def __repr__(self) -> str:
        """
        Returns a string representation of the Heston model.

        @returns {str} String representation of the engine.
        """
        params = (
            f"{k}={repr(v)}"
            for k, v in {
                "s0": self.s0,
                "v0": self.v0,
                "kappa": self.kappa,
                "theta": self.theta,
                "rho": self.rho,
                "mu": self.mu,
                "sigma": self.sigma,
                "phi": self.phi,
            }.items()
        )
        return f"<Engine.{self.__class__.__qualname__}({', '.join(params)})>"

    def chf(self, tau, s0, v0, z, j):
        """
        Characteristic function of the Heston model.

        @param {float|np.ndarray} tau - Time to expiration.
        @param {float|np.ndarray} s0 - Initial asset price.
        @param {float|np.ndarray} v0 - Initial volatility.
        @param {complex} z - Complex number.
        @param {int} j - Index.

        @returns {complex} Characteristic function value.
        """
        w = 1.0 if j == 1 else -1
        b = self.kappa - self.rho * self.sigma if j == 1 else self.kappa
        ixi = 1j * z
        rho_sigma = self.rho * self.sigma
        sigma_2 = self.sigma * self.sigma
        c = rho_sigma * ixi - b
        d = cmath.sqrt(c * c - sigma_2 * (w * ixi - z * z))
        b_m = b - rho_sigma * ixi - d
        b_p = b - rho_sigma * ixi + d
        g = b_m / b_p
        ee = cmath.e ** (-d * tau)
        C = (
            0.5 * z * (w * 1j - z) * (self.phi * tau)
            + self.risk_free_rate * ixi * tau
            + self.kappa
            * self.theta
            / sigma_2
            * (b_m * tau - 2.0 * np.log((1.0 - g * ee) / (1.0 - g)))
        )
        D = (b_m / sigma_2) * (1.0 - ee) / (1.0 - g * ee)
        return cmath.e ** (C + D * v0 + ixi * np.log(s0))

    def npv(self, options: typing.List):
        """
        Net Present Value (NPV) of the option.

        @param {List} options - List of option objects.

        @returns {np.ndarray} NPV of the options.
        """

        def integrad(z, j):
            return np.real(
                ((np.exp(-1j * z * np.log(k_arr))) * self.chf(tau, s0, v0, z, j))
                / (1j * z)
            )

        def q_j(j):
            return (
                0.5 + (1.0 / np.pi) * quad_vec(lambda z: integrad(z, j), 0.0, 1000.0)[0]
            )

        assert isinstance(options, (list))
        assert all(isinstance(option, EuropeanVanillaOption) for option in options)

        tau = np.array([option.tau for option in options])
        if len(set(tau)) == 1:
            tau = float(tau[0])
        s0 = np.array([option.s0 for option in options])
        if len(set(s0)) == 1:
            s0 = float(s0[0])
        flag_arr = np.array([option.flag for option in options])
        k_arr = np.array([option.strike for option in options])
        v0 = self.v0
        if all("v0" in option.kwargs for option in options):
            v0 = np.array([option.kwargs["v0"] for option in options])

        a = self.s0 * q_j(1)
        b = k_arr * np.exp(-self.risk_free_rate * tau) * q_j(2)
        return np.where(
            flag_arr == 1,
            a - b,
            a - b - self.s0 + k_arr * np.exp(-self.risk_free_rate * tau),
        )
