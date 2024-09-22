#!/usr/bin/env python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column,String,DateTime,Integer

class CarModel(BaseModel, Base):
    __tablename__ = 'car_model'
    name = Column(String(60))
    description = Column(String(250))
    make_id = Column(String(60))
    