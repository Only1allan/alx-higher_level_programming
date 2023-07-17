#!/usr/bin/python3
"""module for the base class"""


class Base:
    """definition of the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """intialized our constructor___"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
