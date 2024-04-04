#!/usr/bin/python3
"""A class named square"""

class Square:
    "Private class attribute size"""

    def __init__(self, size=0):
        """Initializes the data"""
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
