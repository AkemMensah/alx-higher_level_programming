#!/usr/bin/python3
def max_integer(my_list=[]):
    """finds the biggest integer of a list"""
    if len(my_list) == 0:
        return None
    else:
        my_list.sort(reverse=False)
    return(my_list[-1])
