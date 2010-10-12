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
        self.debit = None
    
    def __repr__(self):
        return '<User object: %s>' % self.name
    
    
    def rent(self, car, car_rental):
        """
        Used to rent a car
        @param car: Car
        @param car_rental: CarRental
        """
        if not self.debit:
            self.debit = car,car_rental
            return self.debit
    
    
    def pay(self):
        if self.debit is not None:
            debit = self.debit
            self.debit = None
            return debit[0]
        else:
            return False
    
    def show_status(self):
        st = """
        - Name: %s
        - Cpf: %s
        - Status: %s
        """ % (self.name, self.cpf, self.debit or "No debits")
        return st
    
    status = property(show_status)


class Car(object):
    """
    Car
    """
    def __init__(self, license_plate, model, brand):
        self.license_plate = license_plate
        self.model = model
        self.brand = brand
    
    
    def __repr__(self):
        return "<Car: %s>" % (self.license_plate)


class CarRental(object):
    """
    docstring for CarRental
    """
    def __init__(self, name):
        self.users={}
        self.name = name
        
    def __repr__(self):
        return "<CarRental: %s>" % self.name


class Manager(object):
    """
    docstring for Manager
    """
    def __init__(self):
        self.users = {}
        self.rentals = {}
        self.cars = {}
        self.rented_cars = {}
    
    
    def create_rental(self):
        name = '%sCarRental' % random.randint(1, 1000)
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

    def unrent(self, license_plate):
        del self.rented_cars[license_plate]

    def rent_a_car(self, car):
        if car.license_plate not in self.rented_cars:
            self.rented_cars.update({car.license_plate:True})
            return car
            