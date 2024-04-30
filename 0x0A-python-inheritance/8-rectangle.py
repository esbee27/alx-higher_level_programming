#!/usr/bin/python3
"""A module that raises an exception
message
"""

class BaseGeometry:
    """DEfines a geometry"""

    def area(self):
        raise Exception('area() is not implemented')
    
    def integer_validator(self, name, value):
        """Validates value."""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
class Rectangle(BaseGeometry):
    """A class that inheritts from class BaseGeometry"""

    def __init__(self, width, height):
