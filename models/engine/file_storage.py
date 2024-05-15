#!/usr/bin/python3
""" storage class"""


import json

class FileStorage:
    """ save in json """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects
    
    def new(self, obj):
        self.__objects[obj.id] = obj

    def save(self):
        with open(self.__file_path, "w") as Sfile:
            json.dump(self.__objects, Sfile)

    def reload(self):
        with open(self.__file_path, "r") as Sfile:
            self.__objects = json.load(Sfile)