#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
"""Console module
this module defines console program entry point
"""


class HBNBCommand(cmd.Cmd):
    """ this class is a subclass for cmd.Cmd class """

    # Custom prompt
    prompt = "(hbnb) "

    def do_quit(self, args):
        """usage: (hbnb) quit
        Quit the program
        """
        return True

    def do_EOF(self, args):
        """usage: (hbnb) ^D or (hbnb) EOF
        Mark End of the file => Quit the program
        """
        return True

    def emptyline(self):
        """emptyline + Enter
        make sure nothing is executed when the line is empty
        """
        return

    def do_create(self, model):
        """Create an instance of BaseModel """
        if model == "":
            print("** class name missing **")
        elif model != "BaseModel":
            print("** class doesn't exist **")
        else:
            my_model = BaseModel()
            my_model.save()
            print(my_model.id)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
