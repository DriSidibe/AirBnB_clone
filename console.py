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

    def is_class_exist(self, class_name):
        """"""
        if class_name in HBNBCommand.existed_classes:
            return True
        else:
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
            if is_class_exist(line_parsed[0]):
                self.show_all(line_parsed[0])
        else:
            self.show_all("")

    def show_all(self, model):
        """"""
        obj_list = []
        storage.reload()
        __objects = storage.all()
        for key, obj in __objects.items():
            if self.is_class_exist(model):
                if obj["__class__"] == model:
                    obj_list.append(self.make_obj(**obj).__str__())
            elif model == "":
                if obj["__class__"] == "BaseModel":
                    obj_list.append(BaseModel(**obj).__str__())
                elif obj["__class__"] == "User":
                    obj_list.append(User(**obj).__str__())
                elif obj["__class__"] == "Place":
                    obj_list.append(Place(**obj).__str__())
                elif obj["__class__"] == "State":
                    obj_list.append(State(**obj).__str__())
                elif obj["__class__"] == "City":
                    obj_list.append(City(**obj).__str__())
                elif obj["__class__"] == "Amenity":
                    obj_list.append(Amenity(**obj).__str__())
                elif obj["__class__"] == "Review":
                    obj_list.append(Review(**obj).__str__())
        print(obj_list)

    def update(self, args, obj):
        """"""
        model = object()
        if self.is_class_exist(args[0]):
            model = self.make_obj(**obj[args[1]])
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
    
    def parse_line(self, line):
        return list(filter(lambda w: (w != ''), line.split(" ")))

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
