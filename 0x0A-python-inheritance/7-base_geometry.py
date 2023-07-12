#!/usr/bin/python3
"""defines a base geometry class"""


class BaseGeometry:
    """instance of a basegeometry class"""
    def area(self):
        """implementation failure"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate if value is an int"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
