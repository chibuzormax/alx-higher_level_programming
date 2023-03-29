#!/usr/bin/python3
"""Defines a class Square"""


class Square:
     """Represent a square."""

    def __init__(self, size=0):
          """Initialize a new square.

          Args:
          size (int): The size of the new square.
          """
        self.size = size

    def area(self):
        """ calculates the area of square
        Returns:
            Area of the square
        """
        return (self.__size) ** 2

    @property
    def size(self):
         """Get/set the current size of the square."""
         return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
              raise TypeError("size must be an integer")
        elif value < 0:
              raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints the square
        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
