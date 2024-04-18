#!/usr/bin/python3
"""Converts a json file to
an oject
"""

import json

def load_from_json_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)
