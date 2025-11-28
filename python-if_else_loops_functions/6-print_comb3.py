#!/usr/bin/python3
for i in range(0, 9):
    for j in range(1 + (i*11), 1 + (i*11) + 9 - i):
        if(i != 8):
            print("{num:02d}".format(num=j), end=", ")
        else:
            print("{num:02d}".format(num=j))
        
