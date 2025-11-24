#!/usr/bin/python3
for i in range(0, 100):
    if i != 99:
        print("{num}, ".format(num=i), end="")
    else:
        print("{num}".format(num=i))
