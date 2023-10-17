#!/usr/bin/env python3
from uuid import uuid4
from datetime import datetime
from models import storage

"""
    the base model package
"""


class BaseModel:
    """ the base model class"""
    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            iso_format = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "id":
                    self.id = kwargs["id"]
                elif key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, iso_format)
                    setattr(self, key, value)
                elif key != "__class__":
                    setattr(self, key, value)
    
    def __str__(self):
        """ string representation of base model object """
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """ updates the public instance
        attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing all
        keys/values of __dict__ of the instance """
        dict_rep = {}
        for key in self.__dict__:
            value = self.__dict__[key]
            if key == "created_at" or key == "updated_at":
                dict_rep[key] = str(value.isoformat())
            else:
                dict_rep[key] = value
        dict_rep["__class__"] = type(self).__name__
        return dict_rep
