#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 13:41:41 2017

@author: sean
"""

#import lxml
#from lxml import etree
#from xml.etree import ElementTree as etree
#
#tree = etree.parse('sapmat2.xml')
#root = tree.getroot()
#root1 = tree.getroot()
#for child in root:
#   print(child.tag, child.attrib)

#==============================================================================
import xmltodict
 
with open('sapmat.xml') as fd:
    doc = xmltodict.parse(fd.read())
 
sapmats = doc['propertyFile']['region']['collection']['standard']
# 
# doc = None
# 
# #zz = []
# 
# for i in range(len(sapmats)):
#     dict(sapmats[i])
#     
#==============================================================================
from xml.dom import minidom

saps = minidom.parse('sapmat.xml')

propf = saps.getElementsByTagName('propertyFile')[0]
region = propf.getElementsByTagName('region')[0]
collection = region.getElementsByTagName('collection')[0]
standard = collection.getElementsByTagName('standard')
for stan in standard:
    print(stan)

#      ']['collection']['standard']

