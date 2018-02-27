# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 10:10:19 2018

@author: danwa
"""
import arcpy
from arcpy import env

env.workspace = r"C:\\Users\\danwa\\Documents\\Programming\\Trutta\\DuckRiver\\"

#fcs = ['T19_straight', 'T21_straight','T22_straight', 'T24_straight', 'T26_straight', 'T26_straight', 'T28_straight', 'T29_straight']
    
features = []
string = "T"
end1 = ".shp"

features = [str(i)+end1 for i in range(30,95)]

snapEnv = ['transectLines', 'EDGE', '50 Feet']

for fc in features:
    arcpy.Snap_edit(fc, [snapEnv])