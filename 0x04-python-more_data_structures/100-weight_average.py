#!/usr/bin/python3
def weight_average(my_list=[]):
    """returns the weighted average of all integers tuple"""
    if not my_list:
        return 0

    num = 0
    den = 0

    for tp in my_list:
        num += tp[0] * tp[1]
        den += tp[1]

    return (num / den)
