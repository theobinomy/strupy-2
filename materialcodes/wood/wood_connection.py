from math import sin, cos
import pint
u = pint.UnitRegistry()


class WoodConnection:
    def __init__(self):
        # self.Woodconnection = WoodConnection
        self.diameter = .25 * u.inch
        self.dowel_bearing_length = 1
        self.fastener_yield = 36000
        self.specific_gravity = .5
        self.angle_of_load = 30
        self.is_small = False

    def haskins_formula(self, angle_grain, angle_of_load, specific_gravity=None, diameter=None):
        Fep = specific_gravity * 112000
        Fel = 6100*specific_gravity**1.45*diameter*-.5
        Felp = (Fep * Fel) / (Fep * sin(angle_of_load)**2 + Fel * cos(angle_of_load)**2)
        return Felp
    def small_dowel(self, specific_gravity=None, diameter=None):
        print(16600*specific_gravity**1.84)
        return 16600*specific_gravity**1.84
class Nails: #specg =.5, fload = 1000):
    def __init__(self, specg = None, load = None):
        self.specg = specg
        self.load = load

    def capacity(self, specg, load):
        return specg * load

class Bolts:
    pass

class LagBolt:
    pass

class ShearPlate:
    pass

class WoodScrew:
    pass

class MetalPlate:
    pass

class Rivet:
    pass

class DriftBolt:
    pass

class SpikeGrid:
    pass

def test():
    test = WoodConnection()
    test.small_dowel(specific_gravity=.5, diameter=.25)


if __name__ == '__main__':
    test()