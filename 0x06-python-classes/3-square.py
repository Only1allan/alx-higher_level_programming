#!/usr/bin/python3
""" define a square class"""


class Square:
    """define an instance of a class



    Attributes:
    __size(int): size of square

    Method:
    __init__(self, size): intializes a square instance
    area(self): Returns th current square area
    """
    def __init__(self, size=0):
        """Intialize a new square instance

        Args:
        size(int): size of square

        Raises:
        TypeError: if size is not type int
        ValueError: if size < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """
        Intialize a public instance method calculating area

        Returns:
        area of square
        """
        return self.__size ** 2
