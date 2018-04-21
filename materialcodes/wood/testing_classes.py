# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 09:42:16 2018

@author: stmwr
"""

from wooddataparser import pass_wood

class size(object):
    def __init__(self, size = '2x4'):       
        super(A, self).__init__()
        r1 = size.split('x')
        ind = 0
        for i in r1:
            i = int(i)
            if i < 8:
                i = i - .5
                print(i)
            elif i >= 8:
                i = i - .75
                print(i)
            r1[ind] = i
            ind += 1                
        self.b = r1[0]
        self.d = r1[1]
   
class species(object):    
    woods = pass_wood()        
    ''' this object is the wood object information)'''
    def __init__(self, name): #,e, fb, fc_par, fc_perp, ft, fv, grade, name, size, species):
        super(B, self).__init__()
        self.e =       woods[name]['E']
        self.e_min =   woods[name]['EMIN']
        self.fb =      woods[name]['FB'] 
        
class beam(size,species):
    def __init__(self, size, name, length=10):
        super(C, self).__init__(size, name)
        self.length = length
        pass

w_name = 'ALASKA SPRUCE NO.3 2 IN. & WIDER'
size = '2x4'
beam = beam(w_name, size)