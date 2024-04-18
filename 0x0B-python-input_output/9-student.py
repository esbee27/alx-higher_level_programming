#!/usr/bin/python3
"""A module that defines
a student
"""

class Student:
    """Defines a student
    Public Attributes:
        - first_name
        - last_name
        - age
    """

    def __init__(self, first_name, last_name, age):
        """Function definition"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
