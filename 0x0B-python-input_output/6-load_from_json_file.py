#!/usr/bin/python3
"""module for a function creating an object from a JSON file"""
import json


def load_from_json_file(filename):
    """function to create and return an instance JSON object"""
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)