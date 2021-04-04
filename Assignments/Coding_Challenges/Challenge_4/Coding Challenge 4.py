# Coding Challenge 4
# For this coding challenge, I want you to find a particular tool that you like in arcpy. It could be a tool that you have used in GIS before or something new.
# Try browsing the full tool list to get some insight here (click Tool Reference on the menu list to the left).
#
# Set up the tool to run in Python, add some useful comments, and importantly, provide some example data in your repository (try to make it open source, such as Open Streetmap, or RI GIS.
# You can add it as a zip file to your repository.
#
# My only requirements are:
#
# Comment your code well.
# Ensure that the code will run on my machine with only a single change to a single variable (i.e. a base folder location).

import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\Data\Students_2021\Dong\Assignments\Coding_Challenges\Challenge_4\Boundary"
# This is the folder location for all data

arcpy.Union_analysis(["OUTLINE25K_POLY.shp", "muni97d.shp"], "MA_RI")
# The files in the brackets are input features, "MA_RI" is the output data name. Union tool allows me to combine RI and MA together.


## Davies feedback - I executed your code and got an overwriteOutput error, so I fixed that by adding line 14 to ensure your code ran.