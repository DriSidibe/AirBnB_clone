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

    def help_quit(self):
        """"""
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """"""
        print("Quit command to exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
