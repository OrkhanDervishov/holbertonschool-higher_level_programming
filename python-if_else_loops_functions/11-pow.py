#!/usr/bin/python3
def pow(a, b):
    if b > 0:
        power = a
        for i in range(b-1):
            power *= a
    elif b < 0:
        power = 1/a
        for i in range((-b)-1):
            power /= a
    else:
        power = 1
    return power

print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))
