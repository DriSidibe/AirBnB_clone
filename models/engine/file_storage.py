#!/usr/bin/env python3
import json
import os

"""
    FileStorage that serializes instances to a
    JSON file and deserializes JSON file to instances
"""


class FileStorage:
    """ the file_storage class"""

    __file_path = "./file.json"
    __objects = {}
    __json_form = {}

    def __init__(self, *args, **kwargs):
        pass

    def all(self):
        """"""
        return (FileStorage.__objects)

    def new(self, obj):
        """"""
        _id = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[_id] = obj
        FileStorage.__json_form[_id] = obj.to_dict()

    def save(self):
        """"""
        for k, v in FileStorage.__objects.items():
            FileStorage.__json_form[k] = v.to_dict()
        with open(FileStorage.__file_path, "w") as fp:
            json.dump(FileStorage.__json_form, fp)

    def delete(self, class_name, id_model):
        id_model = class_name + "." + id_model
        if type(FileStorage.__objects[id_model]).__name__ == class_name:
            del FileStorage.__objects[id_model]
            del FileStorage.__json_form[id_model]
        else:
            print("** object not found **")

    def reload(self):
        """"""
        if os.path.isfile(FileStorage.__file_path):
            if os.path.getsize(FileStorage.__file_path) > 1:
                with open(FileStorage.__file_path) as fp:
                    FileStorage.__json_form = json.load(fp)
            else:
                FileStorage.__objects = {}
        from .knowns import knowns_obj
        FileStorage.__objects = {}
        for k, v in FileStorage.__json_form.items():
            model = object()
            name = k.split(".")[0]
            model = knowns_obj[name](**v)
            FileStorage.__objects[k] = model


if __name__ == "__main__":
    pass
