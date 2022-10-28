#!/usr/bin/python3
"""Square representation"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square representation inheriting from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instance initiialization of Square

        Args:
            size(int): size of square
            x(int): x coordinate
            y(int): y coordinate
            id(int): generic identifier for the square
        """
        # Call the super class with id, x, y, width and height
        # this super call will use the logic of the
        # __init__ of the Rectangle class
        # The width and height must be assigned to the value of size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter function for the size of the square.
        Returns: the size of the square
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setter function for the size of the square."""
        self.width = value
        self.height = value

    def __str__(self):
        """Method overridden to return desired string
        for class Square

        Returns:
            str: [Square] (<id>) <x>/<y> - <size>
        """
        shape = f"[{type(self).__name__}] ({self.id})"
        coords = f"{self.x}/{self.y}"
        sides = f"{self.width}"
        return f"{shape} {coords} - {sides}"
