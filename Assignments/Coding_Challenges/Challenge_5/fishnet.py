# For this coding challenge, I want you to practice the heatmap generation that we went through in class, but this time obtain your own input data, and I want you to generate heatmaps for TWO species.


# My requirements are:

# The two input species data must be in a SINGLE CSV file, you must process the input data to separate out the species (Hint: You can a slightly edited version of our CSV code from a previous session to do this), I recommend downloading the species data from the same source so the columns match.
# Only a single line of code needs to be altered (workspace environment) to ensure code runs on my computer, and you provide the species data along with your Python code.
# The heatmaps are set to the right size and extent for your species input data, i.e. appropriate fishnet cellSize.
# You leave no trace of execution, except the resulting heatmap files.
# You provide print statements that explain what the code is doing, e.g. Fishnet file generated.



import arcpy
arcpy.env.overwriteOutput = True



arcpy.env.workspace = r"C:\Users\17065\OneDrive\Desktop\NRS 528"

in_Table = r"2 species.csv"
x_coords = "decimallongitude"
y_coords = "decimallatitude"
out_Layer = "2_fish"
saved_Layer = r"2_fish_Output.shp"


spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984
lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, "")


print(arcpy.GetCount_management(out_Layer))

arcpy.CopyFeatures_management(lyr, saved_Layer)
if arcpy.Exists(saved_Layer):
    print ("Created file successfully!")



desc = arcpy.Describe(saved_Layer)
XMin = desc.extent.XMin
XMax = desc.extent.XMax
YMin = desc.extent.YMin
YMax = desc.extent.YMax




arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)

outFeatureClass = "Fishnet.shp"


originCoordinate = str(XMin) + " " + str(YMin)
yAxisCoordinate = str(XMin) + " " + str(YMin + 1.0)
cellSizeWidth = "0.25"
cellSizeHeight = "0.25"
numRows =  ""
numColumns = ""
oppositeCorner = str(XMax) + " " + str(YMax)
labels = "NO_LABELS"
templateExtent = "#"
geometryType = "POLYGON"

arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                               cellSizeWidth, cellSizeHeight, numRows, numColumns,
                               oppositeCorner, labels, templateExtent, geometryType)

if arcpy.Exists(outFeatureClass):
    print ("Created Fishnet file successfully!")




target_features="Fishnet.shp"
join_features="2_fish_Output.shp"
out_feature_class="HeatMap.shp"
join_operation="JOIN_ONE_TO_ONE"
join_type="KEEP_ALL"
field_mapping=""
match_option="INTERSECT"
search_radius=""
distance_field_name=""

arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                           join_operation, join_type, field_mapping, match_option,
                           search_radius, distance_field_name)


if arcpy.Exists(out_feature_class):
    print ("Created Heatmap file successfully!")
    print ("Deleting intermediate files")
    arcpy.Delete_management(target_features)
    arcpy.Delete_management(join_features)
