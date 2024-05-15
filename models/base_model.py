#!/usr/bin/python3
"""
This will define the BaseModel class functioning as
the base class for all models."""

from datetime import datetime
import uuid
 

class BaseModel:
    """The Base class of all Classes"""

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.created_at = self.created_at.isoformat()
        self.updated_at = datetime.now()
        self.updated_at = self.updated_at.isoformat()
    
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        self.updated_at = datetime.now()
    
    def to_dict(self):
        b_dict = self.__dict__.copy()
        b_dict[__class__]= type(self).__name__
        return b_dict
    

my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
