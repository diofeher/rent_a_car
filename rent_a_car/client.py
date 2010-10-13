#!/usr/bin/env python
# encoding: utf-8
"""
client.py

Created by Diogenes Herminio on 2010-10-07.
Copyright (c) 2010 CobraTeam. All rights reserved.
"""
import re, sys
from Pyro import core, naming


HELP = """
To login:
    /login <name>
        ex.: /login diofeher

To logout:
    /logout

To rent a car:
    /rent <license_plate>

To see your status:
    /status

To create an account:
    /create user <name> <cpf>
        ex.: /create diofeher 011111111-11

To create a car:
    /create car <license_plate> <model> <brand>
        ex.: /create car XZA-1234, Kadet, Chevrolet

To pay your debits:
    /pay

To see users of the system:
    /users

To see rented cars:
    /rented_cars
"""


class Terminal(object):
    """
    docstring for Client
    """
    def is_logged(_func):
        """
        Decorator used to test if user is logged in functions
        """
        def _new_func(self, *args, **kwargs):
            if self.logged:
                return _func(self, *args, **kwargs)
            else:
                print '- Not logged'
        return _new_func
    
    
    def __init__(self):
        self.logged = False
        self.client = None
        
        # Pyro initialization
        locator = naming.NameServerLocator()
        self.ns = locator.getNS()
        
        manager_uri = self.ns.resolve('manager')
        self.manager = core.getAttrProxyForURI(manager_uri)
        self.car_rental = self.manager.create_rental()
        print """
# Welcome to Rent A Car System.
#
# You are in %s
#
# To get help, type /help
#
# To exit, type /exit
#
""" % self.car_rental
    
    
    def login(self, name):
        if not self.logged:
            user = self.manager.search_user(name)
            if user:
                self.user = user
                self.logged = True
                print '- Logged'
            else:
                print '- Not logged (Inexistent user)'
        else:
            print 'You have already logged. Type /logout to login with other user.'
    
    @is_logged
    def logout(self):
        self.logged = False
        self.user = None
        print '- Logout successful'
    
    
    def create_user(self, name, cpf):
        if name and cpf:
            if name not in self.manager.users:
                print '- Creating user...'
                self.user = self.manager.create_user(name, cpf)
                self.logged = True
                print '- User created'
                print "- Automatically logged - Don't need to log in."
            else:
                print '- Existent user. Pick another name.'
        else:
            print '- Not created.'
    
    
    def create_car(self, attrs):
        """
        Create a car. Don't need to login.
        """
        attrs=attrs.split(',')
        license_plate=attrs[0]
        if len(attrs) != 3:
            print '- Wrong number of attributes '
        else:
            if license_plate not in self.manager.cars:
                car = self.manager.create_car(*attrs)
                print '- Car created: %s' % car
                return car
            else:
                print '- Existent license plate. Pick another.'
    
    @is_logged
    def rent(self, license_plate):
        """
        Rent a car passing a license_plate
        @param license_plate: string
        """
        car = self.manager.search_car(license_plate)
        if car:
            rented = self.manager.rent_a_car(car)
        else:
            print "%s don't exist." % license_plate
            return
            
        if not rented:
            print '%s is already rented.' % car
            return
        
        status = self.manager.check_status(self.user)
        if status:
            print '- Pay your debit before rent another car.'
            return
        
        
        print '- Renting...'
        debit = self.manager.rent(self.user, car, self.car_rental)
        print '- %s rented in %s.' % (car, self.car_rental)
    
    
    @is_logged
    def pay(self):
        car = self.manager.pay(self.user)
        if car:
            self.manager.unrent(car.license_plate)
            print '- Payed your debit. Now you can rent other cars.'
        else:
            print "- You didn't have rent any car."
    
    
    @is_logged
    def status(self):
        print self.manager.show_status(self.user)
    
    
    def users(self):
        print self.manager.users
    
    
    def exit(self):
        print 'Goodbye!'
        sys.exit(0)
    
    
    def command(self, command):
        """
        Point command to the right method
        """
        # Building regex matches
        exit_match = re.match(r'^/exit$', command)
        rent_match = re.match(r'^/rent ([A-Za-z0-9]+)$', command)
        create_car_match = re.match(r'^/create car (.+)', command)
        help_match = re.match(r'^/help$', command)
        logout_match = re.match(r'^/logout$', command)
        pay_match = re.match(r'^/pay$', command)
        users_match = re.match(r'^/users$', command)
        cars_match = re.match(r'^/cars$', command)
        rented_cars_match = re.match(r'^/rented_cars$', command)
        status_match = re.match(r'^/status$', command)
        create_user_match = re.match(r'^/create user ([A-Za-z0-9]+) ([\d]+)', command)
        login_match = re.match(r'^/login ([A-Za-z]+)', command)
        
        # Pointing command to methods
        
        if exit_match:
            self.exit()
        elif rent_match:
            self.rent(rent_match.group(1))
        elif help_match:
            print HELP
        elif create_car_match:
            self.create_car(create_car_match.group(1))
        elif users_match:
            self.users()
        elif cars_match:
            print self.manager.cars
        elif rented_cars_match:
            print self.manager.rented_cars
        elif status_match:
            self.status()
        elif pay_match:
            self.pay()
        elif logout_match:
            self.logout()
        elif create_user_match:
            self.create_user(create_user_match.group(1), create_user_match.group(2))
        elif login_match:
            self.login(login_match.group(1))
        else:
            print "Unknown command or wrong usage. Type /help to see existent commands."


if __name__=='__main__':
    # initialization of pyro client
    core.initClient()
    
    terminal = Terminal()
    
    while 1:
        command = raw_input('\n> ')
        if not command:
            terminal.exit()
        terminal.command(command)