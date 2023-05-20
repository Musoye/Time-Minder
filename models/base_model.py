from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Declare the base model"""

    def __init__(self):
        """The constructor class"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
    
    def to_dict(self):
        """Convert to dict"""
        self.__dict__['__class__'] = type(self).__name__
        return (self.__dict__)
