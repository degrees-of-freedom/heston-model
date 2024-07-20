#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""\
This module provides a framework for defining various engines. 
It contains the base class `Engine`, which serves as the foundation 
for implementing any type of financial model.
"""

__author__ = None
__copyright__ = None

from abc import ABC, abstractmethod


class Engine(ABC):
    def __init__(self):
        """
        Constructor method for Engine.
        """
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """
        Returns a string representation of the Engine.

        @returns {str} String representation of the engine.
        """
        pass
