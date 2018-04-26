# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 18:20:24 2018

@author: stmwr
"""
from materialcodes.wood.wooddataparser import ur

class SawnLumberMemberAdjustment():
    def __init__(self):
        self.C_D =  1
        self.C_M =  1
        self.C_t =  1
        self.C_L =  1
        self.C_F =  1
        self.C_fu=  1
        self.C_i =  1
        self.C_r =  1
        self.C_P =  1
        self.C_T =  1
        self.C_b =  1
        self.lambda_ =  1

    def getAdjustedBendingDesignValue(self, f_b):
        K_f = 2.54  # Table 4.3.1
        phi = 0.85 #Table 4.3.1
        F_b_prime = f_b * self.C_M * self.C_t * self.C_L * \
                    self.C_F * self.C_fu * self.C_i * self.C_r * K_f * phi * self.lambda_
        return F_b_prime
        
    def GetAdjustedTensionValue(self, f_t):
        phi = 0.8 #Table 4.3.1
        K_f = 2.7 #Table 4.3.1
        F_t_prime = f_t * self.C_M * self.C_t * self.C_F * self.C_i * K_f * phi * self.lambda_
        return F_t_prime

    def GetAdjustedCompressionDesignValue(self, f_c):
        phi = 0.9 #Table 4.3.1
        K_f = 2.4 #Table 4.3.1
        F_c_prime = f_c * self.C_M * self.C_t * self.C_F * \
                    self.C_i * self.C_P * K_f * phi * self.lambda_
        return F_c_prime

    def GetAdjustedShearDesignValue(self, f_v):
        phi = 0.75
        K_f = 2.88
        F_v_prime = f_v * self.C_M * self.C_t * self.C_i * K_f * phi * self.lambda_
        return F_v_prime

    def GetAdjustedModulusOfElasticity(self, E):
        E_prime = E * self.C_M * self.C_t * self.C_i #Table 4.3.1
        return E_prime
        
    def GetAdjustedMinimumModulusOfElasticityForStability(self, E_min):
        K_F = 1.76
        phi = 0.85
        E_min_prime = E_min * self.C_M * self.C_t * self.C_i * self.C_T * K_F * phi #from Table 4.3.1
        return E_min_prime

class GlulamMemberAdjustment():
    def __init__(self):
        self.C_D  =  1
        self.C_M  =  1
        self.C_t  =  1
        self.C_L  =  1
        self.C_V  =  1
        self.C_fu =  1
        self.C_c  =  1
        self.C_I  =  1
        self.C_vr =  1
        self.C_P  =  1
        self.C_b  =  1
        self.lambda_ = 1

    def getAdjustedBendingDesignValue(self, f_b):
        K_f = 2.54  # Table 4.3.1
        phi = 0.85  # Table 4.3.1
        F_b_prime = f_b * self.C_D * self.C_M * self.C_t * self.C_L * self.C_V * self.C_fu * \
                    self.C_c * self.C_I * K_f * phi * self.lambda_
        return F_b_prime

    def GetAdjustedTensionValue(self, f_t):
        phi = 0.8  # Table 4.3.1
        K_f = 2.7  # Table 4.3.1
        F_t_prime = f_t * self.C_M * self.C_t * K_f * phi * self.lambda_
        return F_t_prime

    def GetAdjustedShearDesignValue(self, f_v):
        phi = 0.75
        K_f = 2.88
        F_v_prime = f_v * self.C_M * self.C_t * self.C_vr * K_f * phi * self.lambda_
        return F_v_prime

    def GetAdjustedRadialTensionValue(self, f_rt):
        phi = 0.75
        K_f = 2.88
        F_rt_prime = f_rt * self.C_M * self.C_t * K_f * phi * self.lambda_
        return F_rt_prime

    def GetAdjustedCompressionDesignValue(self, f_c):
        phi = 0.9  # Table 4.3.1
        K_f = 2.4  # Table 4.3.1
        F_c_prime = f_c * self.C_M * self.C_t * self.C_b * K_f * phi * self.lambda_
        return F_c_prime

    def GetAdjustedCompressionParallelDesignValue(self, f_cp):
        phi = 0.9  # Table 5.3.1
        K_f = 1.67  # Table 5.3.1
        F_cp_prime = f_cp * self.C_M * self.C_t * K_f * phi
        return F_cp_prime

    def GetAdjustedModulusOfElasticity(self, E):
        E_prime = E * self.C_M * self.C_t  # Table 4.3.1
        return E_prime

    def GetAdjustedMinimumModulusOfElasticityForStability(self, E_min):
        K_f = 1.76
        phi = 0.85
        E_min_prime = E_min * self.C_M * self.C_t * K_f * phi  # from Table 4.3.1
        return E_min_prime


class RoundTimberMemberAdjustment():
    #todo QC Kf and Phi values
    #todo update C_ equatoins
    def __init__(self):
        self.C_D  = 1
        self.C_t  = 1
        self.C_ct = 1
        self.C_F  = 1
        self.C_P  = 1
        self.C_cs = 1
        self.C_b  = 1
        self.C_ls = 1
        self.lambda_ = 1

    def GetAdjustedCompressionDesignValue(self, f_c):
        phi = 0.9  # Table 4.3.1
        K_f = 2.4  # Table 4.3.1
        F_c_prime = f_c * self.C_t * self.C_P * self.C_cs * self.C_ls * K_f * phi * self.lambda_
        return F_c_prime

    def getAdjustedBendingDesignValue(self, f_b):
        K_f = 2.88  # Table 4.3.1
        phi = 0.75  # Table 4.3.1
        F_b_prime = f_b * self.C_t * self.C_ct * self.C_F * self.C_ls * K_f * phi * self.lambda_
        return F_b_prime
    #
    # def GetAdjustedTensionValue(self, f_t):
    #     phi = 0.8  # Table 4.3.1
    #     K_f = 2.7  # Table 4.3.1
    #     F_t_prime = f_t * self.C_t * self.C_t * K_f * phi * self.lambda_
    #     return F_t_prime

    def GetAdjustedShearDesignValue(self, f_v):
        phi = 0.75
        K_f = 2.88
        F_v_prime = f_v * self.C_t * self.C_ct * K_f * phi * self.lambda_
        return F_v_prime

    def GetAdjustedCompressionParallelDesignValue(self, f_cp):
        phi = 0.9  # Table 5.3.1
        K_f = 1.67  # Table 5.3.1
        F_cp_prime = f_cp * self.C_t * self.C_ct * self.C_b * K_f * phi
        return F_cp_prime

    def GetAdjustedModulusOfElasticity(self, E):
        E_prime = E * self.C_t  # Table 4.3.1
        return E_prime

    def GetAdjustedMinimumModulusOfElasticityForStability(self, E_min):
        K_f = 1.76
        phi = 0.85
        E_min_prime = E_min * self.C_t * K_f * phi  # from Table 4.3.1
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