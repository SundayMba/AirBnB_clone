#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
"""Console module
this module defines console program entry point
"""


class HBNBCommand(cmd.Cmd):
    """ this class is a subclass for cmd.Cmd class """

    @staticmethod
    def missing_name():
        """ print class name is missing message """
        print("** class name missing **")

    @staticmethod
    def wrong_class():
        """ print class doesn't exist message """
        print("** class doesn't exist **")

    @staticmethod
    def missing_id():
        """ print instance id is missing message """
        print("** instance id missing **")

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
            self.missing_name()
        elif model != "BaseModel":
            self.wrong_class()
        else:
            my_model = BaseModel()
            my_model.save()
            print(my_model.id)

    def do_show(self, args):
        """ show an instance of BaseModel """
        args_list = args.split()
        if len(args_list) == 0:
            self.missing_name()
        elif len(args_list) == 1 and args != "BaseModel":
            self.wrong_class()
        elif len(args_list) == 1 and args == "BaseModel":
            self.missing_id()
        else:
            my_storage = storage.all()
            for user_id, user_data  in my_storage.items():
                if args_list[1] == user_data.id:
                    print(user_data)
                    return
            print("** no instance found **")

    def do_all(self, class_name):
        """ print all instances """
        if class_name == "" or class_name == "BaseModel":
            my_storage = storage.all()
            for user_id in my_storage.keys():
                print(my_storage[user_id])
        else:
            self.wrong_class()




if __name__ == "__main__":
    HBNBCommand().cmdloop()
