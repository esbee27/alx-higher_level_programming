#!/usr/bin/python3
"""A file that defines a square based
on some properties of Rectangle
"""

import json
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from class Rectangle"""
    
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes square
        Args:
            - size
            - x
            - y
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of self"""
        str = "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                self.__width)
        return str

     @property
    def size(self):
        """gets the width of the rectangle"""
        return self.size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """Updates the values using args and kwargs"""
        if len(args) != 0 and args is not None:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "size":
                    self.width = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
