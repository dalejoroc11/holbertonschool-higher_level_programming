#!/usr/bin/python3
""" base """

import json
import os


class Base:
    """ class base """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ static method"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ class method"""
        filename = "" + cls.__name__ + ".json"
        text = []
        with open(filename, mode='w', encoding='UTF-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))
            else:
                for i in list_objs:
                    text.append(i.to_dictionary())
                json_list = cls.to_json_string(text)
            return f.write(json_list)

    @staticmethod
    def from_json_string(json_string):
        """static method"""
        if json_string is None or len(json_string) <= 0:
            return []
        return list(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ class method"""
        if cls.__name__ == "Rectangle":
            aux = cls(1, 1)
        elif cls.__name__ == "Square":
            aux = cls(560)
        aux.update(**dictionary)
        return aux

    @classmethod
    def load_from_file(cls):
        """ class method load file from"""
        h = "" + cls.__name__ + ".json"
        text = ""
        newlist = []
        if os.path.exists(h) is False:
            return []
        with open(h, "r", encoding="UTF-8") as f:
            text = f.read()
            obj = cls.from_json_string(text)
            for i in obj:
                newlist.append(cls.create(**i))
        return newlist

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save to file"""
        filename = "" + cls.__name__ + ".csv"
        ls = []
        with open(filename, mode='w', encoding='UTF-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))
            else:
                for i in list_objs:
                    ls.append(i.to_dictionary())
                json_list = cls.to_json_string(ls)
            return f.write(json_list)

    @classmethod
    def load_from_file_csv(cls):
        """ load from file"""
        h = "" + cls.__name__ + ".csv"
        text = ""
        newlist = []
        if os.path.exists(h) is False:
            return []
        with open(h, "r", encoding="UTF-8") as f:
            text = f.read()
            obj = cls.from_json_string(text)
            for i in obj:
                newlist.append(cls.create(**i))
        return newlist
