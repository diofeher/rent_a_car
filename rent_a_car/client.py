#!/usr/bin/env python
# encoding: utf-8
"""
client.py

Created by Diogenes Herminio on 2010-10-07.
Copyright (c) 2010 CobraTeam. All rights reserved.
"""
import re, sys
from Pyro import core, naming

HELLO = """
# Welcome to Rent A Car System.
#
# To get help, type /help
#
# To login, type /login <name>
#
# To exit, type /exit
#
"""

HELP = """
There are 4 commands:

To rent a car:
    /rent <license_plate>

To see your status:
    /status

To create your account:
    /create <name> <cpf>
        ex.: /create diofeher 011111111-11

To login:
    /login <name>
        ex.: /login diofeher

To see users of the system:
    /users
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
        print HELLO
        self.logged = False
        self.client = None
        
        # Pyro initialization
        locator = naming.NameServerLocator()
        self.ns = locator.getNS()
        
        manager_uri = self.ns.resolve('manager')
        self.manager = core.getAttrProxyForURI(manager_uri)
        self.car_rental = self.manager.create_rental()
    
    
    def login(self, name):
        if not self.logged:
            try:
                user = self.manager.search_user(name)
                self.user = user
                self.logged = True
                print '- Logged'
            except Exception, e:
                print e
                print '- Not logged'
        else:
            print 'You have already log. Type /logout to login with other user.'
    
    @is_logged
    def logout(self):
        self.logged = False
        self.user = None
        print '- Logout successful'
    
    
    def create_user(self, name, cpf):
        if name and cpf and not self.logged:
            print '- Creating user...'
            self.user = self.manager.create_user(name, cpf)
            self.logged = True
            print '- User created'
            print "- Automatically logged - Don't need to log in."
        else:
            print '- Not created'
    
    
    def create_car(self, attrs):
        attrs=attrs.split(',')
        if len(attrs) != 3:
            print '- Wrong number of attributes'
        else:
            print '- Car created'
            return self.manager.create_car(*attrs)
    
    
    def rent(self, license_plate):
        print '- Renting...'
        car = self.manager.search_car(license_plate)
        debit = self.user.rent(car, self.car_rental)
        if debit:
            print '- %s rented in %s.' % (car, self.car_rental)
        else:
            print '- Pay your debit before rent another car.'
            
    def pay(self):
        payed = self.user.pay()
        if payed:
            print '- Payed your debit. Now you can rent other cars.'
        else:
            print "- You didn't have rent any car."
    
    
    @is_logged
    def status(self):
        print self.user.status
    
    
    def users(self):
        print self.manager.users
    
    
    def exit(self):
        print 'Goodbye!'
        sys.exit(0)
    
    
    def command(self, command):
        """
        Direct command to right function
        """
        # Building regex matches
        exit_match = re.match(r'^/exit$', command)
        rent_match = re.match(r'^/rent ([A-Za-z0-9]+)$', command)
        create_car_match = re.match(r'^/create car (.+)', command)
        help_match = re.match(r'^/help$', command)
        logout_match = re.match(r'^/logout$', command)
        pay_match = re.match(r'^/pay$', command)
        users_match = re.match(r'^/users$', command)
        status_match = re.match(r'^/status$', command)
        create_user_match = re.match(r'^/create user ([A-Za-z]+) ([\d]+)', command)
        login_match = re.match(r'^/login ([A-Za-z]+)', command)
        
        # Directing
        
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
    core.initClient()
    terminal = Terminal()

    # create cars in initialization
    init_file = open('commands.txt', 'r')
    for f in init_file:
        terminal.command(f)
    init_file.close()

    while 1:
        command = raw_input('\n> ')
        if not command:
            terminal.exit()
        terminal.command(command)