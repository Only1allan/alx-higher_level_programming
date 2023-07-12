#!/usr/bin/python3
"""import rectangle subclass"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""
    def __init__(self, size):
        """intialization of square sizes"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area for the function"""
        return super().area()
