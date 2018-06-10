#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 15:56:40 2017

@author: sean
"""
import csv
import pint
ur = pint.UnitRegistry(system = 'US')
import pprint

#creates list of datafile
i = []
with open('NDS_Design_Values_Sawn_Lumber.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        i.append(row)

#make all items in file uppcercase     
for zz in range(len(i[0])):
    i[0][zz] = i[0][zz].upper()
for zz in range(len(i[1])):
    i[1][zz] = i[1][zz].upper()
for rr in range(len(i)):
    i[rr][0] = i[rr][0].upper()
#converts numbers to floats
for j in range(len(i)):
    for k in range(len(i[0])):
        try:
            i[j][k] = float(i[j][k])
        except ValueError:
            pass

#writes all wood items to single dict
woods = {}
for j in range(len(i)):
    aab = list(zip(i[0][1:],i[j][1:]))
    props = {aab[i][0]:aab[i][1] for i in range(0,len(aab))}
    woods[i[j][0]] = props

i= j= k= row= props= aab= zz= rr= None
   
with open("Output.txt", "w") as text_file:
    text_file.writelines(woods)
    
def pass_wood():
    return woods

class WoodSpecies():
    ''' this object is the wood object information)
    def __init__(self, e, e_main, fb, fc_par, fc_perp, ft, fv, grade,
    size, species, sp_grav, name): #,e, fb, fc_par, fc_perp, ft, fv, grade, name, size, species):'''
    def __init__(self, name):
        self.E =       woods[name]['E'] * ur.psi #(ur.pound / ur.inch**2)
        self.E_min =    woods[name]['EMIN'] * ur.psi
        self.F_b =      woods[name]['FB'] * ur.psi #(ur.pound / ur.inch**2)
        self.F_c_par =  woods[name]['FC_PAR'] * ur.psi
        self.F_c_perp = woods[name]['FC_PERP'] * ur.psi
        self.F_t =      woods[name]['FT'] * ur.psi
        self.F_v =      woods[name]['FV'] * ur.psi
        self.Grade =   woods[name]['GRADE']
        self.Size =    woods[name]['SIZE']
        self.Species = woods[name]['SPECIES']
        self.Sp_grav = woods[name]['SP_GRAV'] * ur.dimensionless
        self.Name = name

size_enum = {
    1: '2 in. - 4 in. wide',
    2: '2 in. & wider',
    3: 'opengrain',
    }

grade_enum = {
    1: 'ClearStructural',
    2: 'Construction',
    3: 'No.1',
    4: 'No.1&Btr',
    5: 'No.2',
    6: 'No.3',
    7: 'SelectStructural',
    8: 'Standard',
    9: 'Stud',
    10: 'Utility',
    }

species_enum = {
    1: 'ALASKA CEDAR',
    2: 'ALASKA HEMLOCK',
    3: 'ALASKA SPRUCE',
    4: 'ALASKA YELLOW CEDAR',
    5: 'ASPEN',
    6: 'BALDCYPRESS',
    7: 'BEECH-BIRCH-HICKORY',
    8: 'COAST SITKA SPRUCE',
    9: 'COTTONWOOD',
    10: 'DOUGLAS FIR-LARCH',
    11: 'DOUGLAS FIR-LARCH (NORTH)',
    12: 'DOUGLAS FIR-SOUTH',
    13: 'EASTERN HEMLOCK-BALSAM FIR',
    14: 'EASTERN HEMLOCK-TAMARACK',
    15: 'EASTERN SOFTWOODS',
    16: 'EASTERN WHITE PINE',
    17: 'HEM-FIR',
    18: 'HEM-FIR (NORTH)',
    19: 'MIXED MAPLE',
    20: 'MIXED OAK',
    21: 'NORTHERN RED OAK',
    22: 'NORTHERN SPECIES',
    23: 'NORTHERN WHITE CEDAR',
    24: 'RED MAPLE',
    25: 'RED OAK',
    26: 'REDWOOD',
    27: 'SPRUCE-PINE-FIR',
    28: 'SPRUCE-PINE-FIR (SOUTH)',
    29: 'WESTERN CEDARS',
    30: 'WESTERN WOODS',
    31: 'WHITE OAK',
    32: 'YELLOW CEDAR',
    33: 'YELLOW POPLAR',
    }

def spec_select():
    pprint.pprint(species_enum)
    #print(species_enum)
    species = input('what species would you like? >>')
    species = int(species)
    available_grades = []
    for i in woods:
        if woods[i]['SPECIES'] == species_enum[species]:
            #print(woods[i]['GRADE'])
            available_grades.append(woods[i]['GRADE'])
    print('the available grades are ', available_grades)
    pprint.pprint(grade_enum)
    grade = input('what grade would you like? >>')
    grade = int(grade)
    available_size = []
    for i in woods:
        if woods[i]['SPECIES'] == species_enum[species]:
            if woods[i]['GRADE'] == grade_enum[grade]:
            #print(woods[i]['GRADE'])
                available_size.append(woods[i]['SIZE'])
    print('the available sizes are ', available_size)
    pprint.pprint(size_enum)
    size = input('what size would you like? >')
    size = int(size)
    name = species_enum[species]+' ' + grade_enum[grade] +' '+ size_enum[size]
    name = name.upper()
    print(name)
    return name

if __name__ == '__main__':
    spec_select()
    pass
