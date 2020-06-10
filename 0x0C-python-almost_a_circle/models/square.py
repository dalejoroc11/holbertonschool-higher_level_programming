#!/usr/bin/python3
""" square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ square """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        super().valwh("width", val)
        self.width = val
        self.height = val

    def __str__(self):
        """ string """
        return "[" + __class__.__name__ + "] (" + str(self.id) + ") " +\
               str(self.x) + "/" + str(self.y) + " - " + str(self.width)

    def update(self, *args, **kwargs):
        """ update """
        if len(args) > 0:
            i = 0
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                    self.height = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        else:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "size":
                    self.width = kwargs[key]
                    self.height = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                elif key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        """ dictionary """
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
