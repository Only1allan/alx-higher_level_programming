#!/usr/bin/python3
"""module for function returning an python object rep by JSON"""
import json


def from_json_string(my_str):
    """function returns python data structure in JSON"""

    return json.loads(my_str)
