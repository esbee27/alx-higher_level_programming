#!/usr/bin/python3
"""A square module"""


class Square:
    """A class with sides of size"""

    def __init__(self, size=0):
        """Initializes the square.

        Args:
            size: length of the sides of the square.
        """

        self.__size = size

    @property
    def size(self):
        """Defines the size of the square
        A private class
        
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square

        Args:
            value: the value of the size

        """
        if type(value) != int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """Returns the area of the square"""

        return self.__size ** 2
