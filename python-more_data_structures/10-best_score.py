#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    maxValue = -999999
    maxKey = None
    for i in a_dictionary.keys():
        maxKey = i if a_dictionary[i] > maxValue else maxKey
        maxValue = a_dictionary[maxKey]
    return maxKey
