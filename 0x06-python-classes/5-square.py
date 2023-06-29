#!/usr/bin/python3
""" define a square class"""


class Square:
    """define an instance of a class



    Attributes:
    __size(int): size of square

    Method:
    __init__(self, size): intializes a square instance
    area(self): Returns the current square area
    size(self): Getter method
    size(self, value): set method
    """
    def __init__(self, size=0):
        """Intialize a new square instance"""

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size is >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Returns:
        area of square
        """
        return self.__size ** 2

    def my_print(self):
        """print the square with # character"""
        if self.__size == 0:
            print()
        for row in range(self.__size):
            for col in range(self.__size):
                print("#", end="")
            print("")
