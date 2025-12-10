#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max = -999999
    for i in my_list:
        max = i if i > max else max
    return max
