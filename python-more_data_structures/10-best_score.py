#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is {}:
        return None
    max = -999999
    for i in a_dictionary.keys():
        max = a_dictionary[i] if a_dictionary[i] > max else max
    return max
