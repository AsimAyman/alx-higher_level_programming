#!/usr/bin/python3
def no_c(my_string):
    s = list(my_string)
    [s.remove(i) for i in slist if i == 'c' or i == 'C']
    return("".join(s))
