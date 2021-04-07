import arcpy
from arcpy.sa import *

import os

workspace = r"C:\Users\17065\OneDrive\Desktop\NRS 528\06_Cheating\ALL_FILES_lfs\Step_3_data_lfs"

# Create list of workspace files
listMonths = os.listdir(workspace)
print(listMonths)

for month in listMonths:
    arcpy.env.workspace = workspace + "\\" + str(month)  # will change which file is being worked with as it loops for the workspace
    listRasters = arcpy.ListRasters("*", "TIF")
    # print(listRasters)
    # Remove all but B4.tif and B5.tif files from the list, replace ****** with the correct string.
    B4Raster = [x for x in listRasters if "B4" in x]
    print(B4Raster)
    Red = workspace + "\\" + str(month) + "\\" + str(B4Raster[0])
    print(Red)
    B5Raster = [x for x in listRasters if "B5" in x]
    print(B5Raster)
    NIR = workspace + "\\" + str(month) + "\\" + str(B5Raster[0])
    print(NIR)
    print()  # space between loop iteration print outs

    #AD - Printing these to get a feel for what they look like.
    print(Red)
    print(NIR)

    output_raster = (Raster(NIR) - Raster(Red)) / (Raster(NIR) + Raster(Red))
    output_raster.save(workspace + "\\" + str(month) + "\\" + str(month) + "_NDVI.tif")
