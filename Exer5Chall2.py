#Add XY Features to hospital.shp
import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise05"
arcpy.AddXY_management("hospitals.shp")