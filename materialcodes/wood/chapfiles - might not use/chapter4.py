#NDS chapter 1

"""
Created on Fri Mar 30 18:20:24 2018

@author: stmwr
"""
class SawnLumber():
    

class SawnLumberMemberAdjustment():
    def __init__(self):
        self.F_b = 1
        self.C_M_Fb = 1
        self.C_t_Fb = 1
        self.C_L =1
        self.C_F_Fb = 1
        self.C_fu_Fb = 1
        self.C_i_Fb = 1
        self.C_r = 1
        self.lambd = 12
    
    def getAdjustedBendingDesignValue(F_b, C_M_Fb, C_t_Fb, \
                                      C_L, C_F_Fb, C_fu_Fb, \
                                      C_i_Fb, C_r, lambd):
        phi = 0.85 #; //Table 4.3.1
        K_f = 2.54 #; //Table 4.3.1
        F_b_prime = self.F_b * phi * K_f * self.lambd * self.C_M_Fb * \
                    self.C_t_Fb * self.C_L * self.C_F_Fb * self.C_fu_Fb *\
                    self.C_i_Fb * self.C_r
        return F_b_prime
        
    def GetAdjustedCompressionDesignValue( F_c, C_M_Fc, C_t_Fc, C_F_Fc, C_i_Fc, C_P, lambd):
        phi = 0.9 #; //Table 4.3.1
        K_f = 2.4 #; //Table 4.3.1
        F_c_prime = F_c*phi * K_f * lambd * C_M_Fc * C_t_Fc *  C_F_Fc * C_i_Fc * C_P
        return F_c_prime

    def GetAdjustedShearDesignValue( F_v, C_M_Fv, C_t_Fv, C_i_Fv, lambd):
        phi = 0.75 #; //Table 4.3.1
        K_f = 2.88 #; //Table 4.3.1
        F_v_prime = F_c * phi * K_f * lambd * C_M_Fv * C_t_Fv *  C_i_Fv
        return F_v_prime
        
    def GetAdjustedTensionValue( F_t, C_M_Ft, C_t_Ft, C_F_Ft, C_i_Ft, lambd):
        phi = 0.8 #; //Table 4.3.1
        K_f = 2.7 #; //Table 4.3.1
        F_t_prime = F_t * phi * K_f * lambd * C_M_Ft * C_t_Ft * C_F_Ft * C_i_Ft
        return F_t_prime
    
    def GetAdjustedModulusOfElasticity( E, C_M, C_t_E, C_i):
        E_prime = E * C_M * C_t_E * C_i #;  //from Table 4.3.1
        return E_prime
        
    def GetAdjustedMinimumModulusOfElasticityForStability( E_min, C_M_E, C_t_E, C_i_E, C_T):
        K_F = 1.76;
        phi = 0.85;
        E_min_prime = E_min * C_M_E * C_t_E * C_i_E * C_T * K_F * phi #; //from Table 4.3.1
        return E_min_prime;
        