#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 22:29:44 2017

@author: sean
"""


import steeldataparser
steelraw = steeldataparser.pass_steel()

def make_lower(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result = [str(value).lower() for value in result]
        result = [value.lower() for value in result]
        return result
    return wrapper

#section A
def typicalgrades():

'''
(1) Hot-rolled structural shapes
ASTM A36/A36M ASTM A709/A709M
ASTM A529/A529M ASTM A913/A913M
ASTM A572/A572M ASTM A992/ A992M
ASTM A588/A588M ASTM A1043/A1043M
(2) Structural tubing
ASTM A500 ASTM A618/A618M
ASTM A501 ASTM A847/A847M
(3) Pipe
ASTM A53/A53M, Gr. B
(4) Plates
ASTM A36/A36M ASTM A588/A588M
ASTM A242/A242M ASTM A709/A709M
ASTM A283/A283M ASTM A852/A852M
ASTM A514/A514M ASTM A1011/A1011M
ASTM A529/A529M ASTM A1043/A1043M
ASTM A572/A572M
(5) Bars
ASTM A36/A36M ASTM A572/A572M
ASTM A529/A529M ASTM A709/A709M
(6) Sheets
ASTM A606/A606M
ASTM A1011/A1011M SS, HSLAS, AND HSLAS-F
'''



def steel(steelmember):
    return steelraw[steelmember.upper()]


testunit = 's8x23'
e_steel = 29000000
fy= 50
def slender_check():
    if steelraw[steelmember.upper()]['TYPE'] == 'W':
        print('is w')


def tension_capacity(steelmember):
    print(steelraw[steelmember.upper()]['TYPE'])
    return .9*50*steelraw[steelmember.upper()]['AREA']
# the moment sections are not to be trusted!
def moment(force,distance):
    moment = force * distance
    print( moment)
    return moment

def moment_overturning(force,distance,width):
    return (force*distance/width)

def moment_capacity(steelbeam):
    phi = .9
    sy = steelraw[steelinput(steelbeam)]['Sy']
    sy = phi*sy
    return sy    

def moment_dcr():
    pass

#chapter D: Design of members for tension
fy = 'yield_stress'
ag = 'gross_area_steel'
fu = 'ultimate_strength'
ae = 'effective_area_steel'
#pn = fy * ag
phi_pn_fy = .9
phi_pn_fu = .75

	
'''	
#Chapter E: Design of members for compressions
phi_compression = .9
ae = {'effective net area', 0}
u = {'shear lag' : 0}
an = {'net area':0}
ae = an * u

#chapter F
Mmax = 1
Ma = 0
Mb = 0
Mc = 0
#F1-1
Cb = 12.5 * Mmax / ( 2.5*Mmax+ 3*Ma + 4*Mb + 3*Mc)

#F2-1
F_y = 36000
Z_x = 1

Mp = F_y * Z_x
Mn = Mp'''
'''
if lb =< lp:
    pass
elif lp < lp < lr:
    mn = cb(mp - (mp - .7*fy*sx*((lb-lp)/(lr-lp)))
    if mn > mp:
        mn = mp
else:
    mn = fcr * sx
    if mn > mp:
        mn = mp
'''

def freewidth(member):
    member = steelraw[member]
    #print(member)
    wid = member['bf']/2-member['tf']
    print(wid)
    #wid = member['bf']/2 - member['kf']
    #return wid

def tests():
    pass

if __name__ == '__main__': 
    freewidth('w10x15')


#b1 = 'w10x15'