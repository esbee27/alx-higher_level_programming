#!/usr/bin/python3
"""A rectangle class that 
inherits from the base class
"""

class Rectangle(Base):
    """Inherits from the base class
    Args:
        Private classes
        _ width
        - height
        - x
        - y
    """


    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes"""

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

     @property
    def height(self):
        """gets the width of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

     @property
    def x(self):
        """gets the x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """gets the x coordinate of the rectangle"""
        return self.__y

    @x.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Prints the rectangle to the stdout"""
        for i in range(0, __width):
            for j in range(0, __height):
                print("#", end="")
            print()

    def __str__(self):
        """Prints out the string representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                                                       self.__y, self.__width,
                                                       self.__height)
