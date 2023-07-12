#!/usr/bin/python3
"""module for a class that inherits from another class"""


class Mylist(list):
    """Class inheriting list and some methods to it."""
    def print_sorted(self):
        """print sorted list which is the superclass"""
        print(sorted(self))
