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
        return (FileStorage.__objects)

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        cls_name = obj.__class__.__name__
        key = cls_name + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """

        # Convert __objects to dictionary before storing in file
        object_dict  = {}
        for key, value in FileStorage.__objects.items():
            object_dict[key] = value.to_dict()

        # Serialization to JSON
        json_str = json.dumps(object_dict)

        with open(FileStorage.__file_path, "w") as file:
            file.write(json_str)

    def delete(self, obj_id):
        """ delete an object from json file """
        del self.__objects[obj_id]
        self.save()

    def reload(self):
        """
            deserializes the JSON file to __objects (only if the JSON file
            (__file_path) exists ; otherwise, do nothing. If the file doesn’t
            exist, no exception should be raised)
        """
        if os.path.exists(FileStorage.__file_path):
            json_str = ""
            with open(FileStorage.__file_path, "r") as file:
                json_str = file.read()

            # BaseModel imported here to avoid circular import
            from models.base_model import BaseModel

            # Deserialized back to python dictionary
            object_dict = json.loads(json_str)
            for key, value in object_dict.items():
                FileStorage.__objects[key] = BaseModel(**value)
