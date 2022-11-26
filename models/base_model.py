#!/usr/bin/python3
"""
Module that implements the base model class
"""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    A class that defines common attr/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance
        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("created_at", "updated_at"):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """
        Prints [<class name>] (<self.id>) <self.__dict__>
        """
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        updates public instance attribute updated_at with current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
         returns dictionary containing keys/values of __dict__ of instance
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__

        for key, value in dictionary.items():
            if key in ("created_at", "updated_at"):
                value = self.__dict__[key].isoformat()
                dictionary[key] = value
        return dictionary
