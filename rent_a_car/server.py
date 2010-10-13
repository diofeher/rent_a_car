#!/usr/bin/env python
# encoding: utf-8
"""
server.py

Created by Diogenes Herminio on 2010-10-07.
Copyright (c) 2010 CobraTeam. All rights reserved.
"""
from Pyro import core, naming, errors
import lib

def main():
    """
    server script
    """
    core.initServer()
    daemon = core.Daemon()
    ns = naming.NameServerLocator().getNS()
    daemon.useNameServer(ns)
    
    try:
        ns.unregister('manager')
    except errors.NamingError, e:
        print e
    
    manager = core.ObjBase()
    manager.delegateTo(lib.Manager())
    #lib.init_server(car_rental)
    daemon.connect(manager, 'manager')
    
    
    # enter server loop
    print "Started server..."
    daemon.requestLoop()


if __name__=="__main__":
    main()
        