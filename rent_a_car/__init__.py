#!/usr/bin/env python
# encoding: utf-8
"""
__init__.py

Created by Diogenes Herminio on 2010-10-07.
Copyright (c) 2010 CobraTeam. All rights reserved.
"""
import lib

if __name__=="__main__":
    """
    Used to test if interface is working
    """
    rc = lib.CarRental()
    user = rc.create_user('dio', '123')
    gol = rc.create_car('XZA', 'Volkswagen', 'Gol')
    
    chevrolet1 = rc.create_car('XZA1', 'Veraneio', 'Chevrolet')
    chevrolet2 = rc.create_car('XZA2', 'Ipanema', 'Chevrolet')
    chevrolet3 = rc.create_car('XZA3', 'Kadet', 'Chevrolet')
    chevrolet4 = rc.create_car('XZA4', 'Omega', 'Chevrolet')
    chevrolet5 = rc.create_car('XZA5', 'Astra', 'Chevrolet')
    chevrolet6 = rc.create_car('XZA6', 'Celta', 'Chevrolet')
    chevrolet7 = rc.create_car('XZA7', 'Vectra', 'Chevrolet')
    chevrolet8 = rc.create_car('XZA8', 'Agile', 'Chevrolet')
    print user
    print chevrolet1, chevrolet2, chevrolet3, chevrolet4