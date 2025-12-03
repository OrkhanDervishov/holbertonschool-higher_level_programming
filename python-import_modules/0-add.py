#!/usr/bin/python3
from add_0 import add

if __name__ == "__main__":
    a = 1
    b = 2
    print("{va} + {vb} = {res}".format(va = a, vb = b, res = add(a, b)))
