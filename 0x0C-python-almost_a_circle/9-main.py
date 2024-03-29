#!/usr/bin/python3
""" 9-main """
from models.square import Square

if __name__ == "__main__":

    p_s1 = Square(0)
    print(p_s1)
    print(p_s1.area())
    p_s1.display()

    print("---")

    s2 = Square(1, 2, 3, 4)
    print(s2)
    print(s2.area())
    s2.display()

    print("---")

    s3 = Square(3, 1, 3)
    print(s3)
    print(s3.area())
    s3.display()

    s3 = Square(2, 2)
    print(s3)
    print(s3.area())
    s3.display()

    print("---")
