# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 10:37:08 2018

@author: stmwr
"""

'''
Chapter 7  - One way slabs

slabs that are 'one way'
solid slabs
slabs cast on stay-in-place
'''


#import loadgeneration
import chapter5  #required strength
import chapter6  #structural analysis
import chapter15 # beam-columns and slab-column joints
import chapter16 #connecting between members
import chapter19 #design and durability requirements of concrete
import chapter20 #design properties of steel
import chapter21 #strength reduction factors
import chapter22 #sectional strength
import chapter24 #serviceability requirements
import chapter25 #reinforcement details
import chapter16
import chapter9

class chap7():
    '''this is for one way slabs'''
    def __init__(self):
        print('are you making solid slab cast in place slab, composit slab, \
              or prestressed?')
        pass
    
    def get_loads(self):
        loads = chapter5.load_combo()
        return loads
        
    def analysis(self):
        pass
        
    def __str__(self):
        return str(self.get_loads())
        
def tests():
    ch = chap7()       
    print(ch)

if __name__ == '__main__':
    tests()