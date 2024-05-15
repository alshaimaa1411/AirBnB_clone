#!/usr/bin/python3
"""
This will define the BaseModel class functioning as
the base class for all models."""

from datetime import datetime
from uuid import uuid4
import models

class BaseModel:
    """The Base class of all Classes"""

    def __init__(self, *args, **kwargs):

