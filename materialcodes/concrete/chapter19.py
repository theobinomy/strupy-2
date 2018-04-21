# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 10:37:08 2018

@author: stmwr
"""

'''
Chapter 19 - Concrete design and durability requirements
'''

class chap19():
    def __init__(self):
        self.strength = 3000
    def limit_for_fc(self):
        [{'application':'general','concrete':'normal and lightweight','min':2500,'max':'None'},
        {'application':'special moment frames','concrete':'normal','min':3000,'max':'None'},
        {'application':'special moment frames','concrete':'lightweight','min':3000, 'max':5000}]
    def mod_of_rupt(self, lamb, fc):
        fr = 7.5 * lamb * (fc ** .5)
    def lamb(self):
        #note: linear interpolation reqd for 
        lamb = {'all lightweight':.75,'sand lightweight':.8, 'sand lightweight':.85,
               'coarse sand lightweight': .9,'normalweight':1} 
        