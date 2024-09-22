#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.category import Category

print("All objects: {}".format(storage.count()))
print("Category objects: {}".format(storage.count(Category)))

first_state_id = list(storage.all(Category).values())[0].id
print("First state: {}".format(storage.get(Category, first_state_id)))