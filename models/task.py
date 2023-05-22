#!/usr/bin/Python4
"""task model"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Boolean,ForeignKey
from sqlalchemy.orm import relationship


class Task(BaseModel, Base):
    """Task Model"""
    __tablename__ = 'tasks'
    project_id = Column(String(60), ForeignKey('projects.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    status = Column(String(16), nullable=False)
    description = Column(String(128), nullable=True)
    sent = Column(Boolean, default=False)
    is_priority = Column(Boolean, default=False)
    users = relationship("User", backref="task")
    projects = relationship("Project", backref="task")

    def __init__(self):
        """The project constructor class"""
        super().__init__()
