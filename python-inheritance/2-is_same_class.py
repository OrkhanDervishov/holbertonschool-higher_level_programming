#!/usr/bin/python3
"""Doc"""


def is_same_class(obj, a_class):
    """Doc"""
    if obj is None:
        return False
    return type(obj) is a_class
