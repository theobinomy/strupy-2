# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 18:20:24 2018

@author: stmwr
"""
from materialcodes.wood.wooddataparser import ur

class SawnLumberMemberAdjustment():
    def __init__(self):
        self.C_M_E =   1
        self.C_M_Fb =  1
        self.C_t_Fb =  1
        self.C_L =     1
        self.C_F_Fb =  1
        self.C_fu_Fb = 1
        self.C_i_Fb =  1
        self.C_r =     1
        self.lambd =   1
        self.C_M_Fc =  1
        self.C_t_Fc =  1
        self.C_F_Fc =  1
        self.C_i_Fc=   1
        self.C_P =     1
        self.C_M_Fv =  1
        self.C_t_Fv =  1
        self.C_i_Fv =  1
    
    def getAdjustedBendingDesignValue(self, f_b):
        phi = 0.85 #Table 4.3.1
        K_f = 2.54 #Table 4.3.1
        F_b_prime = phi * K_f * f_b *  self.lambd * self.C_M_Fb * \
                    self.C_t_Fb * self.C_L * self.C_F_Fb * self.C_fu_Fb *\
                    self.C_i_Fb * self.C_r
        return F_b_prime
        
    def GetAdjustedCompressionDesignValue(self, f_c):
        phi = 0.9 #Table 4.3.1
        K_f = 2.4 #Table 4.3.1
        F_c_prime = phi * K_f * f_c * self.lambd * \
                    self.C_M_Fc * self.C_t_Fc * self.C_F_Fc * \
                    self.C_i_Fc * self.C_P
        return F_c_prime

    def GetAdjustedShearDesignValue(self, f_v):
        phi = 0.75
        K_f = 2.88
        F_v_prime = phi * K_f * f_v * self.lambd * \
                    self.C_M_Fv * self.C_t_Fv * self.C_i_Fv
        return F_v_prime
        
    def GetAdjustedTensionValue(self):
        phi = 0.8 #Table 4.3.1
        K_f = 2.7 #Table 4.3.1
        F_t_prime = phi * K_f *self.F_t *  self.lambd * self.C_M_Ft * self.C_t_Ft * self.C_F_Ft * self.C_i_Ft
        return F_t_prime
    
    def GetAdjustedModulusOfElasticity(self):
        E_prime = E * self.C_M * self.C_t_E * self.C_i #Table 4.3.1
        return E_prime
        
    def GetAdjustedMinimumModulusOfElasticityForStability(self):
        K_F = 1.76
        phi = 0.85
        E_min_prime = self.E_min * self.C_M_E * self.C_t_E * self.C_i_E * self.C_T * K_F * phi #from Table 4.3.1
        return E_min_prime

class Sawnlumberdimensions():
    def __init__(self, size = '2x4'):       
        #super(sawnlumberdimensions, self).__init__(size)
        r1 = size.split('x')
        ind = 0
        for i in r1:
            i = int(i)
            if i < 8:
                i = i - .5
                #print(i)
            elif i >= 8:
                i = i - .75
                #print(i)
            r1[ind] = i
            ind += 1                

        self.b = r1[0] * ur.inch
        self.d = r1[1] * ur.inch
    
    @property
    def area(self):
        area = self.d * self.b
        assert area.dimensionality == '[length]**2'
        return area
    
    @property
    def mom_x(self):
        return (self.b * self.d**3)/12
    
    @property
    def mom_y(self):
        return (self.b**3 * self.d)/12
    
    @property
    def r_x(self):
        return (self.d)/(12**.5)
    
    @property
    def r_y(self):
        return (self.b)/(12**.5)
    
    @property
    def s_x(self):
        return (self.b * self.d**2)/(6)
    
    @property
    def s_y(self):
        return (self.b**2 * self.d)/(6)

    def __repr__(self):
        return f'sawlumberdimensions({size})'
   
def test():
    def ltest(name,val):
        #print(name , val, -0.02 < (name -val)/name <0.02  )
        return -0.02 < (name -val)/name <0.02 
    
    zz = Sawnlumberdimensions('3x6')
    assert ltest(zz.area, 13.75)
    assert ltest(zz.s_x, 12.60)
    assert ltest(zz.mom_x, 34.66)
    assert ltest(zz.s_y, 5.729)
    assert ltest(zz.mom_y, 7.161)
    assert ltest(zz.r_x, zz.d / (12**.5))
    assert ltest(zz.r_y, zz.b / (12**.5))    
    
    z1 = Sawnlumberdimensions('4x16')
    assert ltest(z1.area, 53.38)
    assert ltest(z1.s_x, 135.66)
    assert ltest(z1.mom_x, 1034)
    assert ltest(z1.s_y, 31.14)
    assert ltest(z1.mom_y, 54.49)
    assert ltest(z1.r_x, z1.d / (12**.5))
    assert ltest(z1.r_y, z1.b / (12**.5))    
    print('passed tests')
    pass
    
if __name__ == '__main__':
    #zz = Sawnlumberdimensions('3x16')
    test()