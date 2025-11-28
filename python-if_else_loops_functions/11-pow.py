#!/usr/bin/python3
def pow(a, b):
    power = a
    for i in range(b-1):
        power *= a
    return power
