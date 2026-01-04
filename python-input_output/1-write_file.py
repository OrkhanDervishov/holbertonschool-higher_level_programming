#!/usr/bin/python3
"""Doc"""


def write_file(filename="", text=""):
    """Doc"""
    with open(filename, encoding="utf-8") as file:
        file.write(text)
    return len(text)