#!/usr/bin/python3
"""Defines a locked class"""


class LockedClass:
    """
    User cannot initiate new attributes apart from first_name
    """
    __slots__ = ["first_name"]