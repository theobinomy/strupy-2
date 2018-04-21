# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 10:38:58 2018

@author: stmwr
"""

class wood_column(wood_species):
    def __init_(self, Emin = 1, CM = 1, Ct = 1, CT = 1, Ci = 1, Cr=1 ):
        super(wood_column,self).__init__()
        self.CM=  CM
        self.Ct=  Ct
        self.CT=  CT
        self.Ci=  Ci
        self.Cr=  Cr
    def  GetAdjustedMinModulusOfElasticity():
        EminPrime = self.Emin * self.CM * self.Ct * self.Ci * self.CT        
        return EminPrime


