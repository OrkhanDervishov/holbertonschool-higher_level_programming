#!/usr/bin/python3
def remove_char_at(str, n):
    if n > len(str) or n < 0:
        return str
    char_list = list(str)
    char_list[n] = ''
    return "".join(char_list)
