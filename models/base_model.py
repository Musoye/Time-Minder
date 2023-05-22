#!/usr/bin/python3
"""The Base Model"""
from datetime import datetime
import models
from uuid import uuid4
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel:
    """Declare the base model"""

    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now)

    def __init__(self):
        """The constructor class"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
    
    def to_dict(self):
        """Convert to dict"""
        dic = self.__dict__.copy()
        if 'created_at' in dic:
            dic['created_at'] = dic['created_at'].strftime("%Y-%m-%dT%H:%M:%S.%f")
        if 'expiry_date' in dic:
            dic['expiry_date'] = dic['expiry_date'].strftime("%Y-%m-%dT%H:%M:%S.%f")
        if 'updated_at' in dic:
            dic['updated_at'] = dic['updated_at'].strftime("%Y-%m-%dT%H:%M:%S.%f")
        dic['__class__'] = type(self).__name__
        return (dic)
    
    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
    
    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
