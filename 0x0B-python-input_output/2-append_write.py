#!/usr/bin/python3
"""a function that appends a string to EOF"""


def append_write(filename="", text=""):
    """appends the given `text` at end of file specified by filename."""

    with open(filename, "a") as file:
        return file.write(text)
