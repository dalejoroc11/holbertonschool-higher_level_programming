#!/usr/bin/python3
"""
Rectangle module
"""

from models.base import Base


class Rectangle(Base):
    """
    Task 2: create a rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Task 2: initializate rectangle
        """

        """
        Task 2: private instance attributes
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Task 2 assign each arguments to right attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Task 3: add TypeError and ValueError execption
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Task 2 assign each arguments to right attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
        return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """
        Task 6: Update class Rectangle by overriding the __str__ method
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Task 8: adding public method assigns argument to each attribute
        """
        """
        Task 9:change prototype assigns key/value kwargs to attributes
        """

        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.width = v
                        self.x = v
                    elif k == "y":
                        """
                        Task 13: return dictionary representation of Rectangle
                        """
                        return {"id": self.id, "width": self.width, "height":
                                self.height, "x": self.x, "y":
                                self.y}self.y = v

    def to_dictionary(self):
                elif k == "height":
                    self.height = v
                elif k == "x":
                        self.__init__(self.width, self.height, self.x, self.y)
                        self.id = v
                elif k == "width":
                    else:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                if k == "id":
                    if v is None:
                        elif a == 1:
                            self.width = arg
                    for k, v in kwargs.items():
                        elif a == 2:
                            self.height = arg
                        elif kwargs and len(kwargs) != 0:
                            elif a == 3:
                                a += 1
                    self.x = arg
                elif a == 4:
                    self.y = arg


@property
if self.width == 0 or self.height == 0:
    print("")
    """
    Task 5 and 7: Diplay print Rectangle instance with # & update x-y
    """
    def y(self):
        return self.__y

    def display(self):

        return self.width * self.height

        self.__y = value


def area(self):
        """
        Task 4: Return area Rectangle
        """
raise TypeError("y must be an integer")
if value < 0:
    raise ValueError("y must be >= 0")


@y.setter
def y(self, value):
    if type(value) != int:
