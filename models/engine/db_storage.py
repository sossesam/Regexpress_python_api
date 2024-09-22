#!/usr/bin/env python3
from sqlalchemy.engine import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session

from models.car_document import Document
from models.car_make import CarMake
from models.car_model import CarModel
from models.category import Category
from models.vehicle import Vehicle
from models.base_model import BaseModel, Base
from models.user import User

classes ={"Document": Document, "Vehicle": Vehicle, "User": User, "CarMake": CarMake, "CarModel": CarModel, "Category": Category}

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        db_user = getenv("HBNB_MYSQL_USER")
        db_pwd = getenv("HBNB_MYSQL_PWD")
        my_db = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(f'mysql://{db_user}:{db_pwd}@localhost:3306/{my_db}', pool_pre_ping=True)

    def all(self, cls=None):
        
        new_dict = {}
        if cls:
            objs = self.__session.query(cls).all()
            for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    new_dict[key] = obj
            
        else:
            for key, value in classes.items():
                objs = self.__session.query(value).all()
                for obj in objs:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    new_dict[key] = obj    

        return (new_dict)
       
    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            
            self.__session.delete(obj)
            self.save()
            print("deleted")

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
         obj = self.__session.query(cls).filter(cls.id == id)

         for value in obj:
             if cls == value.__class__ and id == value.id:
                 return value

    def count(self, cls=None):
        if cls == None:
            new_dict = {}
            for clss in classes.values():
                objs = self.__session.query(clss).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
            return len(new_dict)
        else:
            return self.__session.query(cls).count()