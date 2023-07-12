#!/usr/bin/python3
"""module for my int class"""


class Myint(int):
    """My integer subclass"""
    def __eq__(self, other):
        return self.real != other

    def __ne__(self, value):
        return self.real == other
