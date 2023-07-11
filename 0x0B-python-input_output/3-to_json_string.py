#!/usr/bin/python3
"""module for a function that return JSON rep of an object"""
import json


def to_json_string(my_obj):
    """function to return JSON obj"""

    return json.dumps(my_obj)
