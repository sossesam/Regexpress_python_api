#!/usr/bin/python3
from models import storage
from models.category import Category

all = storage.all(Category)
for each in all.values():
    print(each)
