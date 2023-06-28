#!/usr/bin/python3
"""define a class square"""


class Square:
    """
    Square class size


    Attributes:
    __size(int): square size
    Methods:
    __init__(self, size):
    intialize a square instance
    """
    def __init__(self, size=0):
        """square instance

        Args:
        size(int): size of a square

        Raise:
        TypeError: If size is not an int
        ValueError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
