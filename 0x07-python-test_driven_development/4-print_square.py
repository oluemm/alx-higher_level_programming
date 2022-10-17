#!/usr/bin/python3
"""Defining a function that prints a square"""

def print_square(size):
    """Prints a square

    Args:
        size (int): size of the square to print

    Raises:
        TypeError: if the size is not an integer
        TypeError: if the size is not a postive floating point number
        ValueError: if size is less than zero(0)

    Returns: None
    """
    if not isinstance(size, int) and not isinstance(size, float):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(int(size)):
            print("".join("#" for j in range(int(size))))
