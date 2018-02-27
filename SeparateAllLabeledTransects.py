# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 16:04:55 2018

@author: danwa
"""

# Name: SplitByAttributes.py
# Description: Use the SplitByAttributes tool to split a feature class by unique values.

# Import required modules
import arcpy
from arcpy import env
env.workspace = r"C:\\Users\\danwa\\Documents\\Programming\\Trutta\\DuckRiver\\Duck.gdb"
# Set local variables
in_feature_class = 'DuckAllDay3456dCopy.shp'
target_workspace = r'c:/Users/danwa/Documents/Programming/Trutta/DuckRiver/'
fields = ['xs_ID']

out_path = r"C:\\Users\\danwa\\Documents\\Programming\\Trutta\\DuckRiver\\"

featureList = [arcpy.SplitByAttributes_analysis(in_feature_class, target_workspace, fields)]

tables = []
features = []
string = "T"
end = ".dbf"
end1 = ".shp"

tables = [string+str(i)+end for i in range(30,95)]
features = [string+str(i)+end1 for i in range(30,95)]

#del tables[0]
#del features[0]

spRef = arcpy.Describe(in_feature_class).spatialReference
featsTemp = []
tableList = arcpy.ListTables()
tableListNum = range(len(tableList))

#table = tableList[3]
#feature = features[3]
 
for i in tableListNum:
    featsTemp.append(arcpy.MakeXYEventLayer_management(tableList[i], "EAST", "NORTH", features[i] , spRef, ""))

shapes = []
for i in range(len(featsTemp)):
    shapes.append(arcpy.CopyFeatures_management(featsTemp[i], out_path+features[i]))
 