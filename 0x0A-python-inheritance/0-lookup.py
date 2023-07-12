#!/usr/bin/python3
"""module for a function that lists avalilable methods of an object"""


def lookup(obj):
    """function to list available method rom the given obj."""
    return dir(obj)
