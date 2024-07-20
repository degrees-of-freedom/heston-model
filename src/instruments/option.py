#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""\
This module contains classes defining various types of options. 
These classes inherit methods from the parent class `Instrument`, 
providing a consistent framework for option instruments.
"""

__author__ = None
__copyright__ = None


from instruments.base import Instrument
import numpy as np
import typing


class EuropeanVanillaOption(Instrument):
    def __init__(
        self,
        s0: float,
        strike: float,
        tau: float,
        flag: int = +1,
        sigma: float = 0.0,
        quote: float = 0.0,
        **kwargs,
    ):
        """
        EuropeanVanillaOption class representing an option instrument.

        @param {float} s0 - Initial price of the underlying asset.
        @param {float} strike - Strike price of the option.
        @param {float} tau - Time to expiration of the option in years.
        @param {int} [flag=+1] - Option type flag: +1 for call, -1 for put.
        @param {float} [sigma=0.0] - Implied volatiltiy for the option.
        @param {float} [quote=0.0] - Quote value for the option.
        """
        super().__init__()
        self.s0: float = s0
        self.strike: float = strike
        self.tau: float = tau
        self.flag: int = flag
        self.quote: float = quote
        self.sigma: float = sigma
        self.flag_s: str = "c" if self.flag == +1 else "p"
        self.vega: float = 0.0
        self.delta: float = 0.0
        self.gamma: float = 0.0
        self.kwargs: typing.Dict = kwargs

    @property
    def s0(self):
        return self._s0

    @property
    def strike(self):
        return self._strike

    @property
    def tau(self):
        return self._tau

    @property
    def flag(self):
        return self._flag

    @property
    def quote(self):
        return self._quote

    @property
    def sigma(self):
        return self._sigma

    @property
    def flag_s(self):
        return self._flag_s

    @s0.setter
    def s0(self, x):
        assert isinstance(x, (float, int)) and x >= 0.0
        self._s0 = x

    @strike.setter
    def strike(self, x):
        assert isinstance(x, (float, int)) and x >= 0.0
        self._strike = x

    @tau.setter
    def tau(self, x):
        assert isinstance(x, (float, int)) and x >= 0.0
        self._tau = x

    @flag.setter
    def flag(self, x):
        assert isinstance(x, int) and x in (1, -1)
        self._flag = x
        self._flag_s = "c" if self._flag == +1 else "p"

    @quote.setter
    def quote(self, x):
        assert isinstance(x, (float, int)) and x >= 0.0
        self._quote = x

    @sigma.setter
    def sigma(self, x):
        assert isinstance(x, float) and x >= 0.0
        self._sigma = x

    @flag_s.setter
    def flag_s(self, x):
        assert isinstance(x, str) and x in ("c", "p")
        self._flag_s = x

    def __repr__(self) -> str:
        """
        Returns a string representation of the EuropeanVanillaOption.

        @returns {str} String representation of the option.
        """
        params = (
            f"{k}={repr(v)}"
            for k, v in {
                "s0": self.s0,
                "strike": self.strike,
                "tau": self.tau,
                "flag": self.flag_s,
                "sigma": self.sigma,
                "quote": self.quote,
            }.items()
        )
        return f"<Instrument.{self.__class__.__qualname__}({', '.join(params)})>"

    def get_moneyness(self) -> float:
        """
        Calculate the moneyness of the option.

        @returns {float} Moneyness of the option.
        """
        return self.s0 / self.strike if self.flag == 1 else self.strike / self.s0

    def get_log_moneyness(self) -> float:
        """
        Calculate the log moneyness of the option.

        @returns {float} Log moneyness of the option.
        """
        return (
            np.log(self.s0 / self.strike)
            if self.flag == 1
            else np.log(self.strike / self.s0)
        )

    def get_fwd_moneyness(self, risk_free_rate: float) -> float:
        """
        Calculate the forward moneyness of the option.

        @param {float} risk_free_rate - Risk-free interest rate.
        @returns {float} Forward moneyness of the option.
        """
        fwd = self.s0 * np.exp(self.tau * risk_free_rate)
        return fwd / self.strike if self.flag == 1 else self.strike / fwd

    def get_log_fwd_moneyness(self, risk_free_rate: float) -> float:
        """
        Calculate the log forward moneyness of the option.

        @param {float} risk_free_rate - Risk-free interest rate.
        @returns {float} Log forward moneyness of the option.
        """
        fwd = self.s0 * np.exp(self.tau * risk_free_rate)
        return (
            np.log(fwd / self.strike) if self.flag == 1 else np.log(self.strike / fwd)
        )

    def set_npv(self, engine: object):
        """
        Set the net present value (NPV) for the option using the provided engine.

        @param {Object} engine - The engine used for NPV calculation.
        """
        assert hasattr(engine, "npv")
        self.quote = engine.npv([self])[0]

    def set_sigma(self, engine: object):
        """
        Set the implied volatility (sigma) for the option using the provided engine.

        @param {Object} engine - The engine used for implied volatility calculation.
        """
        assert hasattr(engine, "implied_volatility")
        self.sigma = engine.implied_volatility([self])[0]

    def set_delta(self, engine: object):
        """
        Set the delta greek (Delta) for the option using the provided engine.

        @param {Object} engine - The engine used for delta calculation.
        """
        assert hasattr(engine, "delta")
        self.delta = engine.npv([self])[0]

    def set_vega(self, engine: object):
        """
        Set the vega greek (Vega) for the option using the provided engine.

        @param {Object} engine - The engine used for vega calculation.
        """
        assert hasattr(engine, "vega")
        self.vega = engine.vega([self])[0]

    def set_gamma(self, engine: object):
        """
        Set the gamma greek (Gamma) for the option using the provided engine.

        @param {Object} engine - The engine used for gamma calculation.
        """
        assert hasattr(engine, "gamma")
        self.gamma = engine.gamma([self])[0]


class EuropeanVanillaOptions(object):
    def __init__(self, options: typing.List[EuropeanVanillaOption]):
        """
        Initialize the EuropeanVanillaOptions class with a list of options.

        @param {List} options - List of European vanilla options.
        """
        assert isinstance(options, list)
        assert all(isinstance(option, EuropeanVanillaOption) for option in options)
        self.options = options

    def __repr__(self) -> str:
        """
        Returns a string representation of the EuropeanVanillaOptions.

        @returns {str} String representation of the options.
        """
        params = (f"{k}={repr(v)}" for k, v in {"options": len(self.options)}.items())
        return f"<Instrument.{self.__class__.__qualname__}({', '.join(params)})>"

    def set_npv(self, engine: object):
        """
        Set the net present value (NPV) for each option using the provided engine.

        @param {Object} engine - The engine used for NPV calculation.
        """
        assert hasattr(engine, "npv")
        quotes = engine.npv(self.options)
        for option, quote in zip(self.options, quotes):
            option.quote = quote

    def set_sigma(self, engine: object):
        """
        Set the implied volatility (sigma) for each option using the provided engine.

        @param {Object} engine - The engine used for implied volatility calculation.
        """
        assert hasattr(engine, "implied_volatility")
        sigmas = engine.implied_volatility(self.options)
        for option, sigma in zip(self.options, sigmas):
            option.sigma = sigma

    def set_delta(self, engine: object):
        """
        Set the delta greek (Gamma) for each option using the provided engine.

        @param {Object} engine - The engine used for delta calculation.
        """
        assert hasattr(engine, "delta")
        deltas = engine.npv(self.options)
        for option, delta in zip(self.options, deltas):
            option.delta = delta

    def set_vega(self, engine: object):
        """
        Set the vega greek (Gamma) for each option using the provided engine.

        @param {Object} engine - The engine used for vega calculation.
        """
        assert hasattr(engine, "vega")
        vegas = engine.vega(self.options)
        for option, vega in zip(self.options, vegas):
            option.vega = vega

    def set_gamma(self, engine: object):
        """
        Set the gamma greek (Gamma) for each option using the provided engine.

        @param {Object} engine - The engine used for gamma calculation.
        """
        assert hasattr(engine, "gamma")
        gammas = engine.gamma(self.options)
        for option, gamma in zip(self.options, gammas):
            option.gamma = gamma
