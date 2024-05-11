#!/usr/bin/python3
"""A module that prints a sorted list
    from an inherited class
    """

class MyList(list):
        """A class that inherits a class called list"""

        def print_sorted(self):
            """prints a sorted list"""

            print(sorted(self))
