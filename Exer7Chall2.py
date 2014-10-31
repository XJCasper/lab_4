#Add a text field to teh roads.shp called "FERRY"
import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise07"
fc = "roads.shp"
arcpy.AddField_management(fc, "FERRY", "TEXT", "", "", 30)
#Populate FERRY field with YES and NO values, pending on FEATURE field.
cursor = arcpy.da.UpdateCursor(fc, ["FEATURE", "FERRY"])
for row in cursor:
	if row[0] == "Ferry Crossing":
		row[1] = "YES"
	else:
		row[1] = "NO"
	cursor.updateRow(row)