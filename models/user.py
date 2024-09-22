#!/usr/bin/env python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column,String,DateTime,Integer
class User(BaseModel, Base):
    __tablename__ = 'user'
    name = Column(String(60))
    password = Column(String(60))
    email = Column(String(60))
    first_name = Column(String(60))
    last_name = Column(String(60))
