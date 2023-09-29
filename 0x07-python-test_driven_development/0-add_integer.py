#!/usr/bin/python3
"""Module for add integer methode"""

def add_integer(a, b=98):
    """adds 2 integers.

    Args:
        a:first one.
        b:second one.

    Raise:
        TypeError: if a, b are not int, float.

   Returns:
        The sum ow the two
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
    
if __name__ == "__main__":
    import doctest
    doctest.testile("tests/0-add_integer.txt")
