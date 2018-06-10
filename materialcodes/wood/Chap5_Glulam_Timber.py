from materialcodes.wood.Chap3_Design_Provisions import WoodBeamAnalysis
from materialcodes.wood.WoodSizer import SawnLumberDimensions
from materialcodes.wood.wooddataparser import WoodSpecies, ur

def GlulamBeamSize(size):


    class GlulamMemberAdjustment():
        def __init__(self):
            self._C_D  =  1 or {'perm':.9,'teny':1,'twom':1.15,'sevd':1.25,'tenm':1.6,'imp':2}
            self._C_M  =  {F_b:.85, F_t:1, F_v:0.97, F_cp:.67, F_c : .8, E:.9, E_min:.9}
            self._C_t  =  1
            self._C_L  =  1
            self._C_V  =  1
            self._C_fu =  1
            self._C_c  =  1
            self._C_I  =  1
            self._C_vr =  1
            self._C_P  =  1
            self._C_b  =  1
            self._lambda_ = 1

        def GetAdjustedBendingDesignValue(self, f_b):
            K_f = 2.54  # Table 4.3.1
            phi = 0.85  # Table 4.3.1
            F_b_prime = f_b * self._C_D * self._C_M * self._C_t * self._C_L * self._C_V * self._C_fu * \
                        self._C_c * self._C_I * K_f * phi * self._lambda_
            return F_b_prime

        def GetAdjustedTensionValue(self, f_t):
            phi = 0.8  # Table 4.3.1
            K_f = 2.7  # Table 4.3.1
            F_t_prime = f_t * self._C_M * self._C_t * K_f * phi * self._lambda_
            return F_t_prime

        def GetAdjustedShearDesignValue(self, f_v):
            phi = 0.75
            K_f = 2.88
            F_v_prime = f_v * self._C_M * self._C_t * self._C_vr * K_f * phi * self._lambda_
            return F_v_prime

        def GetAdjustedRadialTensionValue(self, f_rt):
            phi = 0.75
            K_f = 2.88
            F_rt_prime = f_rt * self._C_M * self._C_t * K_f * phi * self._lambda_
            return F_rt_prime

        def GetAdjustedCompressionDesignValue(self, f_c):
            phi = 0.9  # Table 4.3.1
            K_f = 2.4  # Table 4.3.1
            F_c_prime = f_c * self._C_M * self._C_t * self._C_b * K_f * phi * self._lambda_
            return F_c_prime

        def GetAdjustedCompressionParallelDesignValue(self, f_cp):
            phi = 0.9  # Table 5.3.1
            K_f = 1.67  # Table 5.3.1
            F_cp_prime = f_cp * self._C_M * self._C_t * K_f * phi
            return F_cp_prime

        def GetAdjustedModulusOfElasticity(self, E):
            E_prime = E * self._C_M * self._C_t  # Table 4.3.1
            return E_prime

        def GetAdjustedMinimumModulusOfElasticityForStability(self, E_min):
            K_f = 1.76
            phi = 0.85
            E_min_prime = E_min * self._C_M * self._C_t * K_f * phi  # from Table 4.3.1
            return E_min_prime