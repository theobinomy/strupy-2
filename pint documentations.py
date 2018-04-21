#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 09:58:46 2017

@author: sean
"""

#personal pint documentation
#start with pint
import pint

#allows assigning units to numbers
ureg = pint.UnitRegistry()

#assigns variable and units
height = 20*ureg.feet
print(height)
#converts height in place, doesn't chang it, form making new  object
heightin = height.to(ureg.inch)
print(heightin)
#converts as original object
height.ito(ureg.meter)
print(height)

