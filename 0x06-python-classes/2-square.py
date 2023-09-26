#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines a square."""

    def __init__(self, size):
        if size not int:
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        
