#!/usr/bin/python3
"""Saves a string into a file
The string is f
"""

import json

def save_to_json_file(my_obj, filename):
    """Saves a string in a file
    Args:
    my_obj - the object
    """

    with open(filename, 'w+') as f:
        return json.dump(my_obj, f)
