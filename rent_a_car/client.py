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
        
        # Set the User_URI
        # self.user_uri = self.ns.resolve('user')
        # Anonymous function to show status
        self.show_status = lambda x: "Nome: %s \nCpf: %s" % (x.name, x.cpf)
    
    
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
    
    
    def logout(self):
        if self.logged:
            self.logged = False
            self.user = None
            print '- Logout successful'
        else:
            print '- Not logged.'
    
    
    def create(self, command):
        match = re.match(r'^/create ([A-Za-z]+) ([\d]+)', command)
        if match and not self.logged:
            name = match.group(1)
            cpf = match.group(2)
            print '- Creating user...'
            self.user = self.manager.create_user(name, cpf)
            self.logged = True
            print '- User created'
            print "- Automatically logged - Don't need to log in."
        else:
            print '- Not created'
    
    
    def status(self):
        if self.logged:
            print self.user.status
        else:
            print '- Not logged.'
    
    
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
        help_match = re.match(r'^/help$', command)
        logout_match = re.match(r'^/logout$', command)
        users_match = re.match(r'^/users$', command)
        status_match = re.match(r'^/status$', command)
        create_match = re.match(r'^/create', command)
        login_match = re.match(r'^/login ([A-Za-z]+)', command)
        
        # Directing
        
        if exit_match:
            self.exit()
        elif help_match:
            print HELP
        elif users_match:
            self.users()
        elif status_match:
            self.status()
        elif logout_match:
            self.logout()
        elif create_match:
            self.create(command)
        elif login_match:
            self.login(login_match.group(1))
        else:
            print "Unknown command or wrong usage. Type /help to see existent commands."



if __name__=='__main__':
    core.initClient()
    terminal = Terminal()
    while 1:
        command = raw_input('> ')
        if not command:
            terminal.exit()
        terminal.command(command)