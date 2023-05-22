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

    def __init__(self, *args, **kwargs):
        """The constructor class"""
        """Initialization of the base model"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.created_at = datetime.now()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.updated_at = datetime.now()
            if kwargs.get("id", None) is None:
                self.id = str(uuid4())
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
    
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
        if "_sa_instance_state" in dic:
            del dic["_sa_instance_state"]
        return (dic)
    
    def save(self):
        """updates the attribute 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()
    
    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
