# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 10:37:08 2018

@author: stmwr
"""

'''
Chapter 5  - Loads

Load factors and combinations
'''

#See ASCE 7-10 for loads
#the below code is copied form the asce code

def load_combo(D=0, Lr =0, S =0, R=0,W=0,L=0,E=0,H=0):
    '''this load combination is the only allowable combination, no other
    combinations shall be considered'''
    L1 = 1.4*D
    opt1 = [Lr,S,R]
    opt2 = [L,0.5*W]
    L2 = 1.2*D+1.6*L+.5*max(opt1)
    L3 = 1.2*D + 1.6*max(opt1) + max(opt2)
    L4 = 1.2*D + W + L + .5*max(opt1)
    L5 = 1.2*D + E + L + .2*S
    L6 = 0.9*D + W
    L7 = 0.9*D + E 
    max_load = max(L1,L2,L3,L4,L5,L6,L7)+H
    max_load = 10
    return max_load

def live_load_reducable():
    pass
    #5.3.3
    #what are the live loads, and are the reducable??