# -*- coding: utf-8 -*-

print("asce 710 loaded")
class loads:
    pass
def loadfactor(combotype = None):
    combotype = 'LRFD'
    
    def load_combo(D=0, Lr =0, S =0, R=0,W=0,L=0,E=0,H=0):
        #LRFD
        L1 = 1.4*D
        opt1 = [Lr,S,R]
        opt2 = [L,0.5*W]
        L2 = 1.2*D+1.6*L+.5*max(opt1)
        L3 = 1.2*D + 1.6*max(opt1) + max(opt2)
        L4 = 1.2*D + W + L + .5*max(opt1)
        L5 = 1.2*D + E + L + .2*S
        L6 = 0.9*D + W
        L7 = 0.9*D + E
        ls = [L1,L2,L3,L4,L5,L6,L7]
        print(ls)
        max_load = max(L1,L2,L3,L4,L5,L6,L7)+H
        
        return max_load


    def load_combo_asd(D=0, Lr =0, S =0, R=0,W=0,L=0,E=0,H=0):
        #LRFD
        l1 = D
        l2 = D + L
        opt1 = [Lr,S,R]
        l3 = D + max(opt1)
        l4 = D + .75*L + .75*max(opt1)
        opt2 = [.6*W,0.7*E]
        l5 = D + max(opt2)
        l6a = D +.75*L + .75*.6*W+.75*max(opt1)
        l6b = D +.75*L + .75*.7*E+.75*S
        l7 = .6*D+.6*W
        l8 = .6*D+.7*E 
        max_load = max(l1,l2,l3,l4,l5,l6a,l6b,l7,l8)+H
        return max_load 
    
    return load_combo
        
        
def floorloads():
    #lot of work to do here  See table 4-1 ASCE
    val = input('please consult asce 4-1: for loads')
    str(val)
    if 'psf' not in val:
        val = val + " psf"
    return val #'20 psf'

def snowloads():
    #lot of work to do here
    return '25psf'

class wind():

    def __str__(self):
        return "20 mph"
    