!#/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

    def do_quit(self, args):
        """The Quit Command can exit the program"""
        return True
    def do_EOF(self, args):
        """EOF command can exit the program"""
        print('')
        return True
    def emptyline(self):
        """donot execue anything"""
        return


if __name__ = '__main__':
    HBNBCommand().cmdloop()
