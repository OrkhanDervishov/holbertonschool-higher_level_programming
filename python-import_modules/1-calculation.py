#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    a = 10
    b = 5
    print("{va} + {vb} = {res}".format(va=a, vb=b, res=add(a, b)), end="\n")
    print("{va} - {vb} = {res}".format(va=a, vb=b, res=sub(a, b)), end="\n")
    print("{va} * {vb} = {res}".format(va=a, vb=b, res=mul(a, b)), end="\n")
    print("{va} / {vb} = {res}".format(va=a, vb=b, res=div(a, b)), end="\n")
