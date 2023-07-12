#!/usr/bin/python3
"""function to check if object is a class instance"""


def is_same_class(obj, a_class):
    """returns true if objects is a clas instance"""
    if type(obj) == a_class:
        return True
    return False
