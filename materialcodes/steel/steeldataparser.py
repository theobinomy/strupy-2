#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 15:56:40 2017

@author: sean
"""
#import pprintp
import constants
import csv
reader = csv.reader('steel.csv')


i = []
with open('steel.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        i.append(row)
     
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


def pass_steel():
    return steels

steels = {}
for j in range(len(i)):
    aab = list(zip(i[0][1:],i[j][1:]))
    props = {aab[i][0]:aab[i][1] for i in range(0,len(aab))}
    steels[i[j][0]] = props
aab = None

i,j,k,row,props,warmer = None,None,None,None,None,None
sap_enum = {0:'A36',1:'ASTM A53',2:'1'}
typ_grade = {'2L':'A36','Pipe':'Gr','HSS':'steel'}
zz=[]

def get_type(name):
    return steels[name]['TYPE']
    
def get_material(name):
    type_ = get_type(name)
    mat = typ_grade[type_]
    return mat

def sapsteelinsert(name):
    shape = steels[name]['TYPE']
    mat_ = get_material(shape)
    type_ = get_type(shape)
    
with open("Output.txt", "w") as text_file:
    text_file.writelines(steels)
#import pickle

#output = open(')
#data = steels

#pickle.dump(data, output)
#output.close()
#
#with open('aisc314.txt', 'w') as out:
#    #pprint.pprint(print('AISC310'),stream=out)
#    out.write("aisc314=")
#    pprint.pprint(steels, stream=out)

if __name__ == "__main__":
    b1 = 'W10X15'
    print(get_type(b1))
    print(get_material(b1))
    print(sapsteelinsert(b1))
    b = input('hello:')

	
	horseofcourse11