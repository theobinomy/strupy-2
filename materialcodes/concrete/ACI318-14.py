
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 14:34:22 2017

@author: sean
"""

#ACI 318 design assistant
#Chap 2
#load combinations
global soilbearingpressure
soilbearingpressure = 1500

import pint
from pint import UnitRegistry

unit = UnitRegistry()
default_unit = inch.unit

D = 30
Dwall = 18 *unit.pound/(unit.foot**2) * 27*unit.foot 
print(Dwall)
def min_ftg(plf):
    width = plf / soilbearingpressure
    print(width)
    depth = plf / 4
    print(depth)
    return [width,depth]

def min_steel_beam(fy = 60000, fc = 3000):
    w = int(input("what is the height\n"))
    b = int(input('what is the with\n'))
    Ag = b * w
    if (( b*w) / 20) > .02:
        print("reinforcing is adequate")
    else:
        print("add more steel")
    
#D = Dwall
L = 50
print(load_combo(D,L))


#ACI SP-17(14)
#Chapter 7, pg 43
#7.3.1.1
lengthft = 1
l = lengthft * 12
h = l/24
self_weight = (thickness_in*150) /12

#chap5 one way slab

