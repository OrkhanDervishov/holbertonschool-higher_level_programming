#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = ""
    res = 0
    match sys.argv[2]:
        case "+":
            op = "+"
            res = a + b
        case "-":
            op = "-"
            res = a - b
        case "*":
            op = "*"
            res = a * b
        case "/":
            op = "/"
            res = a / b
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)

    print("{va} {oper} {vb} = {result}".format(va=a, oper=op, vb=b, result=res))
    sys.exit(0)
