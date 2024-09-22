#!/usr/bin/env python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column,String,DateTime,Integer, ForeignKey
from sqlalchemy.orm import relationship

class Document(BaseModel, Base):
    __tablename__ = 'document'
    name = Column('document name',String(60), nullable=False )
    description = Column('description',String(128), nullable=False)
    category_id = Column('category_id',String(60), ForeignKey('category.id'), nullable=False)
    cost_price = Column('cost price',Integer)
    selling_price = Column('selling price',Integer)
    
    