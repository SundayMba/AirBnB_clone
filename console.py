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

    @staticmethod
    def invalid_instance():
        """ print no instance found """
        print("** no instance found **")

    def value_conversion(self, value):
        """ perform value conversion """

        # Strip off the double quote [""] around values
        value = value.strip('"')
        if value.isdecimal():
            val = int(value)
            return val
        try:
            val = float(value)
            return val
        except ValueError:
            return value
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
        my_storage = storage.all()
        if len(args_list) == 0:
            self.missing_name()
            return
        class_exit = False
        id_exit = False
        if my_storage == {}:
            if args_list[0] != "BaseModel":
                self.invalid_instance()
                return
            if
        for key, obj in my_storage.items():
            class_name = obj.__class__.__name__
            if class_name == args_list[0]:
                class_exist = True
                if len(args_list) == 1:
                    self.missing_id()
                    return
                if obj.id == args_list[1]:
                    print(obj)
                    return

        # Check if class and id exist
        if not class_exit:
            self.wrong_class()
            return
        if not id_exist():
            self.invalid_instance()
            return

    def do_all(self, args):
        """ print all instances """
        my_storage = storage.all()
        if args == "":
            for user_id in my_storage.keys():
                print(my_storage[user_id])
            return
        class_exit = False
        for key, obj in my_storage.items():
            class_name = obj.__class__.__name__
            if class_name == args:
                print(obj)
                class_exit = True

        if not class_exit:
            self.wrong_class()

    def do_destroy(self, args):
        """ delete a given instance from the json file """
        args_list = args.split()
        my_storage = storage.all()
        if len(args_list) == 0:
            self.missing_name()
            return
        class_exit = False
        id_exist = False
        for key, obj in my_storage.items():
            class_name = obj.__class__.__name__
            if class_name == args_list[0]:
                class_exist = True
                if len(args_list) == 1:
                    self.missing_id()
                    return
                if obj.id == args_list[1]:
                    id_exist = True
                    storage.delete(key)
                    storage.save()
                    return

        # check if class and id doesnt exist
        if not class_exit:
            self.wrong_class()
            return
        if not id_exist:
            self.invalid_instance()

    def do_update(self, args):
        """ update an instance """
        my_storage = storage.all()
        args_list = args.split()
        if len(args_list) == 0:
            self.missing_name()
        else:
            class_exit = False
            id_exist = False
            for key, obj in my_storage.items():
                class_name = obj.__class__.__name__
                if class_name == args_list[0]:
                    class_exit = True
                    if len(args_list) == 1:
                        self.missing_id()
                        return
                    if obj.id == args_list[1]:
                        id_exist = True
                        if len(args_list) == 2:
                            print("** attribute name missing **")
                            return
                        if len(args_list) == 3:
                            print("** value missing **")
                            return
                        attr = args_list[2]
                        value = args_list[3]
                        c_a = "created_at"
                        u_a = "updated_at"
                        if attr != "id" and attr != c_a and attr != u_a:
                            val = self.value_conversion(value)
                            setattr(obj, attr, val)
                            return

            # Check if class name or id does not match
            if not class_exit:
                self.wrong_class()
            if not id_exist:
                self.invalid_instance()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
