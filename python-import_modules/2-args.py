#!/usr/bin/python3
import sys

if __name__ == "__main__":
    print("{} arguments:".format(len(sys.argv) - 1))
    for i in range(1, len(sys.argv)):
        print("{num}: {arg}".format(num=i, arg=sys.argv[i]))
