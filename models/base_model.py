#!/usr/bin/python3
from datetime import datetime
import uuid
""" Base Model module for every other classes """


class BaseModel:
    """ Base Model Class """
    def __init__(self):
        """ instance initializer


            <id>: string - assign with an uuid when an instance is created
            <created_at>:  datetime - assign with the current datetime
            <updated_at>:  datetime - assign with the current datetime
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ instance representation in string format """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
            updates the public instance attribute <updated_at>
            with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
            create a dictionary representation with “simple object type"
            of our BaseModel. dictionary contains all keys/values of
            __dict__ of the instance
        """
        my_dict = self.__dict__
        my_dict["created_at"] = datetime.now().isoformat()
        my_dict["updated_at"] = datetime.now().isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict
