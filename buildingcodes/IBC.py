#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  3 20:00:50 2017

@author: sean
"""
"""BC – Structural
Code Development Committee [BS]: Chapters \
15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
Appendices F, G, H, I, J, L, M"""

import buildingcodes.asce710

'''
class Chap15:
    \'''ROOF ASSEMBLIES AND ROOFTOP STRUCTURES\'''
    pass
'''

class Chap16:
    ''' STRUCTURAL DESIGN '''
    #note I'm not sure what i'm going here so much.
    IsConventionalLightFrame = True
    
    def loadfactor(self):
        return asce710.loadfactors()
    
    
    
    def contractdocs(self):
        print(f'floor loads are {asce710.floorloads()}')
        print(f'ground snow loads are {asce710.snowloads()}')
        print(f'wind speed is {asce710.wind()}')
    #ref = contractdocs()
    pass #Finish Line 76
'''
class Chap17:
    '''  '''
    pass
 
class Chap18:
    '''  '''
    pass
 
class Chap19:
    '''  '''
    pass
 
class Chap20:
    '''  '''
    pass
 
class Chap21:
    '''  '''
    pass
    

class Chap22:
    '''  '''
    pass
 
class Chap23:
    '''  '''
    pass
 
class Chap24:
    '''  '''
    pass
 
class Chap25:
    '''  '''
    pass
 
class Appx_f:
    '''  '''
    pass
 
 
class Appx_g:
    '''  '''
    pass
 
 
class Appx_h:
    '''  '''
    pass
 
 
class Appx_i:
    '''  '''
    pass
 
 
class Appx_j:
    '''  '''
    pass
 
 
class Appx_l:
    '''  '''
    pass
 
 
class Appx_m:
    '''  '''
    pass
    
'''
 
    
    
    
class label():
    def __init__(self):
        print('this is the IBC code book')
        
        


print('IBC here and good')
def tests():
    c16 = Chap16()
    c16.contractdocs()
    pass
if __name__ == '__main__':
    tests()