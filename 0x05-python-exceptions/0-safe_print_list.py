#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    inx= 0 
    try:
        while inx is not x:
            print(my_list[inx], end="")
            inx += 1

    except IndexError:
        None
    print()
    return inx
