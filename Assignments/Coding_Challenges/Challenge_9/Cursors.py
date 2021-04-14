# Coding Challenge 9
# In this coding challenge, your objective is to utilize the arcpy.da module to undertake some basic partitioning of your dataset.
# In this coding challenge, I want you to work with the Forest Health Works dataset from RI GIS (I have provided this as a downloadable ZIP file in this repository).
#
# Using the arcpy.da module (yes, there are other ways and better tools to do this),
# I want you to extract all sites that have a photo of the invasive species (Field: PHOTO) into a new Shapefile, and do some basic counts of the dataset.
# In summary, please addressing the following:
#
# Count how many sites have photos, and how many do not (2 numbers), print the results.
#
# Count how many unique species there are in the dataset, print the result.
#
# Generate two shapefiles, one with photos and the other without.

# 1
import arcpy

arcpy.env.workspace = r'C:\Users\17065\OneDrive\Desktop\NRS 528\RI_Forest_Health_Works_Project_Points_All_Invasives'
input_shp = 'RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp'
fields = ['Species', 'photo']

expression = arcpy.AddFieldDelimiters(input_shp, "photo") + " = 'y'"

count = 0
with arcpy.da.SearchCursor(input_shp, fields, expression) as cursor:
    for row in cursor:
        print(u'{0}, {1}'.format(row[0], row[1]))

        count = count + 1

expression = arcpy.AddFieldDelimiters(input_shp, "photo") + " <> 'y'"

count1 = 0
with arcpy.da.SearchCursor(input_shp, fields, expression) as cursor:
    for row in cursor:
        print(u'{0}, {1}'.format(row[0], row[1]))

        count1 = count1 + 1


print(str(count)+" sites have photos")
print(str(count1)+" sites do not have photos")

# 2
list = []
with arcpy.da.SearchCursor(input_shp, ['Species']) as cursor:
    for row in cursor:
        list.append(row[0])

list_count={}
for i in list:
    if i not in list_count.keys():
        list_count[i]=1
    else:
        list_count[i]+=1

print("There are "+str(len(list_count))+" unique species in the dataset")



# 3

arcpy.env.overwriteOutput = True

output="photo.shp"
output1="no_photo.shp"
expression="photo = 'y'"
expression1="photo<>'y'"
arcpy.Select_analysis(input_shp, output, expression)
arcpy.Select_analysis(input_shp, output1, expression1)

if arcpy.Exists(output):
    print("Created shapefiles with photos successfully!")
if arcpy.Exists(output1):
    print("Created shapefiles without photos successfully!")
