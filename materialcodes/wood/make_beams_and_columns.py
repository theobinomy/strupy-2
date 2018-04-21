# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 18:18:13 2018

@author: stmwr
"""

from materialcodes.wood.wooddataparser import WoodSpecies, ur, spec_select
from materialcodes.wood.sawn_lumber_adjustments import Sawnlumberdimensions, SawnLumberMemberAdjustment
import materialcodes.wood.beamdesign


class WoodBeam(WoodSpecies, Sawnlumberdimensions):
    def __init__(self, name, size, length=10):
        WoodSpecies.__init__(self, name)
        Sawnlumberdimensions.__init__(self, size)
        self.length = length
        self.moisture_content = 0.19
    @property
    def selfweight(self):
        density  = 62.4*(ur.lb/ur.ft**3) * (self.Sp_grav / (1 + self.Sp_grav * self.moisture_content)) * ((1 + self.moisture_content / 100)) #todo replace 0.19 w/ moister ocntent
        density = round(density,2)
        return density


class WoodBeamAnalysis(WoodBeam, materialcodes.wood.beamdesign.simplebeamuniformload,  SawnLumberMemberAdjustment):
    def __init__(self, name:str, size:str, w_, length=10):
        WoodBeam.__init__(self, name, size, length)
        materialcodes.wood.beamdesign.simplebeamuniformload.__init__(self, w_, length, self.E, self.mom_x)
        SawnLumberMemberAdjustment.__init__(self)
        self.failed = False
        self.failed_commentary = []
        pass

    def __repr__(self):
        return f'WoodBeamAnalysis method'
    def __str__(self):
        return 'analysis method for wood beam'

    def Flexure_dcr(self):
        f_b = self.M_applied / self.s_x
        #f_b.ito_base_units()
        #print('f_b dimensoinality is:', f_b.dimensionality)
        #assert f_b.dimensionality == '[mass] / [length] ** 2'
        print('f_b is:', f_b)
        f_b_prime = self.getAdjustedBendingDesignValue(f_b)
        mdcr = f_b_prime / self.F_b
        mdcr.ito_base_units()
        self.dcr_m = mdcr
        if mdcr.magnitude > 1.0:
            self.failed = True
            self.failed_commentary.append('failed in moment')
        return mdcr

    def Beam_Stability(self):
        Cl = 1
        l_e = 1
        R_b = ((l_e * self.d)/(self.b**2))
        if R_b.magnitude > 50:
            self.failed = True
            self.failed_commentary.append('failed in stability')
        return R_b

    def Shear_dcr(self):
        f_v = (3 * self.v_applied) / (2 * self.b * self.d)
        print(f_v)
        f_v_prime = self.GetAdjustedShearDesignValue(f_v)
        print(f_v_prime)
        vdcr = f_v_prime  / self.F_v
        self.dcr_v = vdcr
        if vdcr.magnitude > 1:
            self.failed = True
            self.failed_commentary.append('failed in shear')
        return vdcr

    def Deflection(self):
        delta_t = self.delta
        print('delta_t is:', delta_t)
        delta_t.ito('inch')
        print('delta_t is:', delta_t)
        def_ratio = (self.length /delta_t)
        def_ratio.ito_root_units()
        print('deflection ratio is:', def_ratio)
        if def_ratio < 360:
            self.failed = True
            self.failed_commentary.append('failed in deflectoin')
        return delta_t

    def Combined_dcr(self):
        combined_dcr = self.Shear_dcr() + self.Flexure_dcr()
        self.dcr_combined = combined_dcr
        if combined_dcr.magnitude > 1:
            self.failed = True
            self.failed_commentary.append('combined failed')
        return combined_dcr

class Wood_Column_Analysis(WoodBeam, SawnLumberMemberAdjustment):
    adjustments_factors = SawnLumberMemberAdjustment()
    def __init__(self, name, size, length, Axial_load):
        WoodBeam.__init__(self, name, size, length)
        SawnLumberMemberAdjustment.__init__(self)
        #adjustments2 = SawnLumberMemberAdjustment()
        self.axial_load = Axial_load
        self.el_e = 24 * ur.inch

    def __repr__(self):
        return f'WoodColumnAnalysis method'
    def __str__(self):
        return 'analysis method for wood column'

    def Axial_DCR(self):
        f_c = self.F_c_par
        f_c_prime = self.adjustments_factors.GetAdjustedCompressionDesignValue(f_c)
        cdcr = self.axial_load/ (f_c_prime*self.area)
        if cdcr.magnitude > 1:
            self.failed = True
        return cdcr

    def Column_stability(self):
        FcE = (0.822 * self.E_min) / ((self.el_e / self.d) ** 2)
        c = 0.8  #consevative from NDS 3.7.1.5
        a = ((1 + (FcE / self.F_c_par)) / (2 * c))
        b = (FcE / Fc) / c
        Cp = a * (a ** 2 * b) ** .5
        print(Cp)



if __name__ == "__main__":
    twood = 'RED OAK NO.1 2 IN. & WIDER'
    #twood = spec_select()
    size = '4x6'
    baz = WoodBeamAnalysis(twood, size, 3*(ur.lbf/ur.inch), 72*ur.inch)
    print(
        baz.Flexure_dcr(),
        baz.Deflection(),
        baz.Beam_Stability(),
        baz.Shear_dcr(),
        baz.Combined_dcr()
    )
    print(baz.failed)
    bar = Wood_Column_Analysis(twood, '4x4', 10*ur.foot, 4500*ur.lb)
    tbone = bar.Axial_DCR()
    pass
