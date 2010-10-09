#!/usr/bin/env python
# encoding: utf-8
"""
lib.py

Created by Diogenes Herminio on 2010-10-07.
Copyright (c) 2010 CobraTeam. All rights reserved.
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
        
class Factory(object):
    """
    docstring for Factory
    """
    def create_user(self, *args):
        """
        *args = (name, cpf)
        """
        user = User(*args)
        return user
        
    def create_car(self):
        """
        *args = (license_plate, model, brand)
        """
        car = Car(*args)
        return car
