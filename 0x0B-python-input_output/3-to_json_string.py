#!/usr/bin/python3
"""Returns the JSON representation of
a string
"""


import json


def to_json_string(my_obj):
    """Returns the json representation of the str
    Args:
    my_obj - the object
    """
    return json.dumps(my_obj)
