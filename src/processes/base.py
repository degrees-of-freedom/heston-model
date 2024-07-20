#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""\
This module provides a framework for defining various stochastic processes. 
It contains the base class `StochasticProcess`, which serves as the foundation 
for implementing any type of stochastic process.
"""

__author__ = None
__copyright__ = None


from abc import ABC, abstractmethod
import numpy as np
import scipy


class StochasticProcess(ABC):
    def __init__(self):
        """
        Constructor method for StochasticProcess.
        """
        pass

    def __repr__(self) -> str:
        """
        Returns a string representation of the StochasticProcess.

        @returns {str} String representation of the stochastic process.
        """
        pass

    @staticmethod
    def std_error(arr: np.ndarray) -> float:
        """
        Calculate the standard error of an array.

        @param {np.ndarray} arr - Input array.
        @returns {float} Standard error of the array.
        """
        return scipy.stats.sem(arr)
