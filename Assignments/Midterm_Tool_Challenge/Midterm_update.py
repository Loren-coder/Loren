
# In this assignment, you are instructed to produce a small script tool that takes advantage of arcpy and Python.
# You will need to provide example data, and the code should run on all PC's.
# The tool needs to manipulate a dataset across three different processes, for example, extracting, modifying and exporting data.
# The exact workflow is entirely up to yourself. You are expected to take 3-4 hours on this coding assignment,
# and you should deposit your code and example files within a Github repository for feedback and grading.

# The criteria are:

# Cleanliness of code (10 points)
# Functionality (10 points)
# Appropriate use of documentation (10 points)
# Depth of processing operation (10 points)
# In addition, you must provide example data and minimize the amount of editing a user must make in order for the program to run (10 points).



# The objective of this research is to calculate the distance to the coast from the houses in Rhode Island coastal area,
# and then export the results to excel.

import arcpy


arcpy.env.overwriteOutput = True

arcpy.env.workspace=r"C:\Users\17065\OneDrive\Desktop\NRS 528\Midterm"

 # The first process displays houses on the map based on the coordinates in the table using "XY Table To Point" tool
 # invalid values can be ignored because of missing data

table = "WA_coast_single_XY_correct.csv"
housing_points = "WA_coast_XY_TableToPoint.shp"
longitude="correct_longitude"
latitude="correct_latitude"
z_field=""
coordinate_system=arcpy.SpatialReference(4326)  # 4326 == WGS 1984

arcpy.management.XYTableToPoint(table,housing_points,longitude,latitude,z_field,coordinate_system)

if arcpy.Exists(housing_points):
    print("Display points successfully!")

 # Next, I am going to project housing layer and boundary layer to Rhode Island coordinate system

housing_points_projected = "housing_points_projected.shp"
boundary="Boundary.shp"
boundary_project="boundary_project.shp"
coor_system=coordinate_system=arcpy.SpatialReference(6567) #6567==NAD 1983 (2011) StatePlane Rhode Island FIPS 3800 (Meters)

arcpy.management.Project(housing_points,housing_points_projected,coor_system)
arcpy.management.Project(boundary,boundary_project,coor_system)

if arcpy.Exists(housing_points_projected):
    print("Project points successfully!")
if arcpy.Exists(boundary_project):
    print("Project boundary successfully!")

# Then, I am going to calculate the distance to the coast from each house.
# First, I need to convert the state boundary from polygon feature to line feature. This is because the near feature is line.

boundary_line = "boundary_PolygonToLin.shp"

arcpy.management.PolygonToLine(boundary_project, boundary_line)

if arcpy.Exists(boundary_line):
    print("Convert successfully!")


# Second, I calculate the distance using "Near" tool

arcpy.analysis.Near(housing_points_projected,boundary_line)


# Finally, I export the data to excel using "Table To Excel" tool

Results = "Results.xls"

arcpy.conversion.TableToExcel(housing_points_projected, Results)

if arcpy.Exists(Results):
    print("Created table successfully!")
