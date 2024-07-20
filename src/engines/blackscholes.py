#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""\
This module provides a framework for defining Black-Scholes engine. 
This class inherit methods from the parent class `Engine`, 
providing a consistent framework for Black-Scholes pricing.
"""

__author__ = None
__copyright__ = None


from py_vollib_vectorized import vectorized_black_scholes
from py_vollib_vectorized import vectorized_implied_volatility
from instruments.option import EuropeanVanillaOption
from py_vollib_vectorized import greeks
from engines.base import Engine
import numpy as np
import typing


class BlackScholesEngine(Engine):
    """
    Black-Scholes Engine Class

    This class represents an engine for pricing options using the Black-Scholes model.
    """

    def __init__(self, risk_free_rate: float = 0.0, dividend_yield: float = 0.0):
        """
        Constructor method for BlackScholesEngine.

        @param {float} [risk_free_rate=0.0] - Risk-free interest rate.
        @param {float} [dividend_yield=0.0] - Dividend yield.
        """
        self.risk_free_rate = risk_free_rate
        self.dividend_yield = dividend_yield

    def __repr__(self) -> str:
        """
        Returns a string representation of the Black-Scholes engine.

        @returns {str} String representation of the engine.
        """
        params = (
            f"{k}={repr(v)}"
            for k, v in {
                "risk_free_rate": self.risk_free_rate,
                "dividend_yield": self.dividend_yield,
            }.items()
        )
        return f"<Model.{self.__class__.__qualname__}({', '.join(params)})>"

    def npv(self, options: typing.List):
        """
        Calculate the Net Present Value (NPV) of the options.

        @param {List} objs - List of option objects.

        @returns {np.ndarray} NPV of the options.
        """
        assert isinstance(options, (list))
        assert all(isinstance(option, EuropeanVanillaOption) for option in options)

        flag_arr = np.array(["c" if option.flag == +1 else "p" for option in options])
        strike_arr = np.array([float(option.strike) for option in options])
        s0_arr = np.array([float(option.s0) for option in options])
        tau_arr = np.array([float(option.tau) for option in options])
        sigma_arr = np.array([float(option.sigma) for option in options])

        return vectorized_black_scholes(
            flag_arr,
            s0_arr,
            strike_arr,
            tau_arr,
            self.risk_free_rate,
            sigma_arr,
            return_as="numpy",
        )

    def implied_volatility(self, options: typing.List):
        """
        Calculate the implied volatility of the options.

        @param {List} options - List of option objects.

        @returns {np.ndarray} Implied volatility of the options.
        """
        assert isinstance(options, (list))
        assert all(isinstance(option, EuropeanVanillaOption) for option in options)

        flag_arr = np.array(["c" if option.flag == +1 else "p" for option in options])
        strike_arr = np.array([float(option.strike) for option in options])
        s0_arr = np.array([float(option.s0) for option in options])
        tau_arr = np.array([float(option.tau) for option in options])
        quote_arr = np.array([float(option.quote) for option in options])

        return vectorized_implied_volatility(
            quote_arr,
            s0_arr,
            strike_arr,
            tau_arr,
            self.risk_free_rate,
            flag_arr,
            q=self.dividend_yield,
            model="black_scholes_merton",
            return_as="numpy",
        )

    def delta(self, options: typing.List):
        """
        Calculate the delta of the options.

        @param {List} options - List of option objects.

        @returns {np.ndarray} Delta of the options.
        """
        assert isinstance(options, (list))
        assert all(isinstance(option, EuropeanVanillaOption) for option in options)

        flag_arr = np.array(["c" if option.flag == +1 else "p" for option in options])
        strike_arr = np.array([float(option.strike) for option in options])
        s0_arr = np.array([float(option.s0) for option in options])
        tau_arr = np.array([float(option.tau) for option in options])
        sigma_arr = np.array([float(option.sigma) for option in options])

        return greeks.delta(
            flag_arr,
            s0_arr,
            strike_arr,
            tau_arr,
            0.025,
            sigma_arr,
            q=None,
            model="black_scholes",
            return_as="numpy",
        )

    def gamma(self, options: typing.List):
        """
        Calculate the gamma of the options.

        @param {List} options - List of option objects.

        @returns {np.ndarray} Gamma of the options.
        """
        assert isinstance(options, (list))
        assert all(isinstance(option, EuropeanVanillaOption) for option in options)

        flag_arr = np.array(["c" if option.flag == +1 else "p" for option in options])
        strike_arr = np.array([float(option.strike) for option in options])
        s0_arr = np.array([float(option.s0) for option in options])
        tau_arr = np.array([float(option.tau) for option in options])
        sigma_arr = np.array([float(option.sigma) for option in options])

        return greeks.gamma(
            flag_arr,
            s0_arr,
            strike_arr,
            tau_arr,
            0.025,
            sigma_arr,
            q=None,
            model="black_scholes",
            return_as="numpy",
        )

    def vega(self, options: typing.List):
        """
        Calculate the vega of the options.

        @param {List} options - List of option objects.

        @returns {np.ndarray} Vega of the options.
        """
        assert isinstance(options, (list))
        assert all(isinstance(option, EuropeanVanillaOption) for option in options)

        flag_arr = np.array(["c" if option.flag == +1 else "p" for option in options])
        strike_arr = np.array([float(option.strike) for option in options])
        s0_arr = np.array([float(option.s0) for option in options])
        tau_arr = np.array([float(option.tau) for option in options])
        sigma_arr = np.array([float(option.sigma) for option in options])

        return greeks.vega(
            flag_arr,
            s0_arr,
            strike_arr,
            tau_arr,
            0.025,
            sigma_arr,
            q=None,
            model="black_scholes",
            return_as="numpy",
        )
