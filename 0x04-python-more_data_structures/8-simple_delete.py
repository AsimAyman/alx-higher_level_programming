#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary.__contains__(key):
        del a_dictionary[key]
    return (a_dictionary)    
