#Read all feature classes
import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise06/Results"
#Copy polygon feature classes to a new geodatabase.
arcpy.CreateFileGDB_management("C:/EsriPress/Python/Data/Exercise06/Results", "newdata.gdb")
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
	fcdesc = arcpy.Describe(fc)
	if fcdesc.shapeType == "Polygon":
		arcpy.CopyFeatures_management(fc, "C:/EsriPress/Python/Data/Exercise06/Results/newdata.gdb/" + fc)