#!/usr/bin/python3
"""Module 1-rectangle
Defines a rectangle
"""


class Rectangle:
    """A class that defines a rectangle"""



    def __init__(self, width=0, height=0):
        """Initializes the rectangle.

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Defines the width of the private class width
        A private class

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets value of self

        Args:
            value: value of the width

        """

        if type(width) != int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def width(self):
        """Defines height of the private class width
        A private class

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets value of self

        Args:
            value: value of the height

        """

        if type(height) != int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = value


    def area(self):
        """Sets the public attribute area
        Return: returns area of the rectangle
        
        """

        return self.__height * self.__width

    def perimeter(self):
        """Sets the public instance of the perimeter
        Return: returns the perimeter of the rectangle

        """

        return 2 * (self.__width + self.__height)
