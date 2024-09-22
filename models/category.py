#!/usr/bin/env python3
from models.base_model import BaseModel, Base
from sqlalchemy import Column,String,DateTime,Integer
from sqlalchemy.orm import relationship
import os


class Category(BaseModel, Base):
    __tablename__ = 'category'
    name = Column(String(60), nullable=False)
    description = Column(String(128))

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        document = relationship("Document", backref='category', cascade="all, delete, delete-orphan")

    else:
        @property
        def get_document(self, category_id):
            from models import storage
            from models.car_document import Document
            all_docs = storage.all(Document)
            category_docs = []
            for each_docs in all_docs:
                if category_id == each_docs["id"]:
                    category_docs.append(each_docs)
            return category_docs

