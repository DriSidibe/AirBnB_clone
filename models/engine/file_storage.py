#!/usr/bin/env python3
import json
import os

"""
    FileStorage that serializes instances to a
    JSON file and deserializes JSON file to instances
"""


class FileStorage:
    """ the file_storage class"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self, *args, **kwargs):
        pass

    def all(self):
        """"""
        return (FileStorage.__objects)

    def new(self, obj):
        """"""
        FileStorage.__objects[obj.id] = obj.to_dict()

    def save(self):
        """"""
        with open(FileStorage.__file_path, "w") as fp:
            json.dump(FileStorage.__objects, fp)

    def delete(self, class_name, id_model):
        if FileStorage.__objects[id_model]["__class__"] == class_name:
            del FileStorage.__objects[id_model]
        else:
            print("** object not found **")

    def reload(self):
        """"""
        if os.path.isfile(FileStorage.__file_path):
            if os.path.getsize(FileStorage.__file_path) > 1:
                with open(FileStorage.__file_path) as fp:
                    FileStorage.__objects = json.load(fp)
            else:
                FileStorage.__objects = {}


if __name__ == "__main__":
    pass
