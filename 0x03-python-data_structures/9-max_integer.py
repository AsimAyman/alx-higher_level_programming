#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    mx = sorted(my_list)[-1]
    return (mx)
