#!/usr/bin/env python3
import json
import os

from models.car_document import Document
from models.car_make import CarMake
from models.car_model import CarModel
from models.category import Category
from models.vehicle import Vehicle
from models.base_model import BaseModel
from models.user import User

classes ={"Document": Document, "Vehicle": Vehicle, "BaseModel": BaseModel,
           "User": User, "CarMake": CarMake, "CarModel": CarModel, "Category":Category}


class FileStorage:
    __objects = {}
    __file_path = "file.json"



    def all(self, cls=None):
        if cls == None:
            return self.__objects
        else:
            new_dict = {}
            for key, value in self.__objects.items():
                if cls.__name__ == value.to_dict()["__class__"]:
                    new_dict[key] = value
            return new_dict
            
    
    def new(self, obj):
        obj_name = obj.__class__.__name__
        obj_id = obj.id
        self.__objects[f"{obj_name}.{obj_id}"] = obj

    def save(self):
        file = self.__file_path
        dump_obj = {}

        for key, value in self.__objects.items():
            dump_obj[key] = value.to_dict()
        with open(file, "w") as f:
            json.dump(dump_obj, f, indent = 2)
        f.close()
       

    def reload(self):
        print("FileStorage reloading")
        with open(self.__file_path, 'r') as f:
            jo = json.load(f)
        for key,value in jo.items():
            self.__objects[key] = classes[value["__class__"]](**value)
        
       
    
    def delete(self, cls=None):
        if cls:
            class_obj = cls.to_dict()
            class_name = class_obj["__class__"]
            class_id = class_obj["id"]
            obj_key = f"{class_name}.{class_id}"
            del self.__objects[obj_key]

    def get(self, cls, id):
        return self.__objects[f"{cls.__name__}.{id}"]

    def close(self):
            """call reload() method for deserializing the JSON file to objects"""
            self.reload()

    
    def count(self, cls=None):
        if cls == None:
            new_dict = {}
            for clss in classes:
                if cls is None or cls is classes[clss] or cls is clss:
                    objs = self.__objects
            return len(objs)
        else:
            new_dict = {}
            for key, value in self.__objects.items():
                if value.__class__.__name__ == cls.__name__:
                    new_dict[key] = value
            return len(new_dict)

        