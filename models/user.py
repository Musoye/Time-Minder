#!/usr/bin/python3
"""User Model"""
from models.base_model import BaseModel
from datetime import datetime
from hashlib import md5


class User(BaseModel):
    """User Model"""

    def __init__(self):
        """The constructor Model"""
        self.updated_at = datetime.now()
        super().__init__()
    
    def __setattr__(self, name, value):
        """To convert password to hash value"""
        if name == "password":
            value = md5(value.encode()).hexdigest().lower()
        super().__setattr__(name, value)
