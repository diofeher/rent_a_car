#!/usr/bin/env python
# encoding: utf-8
"""
server.py

Created by Diogenes Herminio on 2010-10-07.
Copyright (c) 2010 CobraTeam. All rights reserved.
"""
from Pyro import core, naming, errors
import lib

class Factory(lib.Factory, core.ObjBase):
    pass


if __name__=="__main__":
    core.initServer()
    daemon = core.Daemon()
    ns = naming.NameServerLocator().getNS()
    daemon.useNameServer(ns)

    try:
        ns.unregister('factory')
    except errors.NamingError, e:
        print e
     
    # connect factory to daemon
    uri = daemon.connect(Factory(), 'factory')
    
    # enter server loop
    print "Started server..."
    daemon.requestLoop()
        