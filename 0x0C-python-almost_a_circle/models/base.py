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
        """Instantiation of a base
        Args:
            - id
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of the dict"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)


