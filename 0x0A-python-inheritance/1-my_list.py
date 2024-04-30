#!/usr/bin/python3
"""A module that prints a sorted list
    from an inherited class
    """

from lookup import list

class Mylist(list):
        """A class that inherits a class called list"""

        def print_sorted(self):
            print(sorted(self))
