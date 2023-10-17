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
