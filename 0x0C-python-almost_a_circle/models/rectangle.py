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
            x (int, optional): x coordinate of Rectangle. Defaults to 0.
            y (int, optional): y coordinate of Rectangle. Defaults to 0.
            id (int, optional):instance identity Defaults to auto-gen id.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        # === private instance attributes ====
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        # super class attributes
        super().__init__(id)

    # ===============SETTER & GETTER FUNCTIONS ===============
    @property
    def width(self):
        """Getter function for the width of the rectangle.
        Returns: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function for the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter function for the x-coord of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter function for the x-coord of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter function for the y-coord of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter function for the y-coord of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the Rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """Prints a visual representation of the rectangle"""
        # using list comprehension, print required new lines for `y`
        [print("") for y in range(self.y)]
        for height in range(self.__height):  # loop thru the heights
            # print spaces suited to `x` on x-axis
            [print(" ", end="") for x in range(self.x)]
            # print d width for each
            [print("#", end="") for w in range(self.__width)]
            print("")

    def __str__(self):
        """Method overridden to return desired string

        Returns:
            str: [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        shape = f"[{type(self).__name__}] ({self.id})"
        coords = f"{self.x}/{self.y}"
        sides = f"{self.__width}/{self.__height}"
        return f"{shape} {coords} - {sides}"

    def update(self, *args, **kwargs):
        """Updating instance attributes using postional args
            and keyword arguments
        """
        if len(args) != 0:
            try:
                self.id = args[0]
            except IndexError:
                pass
            try:
                self.__width = args[1]
            except IndexError:
                pass
            try:
                self.__height = args[2]
            except IndexError:
                pass
            try:
                self.x = args[3]
            except IndexError:
                pass
            try:
                self.y = args[4]
            except IndexError:
                pass
        else:
            try:
                self.id = kwargs["id"]
            except KeyError:
                pass
            try:
                self.__width = kwargs["width"]
            except KeyError:
                pass
            try:
                self.__height = kwargs["height"]
            except KeyError:
                pass
            try:
                self.x = kwargs["x"]
            except KeyError:
                pass
            try:
                self.y = kwargs["y"]
            except KeyError:
                pass
