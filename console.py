#!/usr/bin/python3
"""
The console/command line interpreter for the airbnb
"""

import cmd
import re
from shlex import split
import models
from models.base_model import BaseModel

CLASSES = ["BaseModel", "User"]


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


def check_args(args):
    """checks if args is valid

    Args:
        args (str): the string containing the arguments passed to a command

    Returns:
        Error message if args is None or not a valid class, else the arguments
    """
    arg_list = parse(args)

    if len(arg_list) == 0:
        print("** class name missing **")
    elif arg_list[0] not in CLASSES:
        print("** class doesn't exist **")
    else:
        return arg_list


class HBNBCommand(cmd.Cmd):
    """
    The command interpreter class for AirBnB console
    """

    prompt = "(hbnb) "
    storage = models.storage

    def emptyline(self):
        return

    def do_EOF(self, line):
        """
        Exits the interactive console mode session
        """
        print("")
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def help_create(self):
        print("Creates a new instance of a class")
        print("saves it (to the JSON file) and prints the id")

    def do_create(self, args):
        """
        Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id
        """
        args_list = check_args(args=args)
        if (args_list):
            print(eval(args_list[0])().id)
            self.storage.save()

    def help_show(self):
        """
        Documentation for the show command
        """
        print("Prints the string representation of an instance", end=" ")
        print("base on class name and id")

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args_list = check_args(args=args)
        if args_list:
            if len(args_list) != 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args_list[0], args_list[1])
                if key not in self.storage.all():
                    print("** no instance found **")
                else:
                    print(self.storage.all()[key])

    def help_destroy(self):
        """
        Prints the documentation for the destroy command
        """
        print("Deletes an instance based on the class name and id")
        print("Saves the changes into the json file")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        Saves the changes into the json file
        """

        args_list = check_args(args=args)
        if args_list:
            if len(args_list) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(*args_list)
                if key in self.storage.all():
                    del self.storage.all()[key]
                    self.storage.save()
                else:
                    print("** no instance found **")

    def help_all(self):
        """
        Prints the documentation for all command
        """
        print("Prints all string representation of all instances", end=" ")
        print("based or not on the class name")

    def do_all(self, args):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        arg_list = split(args)
        objects = self.storage.all().values()
        if not arg_list:
            print([str(obj) for obj in objects])
        else:
            if arg_list[0] not in CLASSES:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects
                       if arg_list[0] in str(obj)])

    def do_update(self, args):
        """
        Updates an instance based on:
        the class name and id by adding or updating attribute
        (save the change into the JSON file)
        """
        arg_list = check_args(args)
        if arg_list:
            if len(arg_list) == 1:
                print("** instance id missing **")
            else:
                instance_id = "{}.{}".format(arg_list[0], arg_list[1])
                if instance_id in self.storage.all():
                    if len(arg_list) == 2:
                        print("** attribute name missing **")
                    elif len(arg_list) == 3:
                        print("** value missing **")
                    else:
                        obj = self.storage.all()[instance_id]
                        if arg_list[2] in type(obj).__dict__:
                            v_type = type(obj.__class__.__dict__[arg_list[2]])
                            setattr(obj, arg_list[2], v_type(arg_list[3]))
                        else:
                            setattr(obj, arg_list[2], arg_list[3])
                else:
                    print("** no instance found **")

            self.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
