import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        """
        Initializes a new instance of BaseModel.
        """
        self.id = str(uuid.uuid4())  # Generate a unique ID and convert it to a string
        self.created_at = datetime.now()  # Set the creation timestamp
        self.updated_at = self.created_at  # Initialize updated_at with creation timestamp

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the public instance attribute updated_at with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
