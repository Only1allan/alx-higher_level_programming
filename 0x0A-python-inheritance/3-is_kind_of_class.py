#!/usr/bin/python3
"""function that returns true if object is an inherited class instance"""


def is_kind_of_class(obj, a_class):
    """checks if obj is inherited from a_class"""
    if isinstance(obj, a_class):
        return True
    return False
