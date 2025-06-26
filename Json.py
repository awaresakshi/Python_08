# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 12:51:20 2025

@author: admin
"""
import json

# Writing JSON
data = {"name": "sakshi", "age": 20}
with open("data.json", "w") as file:
    json.dump(data, file)

# Reading JSON
with open("data.json", "r") as file:
    loaded = json.load(file)
    print(loaded)
    
    

