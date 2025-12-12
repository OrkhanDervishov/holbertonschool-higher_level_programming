#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    elif len(roman_string) == 0:
        return None
    roman_keys = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500}
    sum = 0
    for index, value in enumerate(roman_string):
        if index == 0:
            sum += roman_keys[value]
        elif roman_keys[roman_string[index-1]] < roman_keys[value]:
            sum += roman_keys[value] - 2 * roman_keys[roman_string[index-1]]
        else:
            sum += roman_keys[value]
    return sum
