#!/usr/bin/python3
"""Returns the python
structure from json
"""

import json


def from_json_string(my_str):
    """Returns the python structure"""

    return json.loads(my_str)
