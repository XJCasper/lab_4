#Run Dissolve tool on parks.shp using PARK_TYPE feald as the field for 
#aggregating features.  Specify that multipart features are not allowed.
import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exersise05/Results"
arcpy.Dissolve_management("parks.shp", "parks_dissolved.shp", "PARK_TYPE", "", "FALSE")