#!/usr/bin/python3
"""module for writing an object to a file using JSON"""
import json


def save_to_json_file(my_obj, filename):
    """function that saves the given obj as a JSON string"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
