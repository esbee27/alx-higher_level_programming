#!/usr/bin/python3
"""A class with the name Square"""
class Square:
    
    """Constructs the class"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

        """returns the current area"""
    def area(self):
        return (self.__size) * (self.__size)
