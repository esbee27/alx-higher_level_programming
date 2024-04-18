#!/usr/bin/python3
"""Converts a json file to
an oject
"""

import json

def load_from_json_file(filename):
    """Converts json file to
    to an object
    """

    with open(filename, 'r') as f:
        return json.loads(f)
