#!/usr/bin/python3
"""module for the base class"""
import json
import csv


class Base:
    """definition of the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """intialized our constructor___"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to__json_string(list_dictionaries):
        """returns JSON string representation"""
        if list_dictionaries is None or not list_dictionaries:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write JSON serilization to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        objects = [obj.to_dictionary() for obj in list_objs]
        json_str = cls.to__json_string(objects)
        with open(filename, "w", encoding='utf-8') as file:
            file.write(json_str)

    @staticmethod
    def from__json_string(json_string):
        """return the deserialization of a JSON string"""
        if json_string is None or not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return an instance with all attributes"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of classes instatiated from a file JSON"""
        try:
            with open(cls.__name__ + ".json", "r") as jsonfile:
                list_dic = cls.from__json_string(jsonfile.read())
                return [cls.create(**i) for i in list_dic]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """write CSV serialization of objects in a file"""
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or not list_objs:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    attributes = ["id", "width", "height", "x", "y"]
                else:
                    attributes = ["id", "size", "x", "y"]
                content = csv.DictWriter(csvfile, attributes=attributes)

    def load_from_file_csv(cls):
        """deserializes in CSV"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    attributes = ["id", "width", "height", "x", "y"]
                else:
                    attributes = ["id", "size", "x", "y"]
                list_dic = csv.DictReader(csvfile, attributes=attributes)
                list_dic = [dict([k, int(v)] for k, v in x.items())
                            for d in list_dic]
                return [cls.create(**x) for x in list_dic]
        except FileNotFoundError:
            return []
