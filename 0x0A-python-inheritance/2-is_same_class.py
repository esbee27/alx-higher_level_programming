#!/usr/bin/python3
"""A module that checks if
the object is the same instance of a_class
"""

def is_same_class(obj, a_class):
    """Checks for same instance of a class"""
    if type(obj) is a_class:
        return True
    else:
        return False
