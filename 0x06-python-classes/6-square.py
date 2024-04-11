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

    @property
    def position(self):
        """Defines the size of the square
        A private class

        """
        return self.__position

    @size.setter
    def position(self, value):
        """Sets the size of the square

        Args:
            value: the value of the size

        """
        if type(value) != tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    def area(self):
        """Returns the area of the square"""

        return self.__size ** 2
    def my_print(self):
        """Prints the square to the stdout"""

        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
