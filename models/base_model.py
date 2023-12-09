#!/usr/bin/python3
from datetime import datetime
import uuid
from models import storage
""" Base Model module for every other classes """


class BaseModel:
    """ Base Model Class """
    def __init__(self, *args, **kwargs):
        """ instance initializer


            <id>: string - assign with an uuid when an instance is created
            <created_at>:  datetime - assign with the current datetime
            <updated_at>:  datetime - assign with the current datetime
        """
        if kwargs == {} or kwargs is None:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():

                # Exclude the __class__ attribute
                if key != '__class__':
                    attr = key

                    # Convert created_at and updated_at to datetime object
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.fromisoformat(value)

                    # Set the attribute using setattr
                    setattr(self, attr, value)

    def __str__(self):
        """ instance representation in string format """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
            updates the public instance attribute <updated_at>
            with the current datetime
        """
        self.updated_at = datetime.now()

        # Save the entry in the file
        storage.save()

    def to_dict(self):
        """
            create a dictionary representation with “simple object type"
            of our BaseModel. dictionary contains all keys/values of
            __dict__ of the instance attribute
        """
        my_dict = self.__dict__.copy()
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict

    @classmethod
    def create(cls, **dictionary):
        """ Recreate the exact instance of the given class """

        # inline import to avoid circular import error
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review

        obj_dict = {
                "BaseModel": BaseModel,
                "User": User,
                "Place": Place,
                "State": State,
                "Review": Review,
                "City": City,
                "Amenity": Amenity
                }
        class_name = obj_dict[cls.__name__]
        obj = class_name(**dictionary)
        return obj
