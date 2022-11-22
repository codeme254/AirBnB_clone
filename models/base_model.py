#!/usr/bin/env python3
"""BaseModel that defines common attributes/methods for other classes"""

import uuid
import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self):
        """Initializing the base model class"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        str representation of the obj from BaseModel
        [<class name>] (<self.id>) <self.__dict__>
        """
        class_name = __class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        updates public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        returns dictionary containing all keys/values of __dict__ of instance:
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = __class__.__name__

        for key, value in dictionary.items():
            if key == "created_at":
                value = self.__dict__[key].isoformat()
            elif key == "updated_at":
                value = self.__dict__[key].isoformat()
            dictionary[key] = value
        return dictionary
