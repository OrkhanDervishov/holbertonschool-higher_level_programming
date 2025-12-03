#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
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
            exit(1)

    print("{va} {oper} {vb} = {result}".format(va=a, oper=op, vb=b, result=res))
    exit(0)
