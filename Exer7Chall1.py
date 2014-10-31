#Create 15,000-meter buffer around airports.shp items classified as an airports
#(based on the FEATURE field) + 7,500-meter buffer around airports.shp items
#classified as seaplane base.
import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise07"
air = " \"FEATURE\" = 'Airport'"
sea = " \"FEATURE\" = 'Seaplane Base'"
arcpy.Select_analysis ("airports.shp", "Results/airports_final.shp", air)
arcpy.Select_analysis ("airports.shp", "Results/seaports.shp", sea)
arcpy.Buffer_analysis("Results/airports_final.shp", "Results/airport_buffers.shp", "15000 METERS")
arcpy.Buffer_analysis("Results/seaports.shp", "Results/seaports_buffer.shp", "7500 METERS")