#!/usr/bin/env python3
from uuid import uuid4
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,DateTime
import os

Base = declarative_base()
class BaseModel:
    
    
    id = Column(String(60), primary_key=True, nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    updated_at = Column(DateTime, default=datetime.utcnow())
    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if(kwargs):
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        
        else:
            pass

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    
    def save(self):
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        base_object = {**self.__dict__}
        base_object["created_at"] = datetime.strftime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
        base_object["updated_at"] = datetime.strftime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
        base_object["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in base_object.keys():
            del base_object["_sa_instance_state"]

        return base_object

    def delete(self):
        from models import storage
        storage.delete(self)
