#!/usr/bin/python3
"""Function that list integers in a list peak"""


def find_peak(list_of_integers):
    """Function that list integers in a list peak"""
    if len(list_of_integers) == 0:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
