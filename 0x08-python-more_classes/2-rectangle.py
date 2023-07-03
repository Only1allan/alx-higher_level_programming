#!/usr/bin/python3
"""define a rectangle"""


class Rectangle:
    """define an instance of a rectangle class


    Attributes:
    __width(int): shorter side of the square
    __height(int): Longer side of the square

    Method:
    __init__(self, width=0, height=0): intializes a height and width
    height(self): Getter method
    height(self, value): set method
    width(self): Getter method
    width(self, value): set method
    """
    def __init__(self, width=0, height=0):
        """Intializes a height and width instance"""
    
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        Returns:
        area of rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Returns:
        perimeter of rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2
