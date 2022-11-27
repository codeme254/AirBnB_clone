#!/usr/bin/python3
"""
The console/command line interpreter for the airbnb
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    The command interpreter class for AirBnB console
    """

    prompt = "(hbnb) "

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
