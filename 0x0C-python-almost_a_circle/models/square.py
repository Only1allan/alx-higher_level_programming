#!/usr/bin/python3
"""defines a square class that inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square"""
    def __init__(self, size, x=0, y=0, id=None):
        """square intialization"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """gets size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """a function that updates the square"""
        if args and len(args) != 0:
            x = 0
            for arg in args:
                if x == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif x == 1:
                    self.size = arg
                elif x == 2:
                    self.x = arg
                elif x == 3:
                    self.y = arg
                x += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """return the dictionary representation of the Square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """return the print() and str() representation of square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
