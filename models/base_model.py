#!/usr/bin/python3
"""
    Module define the BaseModel class and defines all
    common attributes/methods for other classes.
"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """ Class Base Model. """

    def __init__(self, *args, **kwargs):
        """ Initialize Base Model instance. """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f'))
                elif not key == "__class__":
                    setattr(self, key, val)

    def __str__(self):
        """ Prints the BaseModel Attribute of String representation. """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ Save Method - Updates the attributes with current datetime. """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Method-Return a dictionary of keys/values of __dict__ """
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["updated_at"] = d["updated_at"].isoformat()
        d["created_at"] = d["created_at"].isoformat()
        return d
