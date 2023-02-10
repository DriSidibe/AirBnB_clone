#!/usr/bin/env python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
import re

"""
    the console package
"""


class HBNBCommand(cmd.Cmd):
    """ the cnsole main class """

    prompt = '(hbnb) '
    existed_classes = ["BaseModel",
                       "User",
                       "Place",
                       "State",
                       "City",
                       "Amenity",
                       "Review"]
    object_count = 0
    
    def do_create(self, line):
        """"""
        if line == "":
            print("** class name missing **")
        elif self.is_class_exist(line):
            if line == "BaseModel":
                new_object = BaseModel()
            elif line == "User":
                new_object = User()    
            elif line == "Place":
                new_object = Place()    
            elif line == "State":
                new_object = State()    
            elif line == "City":
                new_object = City()    
            elif line == "Amenity":
                new_object = Amenity()    
            elif line == "Review":
                new_object = Review()    
            new_object.save()
            print(new_object.id)

    def is_class_exist(self, class_name, show=True):
        """"""
        if class_name in HBNBCommand.existed_classes:
            return True
        else:
            if show:
                print("** class doesn't exist **")
            return False

    def make_obj(self, name, **args):
        """"""
        model = object()
        if name == "BaseModel":
            model = BaseModel(**args)
        elif name == "User":
            model = User(**args)
        elif name == "Place":
            model = Place(**args)
        elif name == "City":
            model = City(**args)
        elif name == "Amenity":
            model = Amenity(**args)
        elif name == "Review":
            model = Review(**args)
        elif name == "State":
            model = State(**args)
        return model

    def show_or_destroy(self, mth, class_name, key):
        """"""
        if len(key) == 1:
            print("** instance id missing **")
        else:
            storage.reload()
            __objects = storage.all()
            if key[1] in __objects:
                if mth == "show":
                    if self.is_class_exist(class_name):
                        if __objects[key[1]]["__class__"] == class_name:
                            print(self.make_obj(class_name, **__objects[key[1]]))
                        else:
                            print("** no instance found **")
                else:
                    storage.delete(class_name, key[1])
                    storage.save()
            else:
                print("** no instance found **")

    def do_show(self, line):
        """"""
        line_parsed = self.parse_line(line)
        if line_parsed == []:
            print("** class name missing **")
        elif self.is_class_exist(line_parsed[0]):
            self.show_or_destroy("show" ,line_parsed[0], line_parsed)

    def do_destroy(self, line):
        """"""
        line_parsed = self.parse_line(line)
        if line_parsed == []:
            print("** class name missing **")
        else:
            if self.is_class_exist(line_parsed[0]): 
                self.show_or_destroy("destroy", line_parsed[0], line_parsed)

    def do_all(self, line):
        """"""
        line_parsed = self.parse_line(line)
        if len(line_parsed) != 0:
            if self.is_class_exist(line_parsed[0]):
                self.show_all(line_parsed[0])
        else:
            self.show_all("")

    def show_all(self, model, show=True):
        """"""
        obj_list = []
        storage.reload()
        __objects = storage.all()
        HBNBCommand.object_count = 0
        for key, obj in __objects.items():
            if self.is_class_exist(model, False):
                if obj["__class__"] == model:
                    obj_list.append(self.make_obj(model, **obj).__str__())
                    HBNBCommand.object_count += 1
            elif model == "":
                obj_list.append(self.make_obj(obj["__class__"], **obj).__str__())
        if show:
            print(obj_list)

    def update(self, args, obj):
        """"""
        model = object()
        if self.is_class_exist(args[0]):
            model = self.make_obj(args[0], **obj[args[1]])
        return model

    def do_update(self, line):
        """"""
        line_parsed = self.parse_line(line)
        if line_parsed == []:
            print("** class name missing **")
        elif self.is_class_exist(line_parsed[0]):
            if len(line_parsed) == 1:
                print("** instance id missing **")
            else:
                storage.reload()
                __objects = storage.all()
                if line_parsed[1] in __objects:
                    if len(line_parsed) == 2:
                        print("** attribute name missing **")
                    else:
                        if len(line_parsed) == 3:
                            print("** value missing **")
                        else:
                            if line_parsed[2] in ["id", "updated_at", "created_at"]:
                                pass
                            else:
                                __objects[line_parsed[1]][line_parsed[2]] = line_parsed[3].strip("\"")
                                new_model = self.update(line_parsed, __objects)
                                storage.new(new_model)
                                storage.save()
                else:
                    print("** no instance found **")
    
    def parse_line(self, line, char=" "):
        return list(filter(lambda w: (w != ''), line.split(char)))

    def precmd(self, line):
        line = line.strip()
        line_parsed = self.parse_line(line, ".")
        if len(line_parsed) == 2:
            if len(line_parsed[0]) != 0:
                if line_parsed[1] == "all()":
                    if self.is_class_exist(line_parsed[0]):
                        self.do_all(line_parsed[0])
                elif line_parsed[1] == "count()":
                    if self.is_class_exist(line_parsed[0]):
                        self.show_all(line_parsed[0], False)
                        print(HBNBCommand.object_count)
                elif re.search("^show\([\w-]*\)$", line_parsed[1]):
                    if self.is_class_exist(line_parsed[0]):
                        _id = self.parse_line(line_parsed[1], "(")[1]
                        _id = self.parse_line(_id, ")")[0]
                        self.do_show(f"{line_parsed[0]} {_id}")
                elif re.search("^destroy\([\w-]*\)$", line_parsed[1]):
                    if self.is_class_exist(line_parsed[0]):
                        _id = self.parse_line(line_parsed[1], "(")[1]
                        _id = self.parse_line(_id, ")")[0]
                        self.do_destroy(f"{line_parsed[0]} {_id}")
                elif re.search("^update\( *[\w-]* *, *[\w_-]* *, *.* *\)$", line_parsed[1]):
                    if self.is_class_exist(line_parsed[0]):
                        _id = self.parse_line(line_parsed[1], "(")[1]
                        __ = self.parse_line(_id, ",")
                        _id = __[0].strip()
                        _attr_name = __[1].strip()
                        _value = self.parse_line(__[2], ")")[0].strip()
                        self.do_update(f"{line_parsed[0]} {_id} {_attr_name} {_value}")
                else:
                    return line
            else:
                return line
        else:
            return line
        return ""

    def emptyline(self):
        """"""
        pass

    def do_quit(self, line):
        """"""
        return True

    def do_EOF(self, line):
        """"""
        return True

    def help_update(self):
        """"""
        print("update <class name> <id> <attribute name> \"<attribute value>\"")

    def help_quit(self):
        """"""
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """"""
        print("Quit command to exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
