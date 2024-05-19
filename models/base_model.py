#!/usr/bin/python3
"""
This will define the BaseModel class functioning as
the base class for all models."""


import uuid
from datetime import datetime

class BaseModel:
    """The Base class of all Classes"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        self.updated_at = datetime.now()
        self.updated_at = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    
    def __str__(self):
        """ print id , name"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """ save created time"""
        self.updated_at = datetime.now()
        self.updated_at = self.updated_at.isoformat()

    def to_dict(self):
        """ return dicit"""
        b_dict = self.__dict__.copy()
        b_dict["__class__"]= type(self).__name__
        return b_dict
    