#!/usr/bin/env python
# encoding: utf-8
"""
lib.py

Created by Diogenes Herminio on 2010-10-07.
Copyright (c) 2010 CobraTeam. All rights reserved.
"""
from Pyro import core

import random

class User(object):
    """
    User
    """
    def __init__(self, name, cpf):
        self.name = name
        self.cpf = cpf
        self.rents = {}
    
    def __repr__(self):
        return '<User object: %s>' % self.name
    
    
    def rent(self, car, car_rental):
        self.rents.update({car:car_rental})
    
    
    def show_status(self):
        return """
        Name: %s
        Cpf: %s
        Status: %s
        """ % (self.name, self.cpf, self.rents)
    
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
    def __init__(self, name):
        self.users={}
        self.name = name
    
    
    def rent_a_car(self, user, car):
        """
        @param user: User
        @param car: Car
        """


class Manager(object):
    """
    docstring for Manager
    """
    def __init__(self):
        self.users = {}
        self.rentals = {}
        self.cars = {}
    
    
    def create_rental(self):
        name = '%s' % random.randint(1, 1000)
        rental = CarRental(name)
        self.rentals.update({name:rental})
        return rental
    
    
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
    
    
    def search_car(self, license_plate):
        return self.cars[license_plate]
    
    
    def create_car(self, license_plate, model, brand):
        """
        *args = (license_plate, model, brand)
        @param license_plate: string
        @param model: string
        @param brand: brand
        """
        car = Car(license_plate, model, brand)
        self.cars.update({license_plate:car})
        return car
