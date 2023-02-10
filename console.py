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
        elif not self.is_class_exist(line): 
            print("** class doesn't exist **")
        else:
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
            return False

    def show_or_destroy(self, mth, class_name, key):
        """"""
        if len(key) == 1:
            print("** instance id missing **")
        else:
            storage.reload()
            __objects = storage.all()
            if key[1] in __objects:
                if mth == "show":
                    if class_name == "BaseModel":
                        if __objects[key[1]]["__class__"] == "BaseModel":
                            print(BaseModel(**__objects[key[1]]))
                        else:
                            print("** no instance found **")
                    elif class_name == "User":
                        if __objects[key[1]]["__class__"] == "User":
                            print(User(**__objects[key[1]]))
                        else:
                            print("** no instance found **")
                    elif class_name == "Place":
                        if __objects[key[1]]["__class__"] == "Place":
                            print(Place(**__objects[key[1]]))
                        else:
                            print("** no instance found **")
                    elif class_name == "State":
                        if __objects[key[1]]["__class__"] == "State":
                            print(State(**__objects[key[1]]))
                        else:
                            print("** no instance found **")
                    elif class_name == "City":
                        if __objects[key[1]]["__class__"] == "City":
                            print(City(**__objects[key[1]]))
                        else:
                            print("** no instance found **")
                    elif class_name == "Amenity":
                        if __objects[key[1]]["__class__"] == "Amenity":
                            print(Amenity(**__objects[key[1]]))
                        else:
                            print("** no instance found **")
                    elif class_name == "Review":
                        if __objects[key[1]]["__class__"] == "Review":
                            print(Review(**__objects[key[1]]))
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
        elif not self.is_class_exist(line_parsed[0]):
            print("** class doesn't exist **")
        else:
            self.show_or_destroy("show" ,line_parsed[0], line_parsed)

    def do_destroy(self, line):
        """"""
        line_parsed = self.parse_line(line)
        if line_parsed == []:
            print("** class name missing **")
        else:
            if not self.is_class_exist(line_parsed[0]): 
                print("** class doesn't exist **")
            else:
                self.show_or_destroy("destroy", line_parsed[0], line_parsed)

    def do_all(self, line):
        """"""
        line_parsed = self.parse_line(line)
        if len(line_parsed) != 0:
            if line_parsed[0] == "BaseModel":
                self.show_all("BaseModel")
            elif line_parsed[0] == "User":
                self.show_all("User")
            elif line_parsed[0] == "Place":
                self.show_all("Place")
            elif line_parsed[0] == "State":
                self.show_all("State")
            elif line_parsed[0] == "City":
                self.show_all("City")
            elif line_parsed[0] == "Amenity":
                self.show_all("Amenity")
            elif line_parsed[0] == "Review":
                self.show_all("Review")
            else:
                print("** class doesn't exist **")
        else:
            self.show_all("")

    def show_all(self, model):
        """"""
        obj_list = []
        storage.reload()
        __objects = storage.all()
        for key, obj in __objects.items():
            if model == "BaseModel":
                if obj["__class__"] == "BaseModel":
                    obj_list.append(BaseModel(**obj).__str__())
            elif model == "User":
                if obj["__class__"] == "User":
                    obj_list.append(User(**obj).__str__())
            elif model == "Place":
                if obj["__class__"] == "Place":
                    obj_list.append(Place(**obj).__str__())
            elif model == "State":
                if obj["__class__"] == "State":
                    obj_list.append(State(**obj).__str__())
            elif model == "City":
                if obj["__class__"] == "City":
                    obj_list.append(City(**obj).__str__())
            elif model == "Amenity":
                if obj["__class__"] == "Amenity":
                    obj_list.append(Amenity(**obj).__str__())
            elif model == "Review":
                if obj["__class__"] == "Review":
                    obj_list.append(Review(**obj).__str__())
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
        if args[0] == "BaseModel":
            model = BaseModel(**obj[args[1]])
        elif args[0] == "User":
            model = User(**obj[args[1]])
        elif args[0] == "Place":
            model = Place(**obj[args[1]])
        elif args[0] == "State":
            model = State(**obj[args[1]])
        elif args[0] == "City":
            model = City(**obj[args[1]])
        elif args[0] == "Amenity":
            model = Amenity(**obj[args[1]])
        elif args[0] == "Review":
            model = Review(**obj[args[1]])
        return model

    def do_update(self, line):
        """"""
        line_parsed = self.parse_line(line)
        if line_parsed == []:
            print("** class name missing **")
        elif line_parsed[0] == "BaseModel":
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
        else:
            print("** class doesn't exist **")

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
