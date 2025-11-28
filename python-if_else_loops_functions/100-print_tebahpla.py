#!/usr/bin/python3
c = 1
for i in range(122, 96, -1):
    if c % 2 == 0:
        i = i - 32
    print("{x:c}".format(x=i), end="")
    c += 1
