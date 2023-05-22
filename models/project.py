#!/usr/bin/Python3
"""Project  model"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Boolean,ForeignKey
from sqlalchemy.orm import relationship


class Project(BaseModel, Base):
    """The Project Model"""
    __tablename__ = 'projects'
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(128), nullable=True)
    sent = Column(Boolean, default=False)
    is_priority = Column(Boolean, default=False)
    users = relationship("User", backref="project")


    def __init__(self):
        """The project constructor class"""
        super().__init__()
