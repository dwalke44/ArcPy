# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 09:16:30 2018

@author: danwa
"""

#Delete identical records

import arcpy
from arcpy import env

env.workspace = r"C:\\Users\\danwa\\Documents\\Programming\\Trutta\\DuckRiver\\"

features = []
for i in range(30, 95):
    features.append("%d" % i)
#del features[0]

for fc in features:
    arcpy.DeleteIdentical_management(fc, "SECID")

del features[0]

for fc in features:
    arcpy.ApplySymbologyFromLayer_management(fc, "30")