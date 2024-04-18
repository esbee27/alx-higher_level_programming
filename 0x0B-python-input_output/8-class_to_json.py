#!/usr/bin/python3
"""Returns the dictionary representation
of an object
"""

def class_to_json(obj):
    """Returns the dictionary description of a simple data structure
    Args:
        obj - The object to be opened
    """

    return obj.__dict__
