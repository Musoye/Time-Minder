#!/usr/bin/python3
"""User Model"""
from models.base_model import BaseModel, Base
from datetime import datetime
from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship
from hashlib import md5


class User(BaseModel, Base):
    """User Model"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    is_suscribe = Column(Boolean, default=True)
    projects = relationship("Project", backref="user")
    tasks = relationship("Task", backref="user")

    def __init__(self):
        """The constructor Model"""
        self.updated_at = datetime.now()
        super().__init__()
    
    def __setattr__(self, name, value):
        """To convert password to hash value"""
        if name == "password":
            value = md5(value.encode()).hexdigest().lower()
        super().__setattr__(name, value)
