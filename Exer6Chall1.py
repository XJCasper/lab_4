#Read all feature classes in a workspace
import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise06/Results"
fc_list = arcpy.ListFeatureClasses()
#print names of each feature class and geometry type
for fc in fc_list:
	desc = arcpy.Describe(fc)
	print "{0} is a {1} feature class".format(desc.basename, desc.shapeType)