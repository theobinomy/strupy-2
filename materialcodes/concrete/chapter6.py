# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 10:37:08 2018

@author: stmwr
"""

'''
Chapter 6  - Structural analysis

How to do analysis and calcs for concrete structures
'''


def column_slenderness_flowchart():
    z = input('would you like to neglect slenderness? y/n: ')
    if not z == 'y':
        k = input('analyze column as nonsway? y/n: ')
        if k == 'y':
            print('slenderness check at ends, ')
            print('slnderness check along length. 6.7')
        else:
            print('slnderness check along length. 6.6.4.1')
        print('second order, see 6.2.6')
    else: 
        print('only 1st order analysis')
    