#!/usr/bin/env python3
"""BaseModel that defines common attributes/methods for other classes"""

import datetime
import uuid
from models import storage


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """
        Initializing the base model class
        Each key of kwargs is an attribute name
        Each value is the value of this attribute name
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        date_time_iso = datetime.datetime.fromisoformat(value)
                        setattr(self, key, date_time_iso)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.datetime.now()
            # self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self):
        """
        str representation of the obj from BaseModel
        [<class name>] (<self.id>) <self.__dict__>
        """
        class_name = type(self).__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        updates public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
        returns dictionary containing all keys/values of __dict__ of instance:
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__

        for key, value in dictionary.items():
            if key == "created_at":
                value = self.__dict__[key].isoformat()
            elif key == "updated_at":
                value = self.__dict__[key].isoformat()
            dictionary[key] = value
        return dictionary
