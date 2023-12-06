#!/usr/bin/python3
import json
import os
""" file storage module """


class FileStorage:
    """ A class that stores objects in a file in json format """

    # Private Class Attributes
    __file_path = "file.json"
    __objects = {}

    # Public instance method
    def all(self):
        """ returns the dictionary __objects """
        return (self.__objects)

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        cls_name = obj.__class__.__name__
        key = cls_name + "." + obj.id
        self.__objects[key] = obj.to_dict()

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """

        # Serialization to JSON
        json_str = json.dumps(self.__objects)

        with open(self.__file_path, "w") as file:
            file.write(json_str)

    def reload(self):
        """
            deserializes the JSON file to __objects (only if the JSON file
            (__file_path) exists ; otherwise, do nothing. If the file doesn’t
            exist, no exception should be raised)
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                json_str = file.read()

                # Deserialized back to python dictionary
                self.__objects = json.loads(json_str)
