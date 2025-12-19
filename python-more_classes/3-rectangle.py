#!/usr/bin/python3
'''Documentation'''


class Rectangle:
    """za"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*self.width + 2*self.height

    def __draw(self):
        rectangle = ""
        height = self.__height
        width = self.__width

        for i in range(height):
            rectangle += "#" * width

            if i != height - 1:
                rectangle += "\n"

        return rectangle

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return self.__draw()
