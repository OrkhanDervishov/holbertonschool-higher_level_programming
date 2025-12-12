#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if isinstance(value. int) == False:
            raise Exception()
        print("{}".format(value))
    except Exception:
        print("{} is not integer".format(value))
