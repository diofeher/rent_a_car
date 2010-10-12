#!/usr/bin/env python
# encoding: utf-8
"""
server.py

Created by Diogenes Herminio on 2010-10-07.
Copyright (c) 2010 CobraTeam. All rights reserved.
"""
from Pyro import core, naming, errors
import lib

if __name__=="__main__":
    core.initServer()
    daemon = core.Daemon()
    ns = naming.NameServerLocator().getNS()
    daemon.useNameServer(ns)

    try:
        ns.unregister('car_rental')
    except errors.NamingError, e:
        print e
    
    car_rental = core.ObjBase()
    car_rental.delegateTo(lib.CarRental())
    daemon.connect(car_rental, 'car_rental')
    
    # enter server loop
    print "Started server..."
    daemon.requestLoop()
        