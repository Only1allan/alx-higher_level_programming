#!/usr/bin/python3
"""function that writes a string to a textfile"""


def write_file(filename="", text=""):
    """writes the given `text` into file with name specified by filename"""

    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
