#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 15:56:40 2017

@author: sean
"""
#import pprintp
import constants
import csv
reader = csv.reader('NDS_Design_Values1.csv')

#creates list of datafile
i = []
with open('NDS_Design_Values3.csv', newline='') as csvfile:
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


def pass_wood():
    return woods

#writes all wood items to single dict
woods = {}
for j in range(len(i)):
    aab = list(zip(i[0][1:],i[j][1:]))
    props = {aab[i][0]:aab[i][1] for i in range(0,len(aab))}
    woods[i[j][0]] = props



i=j=k=row=props=warmer= aab =zz= rr=None

sap_enum = {0:'A36',1:'ASTM A53',2:'1'}
typ_grade = {'2L':'A36','Pipe':'Gr','HSS':'steel'}
zz=[]

def get_type(name):
    return woods[name]['CLASS']
    
def get_material(name):
    type_ = get_type(name)
    mat = typ_grade[type_]
    return mat

def sapsteelinsert(name):
    shape = woods[name]['TYPE']
    mat_ = get_material(shape)
    type_ = get_type(shape)
    
with open("Output.txt", "w") as text_file:
    text_file.writelines(woods)
    
    
class wood_species(object):
    name = object
    def __init__(self, name): #,e, fb, fc_par, fc_perp, ft, fv, grade, name, size, species):
        self.e = woods[name]['E']
        self.fb = woods[name]['FB'] 
        self.fc_par = woods[name]['FC_PAR'] 
        self.fc_perp = woods[name]['FC_PERP'] 
        self.ft = woods[name]['FT']
        self.fv = woods[name]['FV']
        self.grade = woods[name]['GRADE'] 
        #self.name = woods[name]['NAME']
        self.size = woods[name]['SIZE']
        self.species = woods[name]['SPECIES']
    def __call__(self):
        return f'the species is {species}'

class wood_beam(object):
    def __init__(self,object):
        spec_name = 'WHITE OAK STANDARD'
        size = '2x4'
        if size == '2x4':
            b = 2
            d = 4
        self.species = wood_species(spec_name)
        self.spanlength = 10 #10 feet

#pickle.dump(data, output)
#output.close()


if __name__ == "__main__":
    #foo = wood_species('WHITE OAK STANDARD')
    pass
