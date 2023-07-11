#!/usr/bin/python3
"""A function that reads a text file and prints it"""


def read_file(filename=""):
    """print the contents of my file """
    with open(filename, encoding="utf-8") as file:
        content = file.read()
        for ch in content:
            print(ch, end="")
        print()