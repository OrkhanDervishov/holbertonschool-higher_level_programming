#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) == False:
        return 0
    sum = 0
    for i in roman_string:
        if i == 'I':
            sum += 1
        elif i == 'V':
            sum += 5
        elif i == 'X':
            sum += 10
        elif i == 'L':
            sum += 50
        elif i == 'C':
            sum += 100
        elif i == 'D':
            sum += 500
        elif i == 'M':
            sum += 1000
    return sum
