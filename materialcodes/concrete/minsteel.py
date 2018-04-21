# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 21:22:57 2017

@author: stmwr
"""

#Min steelers
a = 1
b = 10
class min_steel(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.ag = a*b
    def min_steel_beam(fy = 60000, fc = 3000):
        w = int(input("what is the height\n"))
        b = int(input('what is the with\n'))
        Ag = b * w
        if (( b*w) / 20) > .02:
            print("reinforcing is adequate")
        else:
            print("add more steel")
            
    def min_steel_one_way_slab(fy = 60000, fc = 3000):
        aa = (a*b)
        bb = (a*.004)
        return max(aa,bb)
    
    def min_steel_two_way_slab(fy = 60000, fc = 3000):
        aa = (a*b)
        bb = (a*.004)
        return max(aa,bb)
    
    
    def min_steel_beam(fy = 60000, fc = 3000):
        minA = (3*fc**.5*ag)/fy
        minB = (200*ag)/fy
        return max(minA, minB)
    
rebarSize = {'#1':1,'#2':2,'#3':3,'#4':4}