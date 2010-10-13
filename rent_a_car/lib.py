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
    Class used to persist states and objects.
    If you don't persist here, objects are going to stay only in one session.
    """
    def __init__(self):
        self.users = {}
        self.rentals = {}
        self.cars = {}
        self.rented_cars = {}
        self.debits = {}
    
    
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
        return self.users.get(name)
    
    
    def search_car(self, license_plate):
        return self.cars.get(license_plate)
    
    
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
        """
        Unrent a car
        @param license_plate: string
        """
        del self.rented_cars[license_plate]
    
    def rent_a_car(self, car):
        """
        Rent a car
        @param car: Car
        """
        if car.license_plate not in self.rented_cars:
            self.rented_cars.update({car.license_plate:True})
            return car
    
    
    def rent(self, user, car, car_rental):
        """
        Used to rent a car
        @param user: User
        @param car: Car
        @param car_rental: CarRental
        """
        if user not in self.debits:
            debit = {user.name:car}
            self.debits.update(debit)
            return debit
    
    
    def check_status(self, user):
        """
        Check status of user debits
        """
        return self.debits.get(user.name)
    
    def pay(self, user):
        """
        Method used to pay a debit
        @param user: User
        """
        if user.name in self.debits:
            debit = self.debits[user.name]
            del self.debits[user.name]
            return debit
        else:
            return False
    
    
    def show_status(self, user):
        """
        @param user: User
        """
        st = """
        - Name: %s
        - Cpf: %s
        - Status: %s
        """ % (user.name, user.cpf, self.debits.get(user.name) or "No debits")
        return st
            