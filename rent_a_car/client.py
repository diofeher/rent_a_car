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
# There are 4 commands:
#
# To rent a car:
# /rent <car_number>
#
# To see your status:
# /status
#
# To create your account:
# /create <name> <cpf>
#   ex.: /create diogenes 011111111-11
#
# T
"""

class Terminal(object):
    """docstring for Client"""
    def __init__(self):
        print HELLO
        self.logged = False
        self.client = None
        
        # Pyro initialization
        locator = naming.NameServerLocator()
        ns = locator.getNS()
        
        # Gettin` factory
        uri = ns.resolve('factory')
        self.factory = core.getAttrProxyForURI(uri)
        
    def login(self):
        pass
    
    def create(self, command):
        match = re.match(r'^/create ([A-Za-z]+) ([\d]+)', command)
        if match and not self.logged:
            name = match.group(1)
            cpf = match.group(2)
            print '- Creating user...'
            user = self.factory.create_user(name, cpf)
            self.user = user
            print user
            #user = self.factory.create_user(name, cpf)
            print '- User created'
            print "- Automatically logged - Don't need to log in."
            #return user
        else:
            print '- Not created'

    def status(self):
        pass
    
    def command(self, command):
        if re.match(r'^/exit$', command):
            sys.exit()
        elif re.match(r'^/help$', command):
            print HELP
        elif re.match(r'^/create', command):
            self.create(command)
        else:
            print "Unknown command. Type /help to see existent commands."
    


if __name__=='__main__':
    core.initClient()
    terminal = Terminal()
    while 1:
        command = raw_input('> ')
        if not command:
            break
        terminal.command(command)
    
    print '- Goodbye!'