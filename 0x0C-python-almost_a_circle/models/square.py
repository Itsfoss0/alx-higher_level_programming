#!/usr/bin/python3
from models.rectangle import Rectangle
"""Square class based on Rectangle"""


class Square(Rectangle):
    """Defining Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instanitating an object
        Attrs:
            size (int) -> size of the square
            x (int)    -> x-axis offset
            y (int)    -> y-axis offset
            id(int)    -> Unique identifier
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str() representation of an object"""
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                self.x, self.y, self.width))

    @property
    def size(self):
        """Getter for size"""
        return self.size

    @size.setter
    def size(self, val):
        """Setter for size"""
        self.width = val
        self.height = val
