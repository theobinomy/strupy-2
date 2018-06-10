# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 18:20:24 2018

@author: stmwr
"""


class RoundTimberMemberAdjustment():
    #todo QC Kf and Phi values
    #todo update C_ equatoins
    def __init__(self):
        self._C_D  = 1
        self._C_t  = 1
        self._C_ct = 1
        self._C_F  = 1
        self._C_P  = 1
        self._C_cs = 1
        self._C_b  = 1
        self._C_ls = 1
        self._lambda_ = 1

    def GetAdjustedCompressionDesignValue(self, f_c):
        phi = 0.9  # Table 4.3.1
        K_f = 2.4  # Table 4.3.1
        F_c_prime = f_c * self._C_t * self._C_P * self._C_cs * self._C_ls * K_f * phi * self._lambda_
        return F_c_prime

    def GetAdjustedBendingDesignValue(self, f_b):
        K_f = 2.88  # Table 4.3.1
        phi = 0.75  # Table 4.3.1
        F_b_prime = f_b * self._C_t * self._C_ct * self._C_F * self._C_ls * K_f * phi * self._lambda_
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
        F_v_prime = f_v * self._C_t * self._C_ct * K_f * phi * self._lambda_
        return F_v_prime

    def GetAdjustedCompressionParallelDesignValue(self, f_cp):
        phi = 0.9  # Table 5.3.1
        K_f = 1.67  # Table 5.3.1
        F_cp_prime = f_cp * self._C_t * self._C_ct * self._C_b * K_f * phi
        return F_cp_prime

    def GetAdjustedModulusOfElasticity(self, E):
        E_prime = E * self._C_t  # Table 4.3.1
        return E_prime

    def GetAdjustedMinimumModulusOfElasticityForStability(self, E_min):
        K_f = 1.76
        phi = 0.85
        E_min_prime = E_min * self._C_t * K_f * phi  # from Table 4.3.1
        return E_min_prime

class IJoistAdjustment():
    pass

class StructuralCompositeAdjustment():
    pass

class StructuralPanelAdjustment():
    pass

class CrossLaminatedAdjustment():
    pass

class Adjustments(object):
    def __init__(self):
        self.SawnLumber1 = SawnLumberMemberAdjustment()

    SawnLumber = SawnLumberMemberAdjustment()
    GlulamMember = GlulamMemberAdjustment()
    RoundTimberMember = RoundTimberMemberAdjustment()
    IJoist = IJoistAdjustment()  # todo implement
    StructuralComposite  = StructuralCompositeAdjustment()  # todo implement
    StructuralPanel = StructuralPanelAdjustment()  # todo implement
    CrossLaminated = CrossLaminatedAdjustment()  # todo implement


# def test():
#     def ltest(name,val):
#         #print(name , val, -0.02 < (name -val)/name <0.02  )
#         return -0.02 < (name -val)/name <0.02
#
#     zz = Sawnlumberdimensions('3x6')
#     assert ltest(zz.area, 13.75)
#     assert ltest(zz.s_x, 12.60)
#     assert ltest(zz.mom_x, 34.66)
#     assert ltest(zz.s_y, 5.729)
#     assert ltest(zz.mom_y, 7.161)
#     assert ltest(zz.r_x, zz.d / (12**.5))
#     assert ltest(zz.r_y, zz.b / (12**.5))
#
#     z1 = Sawnlumberdimensions('4x16')
#     assert ltest(z1.area, 53.38)
#     assert ltest(z1.s_x, 135.66)
#     assert ltest(z1.mom_x, 1034)
#     assert ltest(z1.s_y, 31.14)
#     assert ltest(z1.mom_y, 54.49)
#     assert ltest(z1.r_x, z1.d / (12**.5))
#     assert ltest(z1.r_y, z1.b / (12**.5))
#     print('passed tests')
#     pass
    
if __name__ == '__main__':
    #zz = Sawnlumberdimensions('3x16')
    #test()
    zz = Adjustments.SawnLumber.GetAdjustedShearDesignValue(3)
    pass