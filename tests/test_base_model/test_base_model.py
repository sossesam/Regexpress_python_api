#!/usr/bin/python3
from models.base_model import BaseModel
import unittest
import datetime

class TestBaseModel(unittest.TestCase):
    base_model = BaseModel()

    
    
        

    def test_id(self):
       new_base = BaseModel()
       self.assertEqual(type(new_base.id), str)

    def test_created_at_str(self):
       new_base = BaseModel()
       self.assertEqual(type(new_base.to_dict()["created_at"]), str )

    def test_updated_at_str(self):
       new_base = BaseModel()
       self.assertEqual(type(new_base.to_dict()["updated_at"]), str )

    def test_base_model_is_class(self):
       new_base = BaseModel()
       self.assertEqual("__class__" in dir(new_base), True)

    def test_name(self):
       self.assertEqual(type(self.base_model.id), str)
    
   
        
        

if __name__ == "__main__":
   unittest.main()
       