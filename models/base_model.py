#!/usr/bin/python3
"""
This will define the BaseModel class functioning as
the base class for all models."""

from datetime import datetime
import uuid
 

class BaseModel:
    """The Base class of all Classes"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for item in kwargs:
                self.__dict__[item] = kwargs[item]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.created_at = self.created_at.isoformat()
            self.updated_at = datetime.now()
            self.updated_at = self.updated_at.isoformat()
    
    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        self.updated_at = datetime.now()
        self.updated_at = self.updated_at.isoformat()
    
    def to_dict(self):
        b_dict = self.__dict__.copy()
        b_dict["__class__"]= type(self).__name__
        return b_dict
    
