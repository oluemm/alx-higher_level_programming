#!/usr/bin/python3
"""Create a rectangle class from Base class"""

from models.base import Base


class Rectangle(Base):
    """Represent class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiates a new Rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional):instance id Defaults to auto-gen id.
        """
        # === private instance attributes ====
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        # super class attributes
        super().__init__(id)

    @property
    def width(self):
        """Getter function for the width of the rectangle.
        Returns: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function for the width of the rectangle."""
        self.__width = value

    @property
    def height(self):
        """Getter function for the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for the height of the rectangle.

        Args:
            value: The newly given height of the rectangle
        """
        self.__height = value
