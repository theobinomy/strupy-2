#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 22:29:44 2017

@author: sean
"""

def moment(force,distance):
    moment = force * distance
    print( moment)
    return moment

def moment_overturning(force,distance,width):
    return (force*distance/width)