#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""\
This module provides a framework for defining various financial instruments. 
It contains the base class `Instrument`, which serves as the foundation 
for implementing any type of financial instrument.
"""

__author__ = None
__copyright__ = None


from abc import ABC, abstractmethod


class Instrument(ABC):
    def __init__(self):
        """
        Constructor method for Instrument.
        """
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """
        Returns a string representation of the Instrument.

        @returns {str} String representation of the instrument.
        """
        pass
