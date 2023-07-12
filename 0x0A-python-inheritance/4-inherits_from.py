#!/usr/bin/python3
"""function to check whether obj is instance that inherited from class"""


def inherits_from(obj, a_class):
    """return true if obj is an inherited class instance"""
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
