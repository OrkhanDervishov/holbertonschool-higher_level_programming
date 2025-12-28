#!/usr/bin/python3
"""Doc"""


def is_kind_of_class(obj, a_class):
    """Doc"""
    if obj is a_class:
        return True
    elif isinstance(obj, a_class):
        return True
    return False
