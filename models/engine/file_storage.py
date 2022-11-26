#!/usr/bin/env python3
"""
Serializes instances to JSON file deserializes, 
deserializes JSON files to instances
"""

import json


class FileStorage:
    """
    Blueprint for a file storage instance
    """

    # Private class attributes
    __file_path = "file.json"
    __objects = {}

    # public instance methods
    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects
    
    def new(self, obj):
        """
        sets in __objects the obj with the key
        <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        In other words, simply writing to a file
        """
        with open(self.__file_path, mode="w") as file:
            dict_storage = {}
            for key, value in self.__objects.items():
                dict_storage[key] = value.to_dict()
            json.dump(dict_storage, file)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
        Otherwise, do nothing
        No exception should be raised
        """
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
