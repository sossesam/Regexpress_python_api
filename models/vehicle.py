#!/usr/bin/env python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column,String,DateTime,Integer

class Vehicle(BaseModel, Base):
    __tablename__ = 'make_and_model'
    name = Column(String(60))
    make_id = Column(String(60))
    model_id = Column(String(60))
    category_id = Column(String(60))
