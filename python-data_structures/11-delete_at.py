#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    for i, val in enumerate(my_list):
        if i != idx:
            new_list.append(val)
    my_list[:] = new_list
    return new_list
