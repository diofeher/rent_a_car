#!/usr/bin/env python
# encoding: utf-8
"""
server.py

Created by Diogenes Herminio on 2010-10-07.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""
from Pyro import core
from lib import Car, User

core.initServer()
daemon = core.Daemon()
daemon.useNameServer(ns)

