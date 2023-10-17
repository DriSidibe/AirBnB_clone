#!/usr/bin/env python3
import cmd
from models.base_model import BaseModel
from models import storage
import re
from models.engine.knowns import knowns_obj
from os import system, name

"""
    the console package
"""


class HBNBCommand(cmd.Cmd):
    """ the cnsole main class """

    prompt = '(hbnb) '
    existed_classes = list(knowns_obj.keys())
    const_atr = ["id", "updated_at", "created_at"]
    object_count = 0

    def do_create(self, line):
        """"""
        if line == "":
            print("** class name missing **")
        elif self.is_class_exist(line):
            new_object = knowns_obj[line]()
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
        model = knowns_obj[name](**args)
        return model

    def obj_to_dict(self, obj):
        dic = {}
        for k, v in obj.items():
            dic[k] = v.to_dict()
        return dic

    def show_or_destroy(self, mth, name, key):
        """"""
        if len(key) == 1:
            print("** instance id missing **")
        else:
            storage.reload()
            _objects = storage.all()
            __objects = self.obj_to_dict(_objects)
            _k = name + "." + key[1]
            if _k in __objects:
                if mth == "show":
                    if self.is_class_exist(name):
                        if __objects[_k]["__class__"] == name:
                            print(self.make_obj(name, **__objects[_k]))
                        else:
                            print("** no instance found **")
                else:
                    storage.delete(name, key[1])
                    storage.save()
            else:
                print("** no instance found **")

    def do_show(self, line):
        """"""
        line_parsed = self.parse_line(line)
        if line_parsed == []:
            print("** class name missing **")
        elif self.is_class_exist(line_parsed[0]):
            self.show_or_destroy("show", line_parsed[0], line_parsed)

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
        _objects = storage.all()
        __objects = self.obj_to_dict(_objects)
        HBNBCommand.object_count = 0
        for key, obj in __objects.items():
            if self.is_class_exist(model, False):
                if obj["__class__"] == model:
                    obj_list.append(self.make_obj(model, **obj).__str__())
                    HBNBCommand.object_count += 1
            elif model == "":
                _ = self.make_obj(obj["__class__"], **obj).__str__()
                obj_list.append(_)
        if show:
            print(obj_list)

    def update(self, args, obj):
        """"""
        model = object()
        _k = args[0] + "." + args[1]
        if self.is_class_exist(args[0]):
            model = self.make_obj(args[0], **obj[_k])
        return model

    def do_clear(self, line):
        system('cls' if name == 'nt' else 'clear')

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
                _objects = storage.all()
                __objects = self.obj_to_dict(_objects)
                _k = line_parsed[0] + "." + line_parsed[1]
                if _k in __objects:
                    if len(line_parsed) == 2:
                        print("** attribute name missing **")
                    else:
                        if len(line_parsed) == 3:
                            print("** value missing **")
                        else:
                            if line_parsed[2] in HBNBCommand.const_atr:
                                pass
                            else:
                                _ = line_parsed[3].strip("\"")
                                __objects[_k][line_parsed[2]] = _
                                new_model = self.update(line_parsed, __objects)
                                storage.new(new_model)
                                storage.save()
                else:
                    print("** no instance found **")

    def parse_line(self, line, char=" "):
        return list(filter(lambda w: (w != ''), line.split(char)))

    def w_out(self, s):
        if s[0] == "\"":
            return s[1:len(s)-1]

    def precmd(self, line):
        line = line.strip()
        line_parsed = self.parse_line(line, ".")
        exp_show = r"^((show)|(destroy))\(\"[\w-]*\"\)$"
        e_upd_1 = r"\( *\"[\w-]*\" *, *\"[\w_-]*\" *, *((.*)|(\".*\"))* *\)"
        # e_upd_2 =
        # "\( *[\"\w-]*\" *, *{ *(\"[a-zA-Z0-9_-]*\" *
        # : *((.*)|(\".*\"))* *,? *)+ *} *\)"
        if len(line_parsed) == 2:
            if len(line_parsed[0]) != 0:
                if line_parsed[1] == "all()":
                    if self.is_class_exist(line_parsed[0]):
                        self.do_all(line_parsed[0])
                elif line_parsed[1] == "count()":
                    if self.is_class_exist(line_parsed[0]):
                        self.show_all(line_parsed[0], False)
                        print(HBNBCommand.object_count)
                elif re.search(exp_show, line_parsed[1]):
                    if self.is_class_exist(line_parsed[0]):
                        res = self.parse_line(line_parsed[1], "(")
                        _id = res[1]
                        _id = self.parse_line(_id, ")")[0]
                        _id = _id[1:len(_id)-1]
                        fun = getattr(self, f"do_{res[0]}")
                        fun(f"{line_parsed[0]} {_id}")
                elif re.search(f"^update{e_upd_1}$", line_parsed[1]):
                    if self.is_class_exist(line_parsed[0]):
                        _id = self.parse_line(line_parsed[1], "(")[1]
                        __ = self.parse_line(_id, ",")
                        _id = self.w_out(__[0].strip())
                        _attr_name = self.w_out(__[1].strip())
                        _ = self.parse_line(__[2], ")")[0].strip()
                        _value = self.w_out(_)
                        __ = f"{line_parsed[0]} {_id} {_attr_name} {_value}"
                        self.do_update(__)
                # elif re.search(f"^update{e_upd_2}$", line_parsed[1]):
                #    if self.is_class_exist(line_parsed[0]):
                #        pass
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
        _ = "update <class name> <id> <attribute name> \"<attribute value>\""
        print(_)

    def help_quit(self):
        """"""
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """"""
        print("Quit command to exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
