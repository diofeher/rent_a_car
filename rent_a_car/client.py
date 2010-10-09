#!/usr/bin/env python
# encoding: utf-8
"""
client.py

Created by Diogenes Herminio on 2010-10-07.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
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
"""

class Terminal(object):
    """docstring for Client"""
    def __init__(self):
        print HELLO
        self.logged = False
        self.client = None
        
        # Pyro initialization
        locator = naming.NameServerLocator()
        self.ns = locator.getNS()
        
    def login(self):
        pass
    
    def create(self):
        pass
    
    def command(self, command):
        if re.match('^/exit$', command):
            sys.exit()
        elif re.match('^/help$', command):
            print HELP
        elif re.match('^/create', command):
            self.create()
            
    


if __name__=='__main__':
    core.initClient()
    terminal = Terminal()
    while 1:
        command = raw_input('> ')
        if not command:
            break
        terminal.command(command)
    
    print '- Goodbye!'