#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
    """

    def __init__(self, size=0):
        """initializes the square
        Args:
            size (int): size of a side of the square
        Returns:
            None
        """
        self.size = size

    def area(self):
        """calculates the square's area
        Returns:
            The area of the square
        
        ##Doctest: Testing this function
        >>> my_square = Square(89)
        >>> print("Area: {} for size: {}".format(my_square.area(), my_square.size))
        Area: 7921 for size: 89
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): size of a side of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """prints the square
        Returns:
            None
        ##Doctest: Testing this function
        >>> my_square = Square(89)
        >>> print("Area: {} for size: {}".format(my_square.area(), my_square.size))
        Area: 7921 for size: 89

        >>> my_square.size = 3
        >>> print("Area: {} for size: {}".format(my_square.area(), my_square.size))
        Area: 9 for size: 3

        >>> try:
        ...     my_square.size = "5 feet"
        ...     print("Area: {} for size: {}".format(my_square.area(), my_square.size))
        ... except Exception as e:
        ...     print(e)
        size must be an integer
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
