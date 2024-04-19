#!/usr/bin/python3
"""A module that defines Base, a superclass
inherited by Rectangle and Square
"""


class Base:
    """A class with id
    Args:
        id - the id of the variable
    """

    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
