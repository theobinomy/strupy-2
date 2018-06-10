from materialcodes.wood.Chap3_Design_Provisions import WoodBeamAnalysis
from materialcodes.wood.WoodSizer import SawnLumberDimensions
from materialcodes.wood.wooddataparser import WoodSpecies, ur


class SawnLumberMemberAdjustment():
    def __init__(self):
        self._C_D = 1
        self._C_M = 1
        self._C_t = 1
        self._C_L = 1
        self._C_F = 1
        self._C_fu = 1
        self._C_i = 1
        self._C_r = 0
        self._C_P = 1
        self._C_T = 1
        self._C_b = 1
        self._lambda_ = 1

    def GetAdjustedBendingDesignValue(self, F_b):
        def ASD(self):
            #duration factor
            if not self.LRFD:
                C_d = 1  #todo implement this cD = {'perm':.9,'teny':1,'twom':1.15,'sevd':1.25,'tenm':1.6,'imp':2}
            else:
                C_d = 1
            return C_d

        def C_M(self):
            if self._C_M == 1:
                C_M = 1
            else:
                C_M = 0.85
            return C_M

        def C_t(self):
            #tempurature factor
            if self._C_t <= 100:
                C_t = 1
            elif 100 < self._C_t <= 125:
                C_t = .9
            else:
                C_t = .8
            return C_t

        def C_L(self):
            #beam stability factor
            return 1  # todo implement full beam stability facot calculatoins

        def C_F(self):
            # Beam size factor
            if self.b.magnitude > 4:
                return min((12/(self.b.magnitude)**(1/9), 1))
            w = str(int(self.d.magnitude + .5))

            t = str(int(self.b.magnitude + .5))

            C_F_vals = {
                'Stud': {
                    # 'width': {
                    '2': {'2': 1.1, '3': 1.1, '4': 1.1},
                    '3': {'2': 1.1, '3': 1.1, '4': 1.1},
                    '4': {'2': 1.1, '3': 1.1, '4': 1.1},
                    '5': {'2': 1.0, '3': 1.0, '4': 1.0},
                    '6': {'2': 1.0, '3': 1.0, '4': 1.0},
                    '8': {'2': 1.2, '3': 1.2, '4': 1.3},
                    '10': {'2': 1.1, '3': 1.1, '4': 1.2},
                    '12': {'2': 1.0, '3': 1.0, '4': 1.1},
                    '14': {'2': 0.9, '3': 0.9, '4': 1.0},
                    # }
                },
                'Construction': {
                    # 'width': {
                    '2': {'2': 1.0, '3': 1.0, '4': 1.0},
                    '3': {'2': 1.0, '3': 1.0, '4': 1.0},
                    '4': {'2': 1.0, '3': 1.0, '4': 1.0},
                    # }
                },
                'Utility': {
                    # 'width': {
                    '2': {'2': .4, '3': .4, '4': 999},
                    '3': {'2': .4, '3': .4, '4': 999},
                    '4': {'2': 1.0, '3': 1.0, '4': 1.0},
                    # }
                },
                'Other': {
                    # 'width': {
                    '2': {'2': 1.5, '3': 1.5, '4': 1.5},
                    '3': {'2': 1.5, '3': 1.5, '4': 1.5},
                    '4': {'2': 1.5, '3': 1.5, '4': 1.5},
                    '5': {'2': 1.4, '3': 1.4, '4': 1.4},
                    '6': {'2': 1.3, '3': 1.3, '4': 1.3},
                    '8': {'2': 1.2, '3': 1.2, '4': 1.3},
                    '10': {'2': 1.1, '3': 1.1, '4': 1.2},
                    '12': {'2': 1.0, '3': 1.0, '4': 1.1},
                    '14': {'2': 0.9, '3': 0.9, '4': 1.0},
                    # }
                },
            }


            if self.Grade in ["Stud","Utility"]:
                cfg = self.Grade
            elif self.Grade in ["Construction", "Standard"]:
                cfg = 'Construction'
            else:
                cfg = 'Other'

            return C_F_vals[cfg][w][t]

        def C_fu(self):
            return 1

        def C_i(self):
            #incising factor
            return 1 #todo implement this

        def C_r(self):
            #repetative factor
            if self._C_r == 0:
                C_r = 1
            else:
                C_r = 1.15
            return C_r

        def LRFD(self):
            def lamval(self):
                # todo factor this for load case information, etc,
                return 1
            if self.LRFD == True:
                K_f = 2.54  # Table 4.3.1
                phi = 0.85  # Table 4.3.1
                _lambda = lamval(self)
            else:
                K_f = 1
                phi = 1
                _lambda = 1
            #print(K_f, phi, _lambda)
            return K_f * phi * _lambda
        # print(f_b)
        # print(ASD(self))
        # print(C_M(self))
        # print(C_t(self), 'ct')
        # print(C_L(self), 'cl')
        # print(C_f(self), 'cf')
        # print(C_r(self), 'cr')
        # print(LRFD(self), 'lrfd')

        #print(f_b, ' fb mod is ',ASD(self) * C_M(self) * C_t(self) * C_L(self) * \
        #            C_F(self) * C_fu(self) * C_i(self) * C_r(self) * LRFD(self))
        F_b_prime = F_b * ASD(self) * C_M(self) * C_t(self) * C_L(self) * \
                    C_F(self) * C_fu(self) * C_i(self) * C_r(self) * LRFD(self)

        #print(C_M, C_t(self), C_L(self), C_f(self), self._C_fu, self._C_i, F_b_prime)
        #print('fb prime is',F_b_prime)
        self.F_b_prime = F_b_prime
        return F_b_prime

    def GetAdjustedTensionValue(self, f_t):
        def ASD(self):
            if not self.LRFD:
                C_d = 1
            else:
                C_d = 1
            return C_d

        def C_M(self):
            if self._C_M == 1:
                C_M = 1
            else:
                C_M = 1
            return C_M

        def C_t(self):
            #tempurature factor
            if self._C_t <= 100:
                C_t = 1
            elif 100 < self._C_t <= 125:
                C_t = .9
            else:
                C_t = .8
            return C_t

        def C_F(self):
            # Beam size factor
            if self.d.magnitude > 4:
                return 1

            w = str(int(self.d.magnitude + .5))

            t = str(int(self.b.magnitude + .5))

            C_F_vals = {
                'Stud': {
                    # 'width': {
                    '2': 1.1,
                    '3': 1.1,
                    '4': 1.1,
                    '5': 1.0,
                    '6': 1.0,
                    '8': 1.2,
                    '10': 1.1,
                    '12': 1.0,
                    '14': 0.9,
                    # }
                },
                'Construction': {
                    '2': 1.0,
                    '3': 1.0,
                    '4': 1.0,

                },
                'Utility': {
                    '2': 0.4,
                    '3': 0.4,
                    '4': 1.0,

                },
                'Other': {
                    '2': 1.5,
                    '3': 1.5,
                    '4': 1.5,
                    '5': 1.4,
                    '6': 1.3,
                    '8': 1.2,
                    '10': 1.1,
                    '12': 1.0,
                    '14': 0.9,

                },}



            if self.Grade in ["Stud","Utility"]:
                cfg = self.Grade
            elif self.Grade in ["Construction", "Standard"]:
                cfg = 'Construction'
            else:
                cfg = 'Other'
            return C_F_vals[cfg][w][t]

        def C_i(self):
            return 1

        def LRFD(self):
            def lamval(self):
                # todo factor this for load case information, etc,
                return 1
            if self.LRFD == True:
                K_f = 2.7  # Table 4.3.1
                phi = 0.8  # Table 4.3.1
                _lambda = lamval(self)
            else:
                K_f = 1
                phi = 1
                _lambda = 1
            #print(K_f, phi, _lambda)
            return K_f * phi * _lambda
        # print(f_b)
        # print(ASD(self))
        # print(C_M(self))
        # print(C_t(self), 'ct')
        # print(C_L(self), 'cl')
        # print(C_f(self), 'cf')
        # print(C_r(self), 'cr')
        # print(LRFD(self), 'lrfd')



        F_t_prime = f_t * ASD(self) * C_M(self) * C_t(self) *  \
                    C_F(self) *  C_i(self) *  LRFD(self)
        return F_t_prime

    def GetAdjustedShearDesignValue(self, f_v):
        def ASD(self):
            if not self.LRFD:
                C_d = 1
            else:
                C_d = 1
            return C_d

        def C_M(self):
            if self._C_M == 1:
                C_M = 1
            else:
                C_M = .85
            return C_M

        def C_t(self):
            # tempurature factor
            if self._C_t <= 100:
                C_t = 1
            elif 100 < self._C_t <= 125:
                C_t = .9
            else:
                C_t = .8
            return C_t


        def C_i(self):
            return 1

        def LRFD(self):
            def lamval(self):
                # todo factor this for load case information, etc,
                return 1

            if self.LRFD == True:
                K_f = 2.88  # Table 4.3.1
                phi = 0.75  # Table 4.3.1
                _lambda = lamval(self)
            else:
                K_f = 1
                phi = 1
                _lambda = 1
            #print(K_f, phi, _lambda)
            return K_f * phi * _lambda

        F_v_prime = f_v * ASD(self) * C_M(self) * C_t(self) *  \
                    C_i(self) *  LRFD(self)
        return F_v_prime

    def GetAdjustedCompressionDesignValuePar(self, f_c_par):
        phi = 0.9  # Table 4.3.1
        K_f = 2.4  # Table 4.3.1

        if self._C_M == 1:
            C_M = 1
        else:
            C_M = 0.85

        F_c_prime = f_c_par * C_M * self._C_t * self._C_F * \
                    self._C_i * self._C_P * K_f * phi * self._lambda_
        return F_c_prime

    def GetAdjustedCompressionDesignValue(self, f_c_perp):
        phi = 0.9  # Table 4.3.1
        K_f = 2.4  # Table 4.3.1

        if self._C_M == 1:
            C_M = 1
        else:
            C_M = 0.85

        F_c_prime = f_c_perp * C_M * self._C_t * self._C_F * \
                    self._C_i * self._C_P * K_f * phi * self._lambda_
        return F_c_prime

    def GetAdjustedModulusOfElasticity(self, E):
        if self._C_M == 1:
            C_M = 1
        else:
            C_M = 0.85

        E_prime = E * C_M * self._C_t * self._C_i  # Table 4.3.1
        return E_prime

    def GetAdjustedMinimumModulusOfElasticityForStability(self, E_min):
        K_F = 1.76
        phi = 0.85
        E_min_prime = E_min * C_M * self._C_t * self._C_i * self._C_T * K_F * phi  # from Table 4.3.1
        return E_min_prime


class WoodBeam(WoodSpecies, SawnLumberDimensions, WoodBeamAnalysis, SawnLumberMemberAdjustment):
    def __init__(self, name, size, w_, length=10):
        self.length = length
        self.moisture_content = 0.19
        self.iscolumn = False
        WoodSpecies.__init__(self, name)
        SawnLumberDimensions.__init__(self, size)
        SawnLumberMemberAdjustment.__init__(self)
        WoodBeamAnalysis.__init__(self, w_, length)

    @property
    def selfweight(self):
        density = 62.4 * (ur.lb / ur.ft ** 3) * (self.Sp_grav / (1 + self.Sp_grav * self.moisture_content)) * (
            (1 + self.moisture_content / 100))  # todo replace 0.19 w/ moister ocntent
        density = round(density, 2)
        return density

    def repetitive_checks(self):
        repete = input("is this repetative?: y/n >> ")
        if repete == 'y':
            self._C_r = 1

    def moist_checks(self):
        dry = input("is this dry?: y/n >> ")
        if dry == 'n':
            self._C_M = 0

    def flat_use(self):
        flat = input("is this laid flat?: y/n >> ")
        if flat == 'y':
            self._C_F = 0
            self.b, self.d = self.d, self.b
            self.s_x, self.s_y = self.s_y, self.s_x
            self.mom_x, self.mom_y = self.mom_y, self.mom_x
            self.r_x, self.r_y = self.r_y, self.r_x


if __name__ == "__main__":
    twood = 'RED OAK NO.1 2 IN. & WIDER'
    # twood = spec_select()
    size = '2x6'
    baz = WoodBeam(twood, size, 10 * (ur.lbf / ur.inch), 72 * ur.inch)
    baz.LRFD = False
    baz.repetitive_checks()
    #baz.GetAdjustedBendingDesignValue(825)
    baz.moist_checks()
    #baz.GetAdjustedBendingDesignValue(825)
    baz.flat_use()
    #baz.GetAdjustedBendingDesignValue(825)
    print(
        'flex ', baz.Flexure_dcr(),
        'defl ',baz.Deflection(),
        'stab ',baz.Beam_Stability(),
        'shear ',baz.Shear_dcr(),
        'comb ',baz.Combined_dcr()
    )
