#Determine whetehr ArcGIS 3D Analyst, ArcGIS Network Analyst, and ArcGIS Spatial Anlyst.
import arcpy

default = "No extensions available"
if arcpy.CheckExtension("3D") == "Available":
	ext_3D = "3D Analyst "
else:
	ext_3D = ""
if arcpy.CheckExtension("Network") == "Available":
	ext_network = "Network Analyst "
else:
	ext_network = ""
if arcpy.CheckExtension("Spatial") == "Available":
	ext_spatial = "Spatial Analyst "
else:
	ext_spatial = ""
#Printed information message with resulsts, "The following
#extensions are available: ..."
print "The following extensions are available: " + ext_3D + ext_network + ext_spatial + default