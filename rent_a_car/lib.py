#!/usr/bin/env python
# encoding: utf-8
"""
lib.py

Created by Diogenes Herminio on 2010-10-07.
Copyright (c) 2010 CobraTeam. All rights reserved.
"""
from Pyro import core


class User(object):
    """
    User
    """
    def __init__(self, name, cpf):
        self.name = name
        self.cpf = cpf
        
    
    def __repr__(self):
        return '<User object: %s>' % self.name
        
    
    def show_status(self):
        return """
        Name: %s
        Cpf: %s
        Status: BLA
        """ % (self.name, self.cpf)
    
    status = property(show_status)


class Car(object):
    """
    Car
    """
    def __init__(self, license_plate, model, brand):
        self.license_plate = license_plate
        self.model = model
        self.brand = brand


class CarRental(object):
    """
    docstring for CarRental
    """
    def __init__(self):
        self.users={}
        
    
    def create_user(self, name, cpf):
        """
        Create a new User
        """
        user = User(name, cpf)
        self.users.update({name:user})
        return user
        
    
    def search_user(self, name):
        """
        Method to look for user
        """
        return self.users[name]
    
    
    def create_car(self, license_plate, model, brand):
        """
        *args = (license_plate, model, brand)
        """
        car = Car(license_plate, model, brand)
        return car


if __name__=="__main__":
    args = ('name', 'cpf')
    user = User(*args)