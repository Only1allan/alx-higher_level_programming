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
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Intializes a height and width instance
        Args:
        width (int): width of rectangle
        height (int): height of rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """get width of rectangle"""
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
        """get height of rectangle"""
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

    def __str__(self):
        """
        Returns:
        print representation of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        output = ""
        for i in range(self.__height):
            [output.append(str(self.print_symbol))for j in range(self.__width)]
        if i != self.__height - 1:
            output.append("\n")
        return ("".join(output))

    def __repr__(self):
        """
        Returns:
        string rep of a rectangle
        """
        new = "Rectangle(" + str(self.__width)
        new += ", " + str(self.__height) + ")"
        return new

    def __del__(self):
        """
        Returns:
        Prints message when rectangle is deleted
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
