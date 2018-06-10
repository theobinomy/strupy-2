'''this file will do the heavy lififting for design of beams'''

#from .make_beams_and_columns import spec_select



beamtypes = 'cantilevered, pin-pin, pin-fix, fix-fix'
beamconditions = 'simplespan, multispan'

class simplebeamuniformload():
    def __init__(self, w, l, E, I):
        R = w * l
        M = (w*(l**2))/8
        #assert M.dimensionality == '[mass]*[length]'
        delta = (5*w*(l**4)) / (384 * E * I)
        assert delta.dimensionality == '[length]'
        self.v_applied = R
        self.M_applied = M
        self.delta = delta


def simplebeamuniformload_partiallydis_mid(w, l, a, b, c):
    x = l
    R1 = (w*b)*(2*c + b) / (2*l)
    R2 = (w*b)*(2*a + b) / (2 * l)
    #V at midpoint not yet calculated
    M = R1
    delta = (5*w*l**4) / (384 * 1000 * 10000)
    return R1, R2, M, delta

def simplebeamuniformload_partiallydis_oneend(w,l,a):
    x = l*.333
    R1 = (w*a)*(2*l - a) / (2*l)
    R2 = (w*a**2)/(2 * l)
    #V at midpoint not yet calculated
    Vx = R1 - w*x
    if x == R1/w:
        M = R1**2 /2*w
    if x < a:
        M = R1*x - w*x**2 / 2
        delta = (w*x) / (24*E*I*l)*(a**2*(2*l-a)**2
                            -2*a*x**2*(2*l-a)+l*x**3)

    if x > a:
        M = R2 ( l - x)
        delta = (w*a**2*(l-x)/ (24*E*I*l))*(4*x*l - 2*x**2 - a**2)

    return R1, R2, M, delta

def uniformloadpartiallydistributedeachend(a,b,c,w1, w2,l):
    x = l
    R1 = w1*a*(2*l-a)+w2*c**2 / (2*l)
    R2 = w2*c*(2*l-c)+w2*a**2 / (2*l)
    if R1 < w1*a:
        Mmax = R1**2 / 2*w1
    else:
        Mmax = R2 ** 2 / 2 * w2
    M = Mmax
    delta = 10
    return R1, R2, M, delta

