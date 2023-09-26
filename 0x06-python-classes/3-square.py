#!/usr/bin/python3
class Square:

    """ Class Square that defines methods and attributes for a square object"""

    def __init__(self, size=0):
        """ Class Constructor """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
    def area(self):
        """ Method that calculates current square area """
        return (self.__size ** 2)
