#!/usr/bin/python3
"""entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage

classes = {
        'Basemodel',
        'State',
        'Amenity',
        'User',
        'Place',
        'Review',
        'City'
        }

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'

  def parse(arg):
      """To Parse the arguments"""
      return arg.split(), len(arg..split())

   def do_quit(self, args):
        """The Quit Command can exit the program"""
        return True
   
   def do_EOF(self, args):
        """EOF command can exit the program"""
        print('')
        return True
   
   def emptyline(self):
        """donot execute anything"""
        return
    def do_create(self, args):
        """create new instance and print the id
        prints an error if class name missing or
        dont exist"""
        args, n = parse(args)
        if not n:
            print("** class name missing **")
        elif args[0] not in classes:
            print('** class doesn\'t exist **')
        else n == 1:
            temp = classes[args[0]]()
            storage.new(temp)
            storage.save()
            print('{}'.format(temp.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])


if __name__ = '__main__':
    HBNBCommand().cmdloop()
