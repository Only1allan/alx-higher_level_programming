#!/usr/bin/python3
"""A function that reads a text file and prints it"""


def read_file(filename=""):
    """function reading a text file"""
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end='')
