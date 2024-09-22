#!/usr/bin/env python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column,String,DateTime,Integer
class CarMake(BaseModel, Base):
    __tablename__ = 'car_make'
    name = Column(String(60))
    description = Column(String(250))
    