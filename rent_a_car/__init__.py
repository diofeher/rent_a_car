#!/usr/bin/env python
# encoding: utf-8
"""
__init__.py

Created by Diogenes Herminio on 2010-10-07.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""

class User(object):
    """
    User
    """
    def build(self, name, cpf):
        self.name = name
        self.cpf = cpf
      

class Car(object):
    """
    Car
    """
    def build(self, license_plate, model, brand):
        self.license_plate = license_plate
        self.model = model
        self.brand = brand
        
        
    