#!/usr/bin/Python4
"""task model"""
from models.base_model import BaseModel


class Project(BaseModel):
    """The Project Model"""

    def __init__(self):
        """The project constructor class"""
        super().__init__()
