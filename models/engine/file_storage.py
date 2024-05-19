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
        s_objects = {}
        for key, obj in self.__objects.items():
            s_objects[key] = obj.to_dict()

        with open(self.__file_path, "w") as file:
            json.dump(s_objects, file)


    def reload(self):
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    module = __import__("models." + class_name, fromlist=[class_name])
                    obj_class = getattr(module, class_name)
                    obj_instance = obj_class(**value)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass