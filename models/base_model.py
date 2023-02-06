#!/usr/bin/env python3
from uuid import uuid4
import datetime

"""
    the base model package
"""

class BaseModel:
    """ the base model class"""
    def __init__(self, *args, **kwargs):
        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.datetime.today()
            self.updated_at = self.created_at
        else:
            self.id = kwargs["id"]
            self.created_at = datetime.datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = datetime.datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            self.name = kwargs["name"]
            self.my_number = kwargs["my_number"]

    def __str__(self):
        return (f"[{self.__class__.__name__}] ({self.id}) <{self.__dict__}>")

    def save(self):
        self.updated_at = datetime.datetime.today()

    def to_dict(self):
        dict_repr = self.__dict__
        dict_repr["__class__"] = self.__class__.__name__
        dict_repr["updated_at"] = str(dict_repr["updated_at"].isoformat())
        dict_repr["created_at"] = str(dict_repr["created_at"].isoformat())
        return (dict_repr)

if __name__ == "__main__":
	pass
