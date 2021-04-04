# Coding Challenge 6
# Our coding challenge this week follows from the last exercise that we did in class during Week 6.
# 
# Task 1 - Use what you have learned to process the Landsat files provided, this time, 
# you know you are interested in the NVDI index which will use Bands 4 (red, aka vis) and 5 (near-infrared, aka nir) from the Landsat 8 imagery.
# Data provided are monthly (a couple are missing due to cloud coverage) during the year 2015 for the State of RI.
# 
# Before you start, here is a suggested workflow:
# 
# Extract the Step_3_data.zip file into a known location.
# For each month provided, you want to calculate the NVDI, using the equation: nvdi = (nir - vis) / (nir + vis) 
# https://en.wikipedia.org/wiki/Normalized_difference_vegetation_index. 
# Consider using the Raster Calculator Tool in ArcMap and using "Copy as Python Snippet" for the first calculation.
# The only rule is, you should run your script once, and generate the NVDI for ALL MONTHS provided. 
# As part of your code submission, you should also provide a visualization document (e.g. an ArcMap layout), 
# showing the patterns for an area of RI that you find interesting.

import arcpy

arcpy.env.workspace=r"C:\Users\17065\OneDrive\Desktop\NRS 528\06_Cheating\ALL_FILES_lfs\Step_3_data_lfs\201502"

# To allow overwriting outputs change overwriteOutput option to True.
arcpy.env.overwriteOutput = True

# Check out any necessary licenses.
arcpy.CheckOutExtension("spatial")
arcpy.CheckOutExtension("ImageAnalyst")

LC08_L1TP_012031_20150201_20170301_01_T1_B5_tif = arcpy.Raster("LC08_L1TP_012031_20150201_20170301_01_T1_B5.tif")
LC08_L1TP_012031_20150201_20170301_01_T1_B4_tif = arcpy.Raster("LC08_L1TP_012031_20150201_20170301_01_T1_B4.tif")


# Process: Raster Calculator (Raster Calculator) (ia)
NDVI = "C:\\Users\\17065\\OneDrive\\Desktop\\NRS 528\\NDVI\\ndvi02"
Raster_Calculator = NDVI
NDVI = nvdi =  (LC08_L1TP_012031_20150201_20170301_01_T1_B5_tif-LC08_L1TP_012031_20150201_20170301_01_T1_B4_tif)/(LC08_L1TP_012031_20150201_20170301_01_T1_B5_tif+LC08_L1TP_012031_20150201_20170301_01_T1_B4_tif)
NDVI.save(Raster_Calculator)


arcpy.env.workspace=r"C:\Users\17065\OneDrive\Desktop\NRS 528\06_Cheating\ALL_FILES_lfs\Step_3_data_lfs\201504"

# To allow overwriting outputs change overwriteOutput option to True.
arcpy.env.overwriteOutput = True

# Check out any necessary licenses.
arcpy.CheckOutExtension("spatial")
arcpy.CheckOutExtension("ImageAnalyst")

LC08_L1TP_012031_20150201_20170301_01_T1_B5_tif = arcpy.Raster("LC08_L1TP_012031_20150422_20170301_01_T1_B5.tif")
LC08_L1TP_012031_20150201_20170301_01_T1_B4_tif = arcpy.Raster("LC08_L1TP_012031_20150422_20170301_01_T1_B4.tif")


# Process: Raster Calculator (Raster Calculator) (ia)
NDVI = "C:\\Users\\17065\\OneDrive\\Desktop\\NRS 528\\NDVI\\ndvi04"
Raster_Calculator = NDVI
NDVI = nvdi =  (LC08_L1TP_012031_20150201_20170301_01_T1_B5_tif-LC08_L1TP_012031_20150201_20170301_01_T1_B4_tif)/(LC08_L1TP_012031_20150201_20170301_01_T1_B5_tif+LC08_L1TP_012031_20150201_20170301_01_T1_B4_tif)
NDVI.save(Raster_Calculator)

arcpy.env.workspace=r"C:\Users\17065\OneDrive\Desktop\NRS 528\06_Cheating\ALL_FILES_lfs\Step_3_data_lfs\201505"

# To allow overwriting outputs change overwriteOutput option to True.
arcpy.env.overwriteOutput = True

# Check out any necessary licenses.
arcpy.CheckOutExtension("spatial")
arcpy.CheckOutExtension("ImageAnalyst")

LC08_L1TP_012031_20150201_20170301_01_T1_B5_tif = arcpy.Raster("LC08_L1TP_012031_20150508_20170227_01_T1_B5.tif")
LC08_L1TP_012031_20150201_20170301_01_T1_B4_tif = arcpy.Raster("LC08_L1TP_012031_20150508_20170227_01_T1_B4.tif")


# Process: Raster Calculator (Raster Calculator) (ia)
NDVI = "C:\\Users\\17065\\OneDrive\\Desktop\\NRS 528\\NDVI\\ndvi05"
Raster_Calculator = NDVI
NDVI = nvdi =  (LC08_L1TP_012031_20150201_20170301_01_T1_B5_tif-LC08_L1TP_012031_20150201_20170301_01_T1_B4_tif)/(LC08_L1TP_012031_20150201_20170301_01_T1_B5_tif+LC08_L1TP_012031_20150201_20170301_01_T1_B4_tif)
NDVI.save(Raster_Calculator)


arcpy.env.workspace=r"C:\Users\17065\OneDrive\Desktop\NRS 528\06_Cheating\ALL_FILES_lfs\Step_3_data_lfs\201507"

# To allow overwriting outputs change overwriteOutput option to True.
arcpy.env.overwriteOutput = True

# Check out any necessary licenses.
arcpy.CheckOutExtension("spatial")
arcpy.CheckOutExtension("ImageAnalyst")

LC08_L1TP_012031_20150201_20170301_01_T1_B5_tif = arcpy.Raster("LC08_L1TP_012031_20150711_20170226_01_T1_B5.tif")
LC08_L1TP_012031_20150201_20170301_01_T1_B4_tif = arcpy.Raster("LC08_L1TP_012031_20150711_20170226_01_T1_B4.tif")


# Process: Raster Calculator (Raster Calculator) (ia)
NDVI = "C:\\Users\\17065\\OneDrive\\Desktop\\NRS 528\\NDVI\\ndvi07"
Raster_Calculator = NDVI
NDVI = nvdi =  (LC08_L1TP_012031_20150201_20170301_01_T1_B5_tif-LC08_L1TP_012031_20150201_20170301_01_T1_B4_tif)/(LC08_L1TP_012031_20150201_20170301_01_T1_B5_tif+LC08_L1TP_012031_20150201_20170301_01_T1_B4_tif)
NDVI.save(Raster_Calculator)


arcpy.env.workspace=r"C:\Users\17065\OneDrive\Desktop\NRS 528\06_Cheating\ALL_FILES_lfs\Step_3_data_lfs\201510"

# To allow overwriting outputs change overwriteOutput option to True.
arcpy.env.overwriteOutput = True

# Check out any necessary licenses.
arcpy.CheckOutExtension("spatial")
arcpy.CheckOutExtension("ImageAnalyst")

LC08_L1TP_012031_20150201_20170301_01_T1_B5_tif = arcpy.Raster("LC08_L1TP_012031_20151015_20170225_01_T1_B5.tif")
LC08_L1TP_012031_20150201_20170301_01_T1_B4_tif = arcpy.Raster("LC08_L1TP_012031_20151015_20170225_01_T1_B4.tif")


# Process: Raster Calculator (Raster Calculator) (ia)
NDVI = "C:\\Users\\17065\\OneDrive\\Desktop\\NRS 528\\NDVI\\ndvi10"
Raster_Calculator = NDVI
NDVI = nvdi =  (LC08_L1TP_012031_20150201_20170301_01_T1_B5_tif-LC08_L1TP_012031_20150201_20170301_01_T1_B4_tif)/(LC08_L1TP_012031_20150201_20170301_01_T1_B5_tif+LC08_L1TP_012031_20150201_20170301_01_T1_B4_tif)
NDVI.save(Raster_Calculator)


arcpy.env.workspace=r"C:\Users\17065\OneDrive\Desktop\NRS 528\06_Cheating\ALL_FILES_lfs\Step_3_data_lfs\201511"

# To allow overwriting outputs change overwriteOutput option to True.
arcpy.env.overwriteOutput = True

# Check out any necessary licenses.
arcpy.CheckOutExtension("spatial")
arcpy.CheckOutExtension("ImageAnalyst")

LC08_L1TP_012031_20150201_20170301_01_T1_B5_tif = arcpy.Raster("LC08_L1TP_012031_20151116_20170225_01_T1_B5.tif")
LC08_L1TP_012031_20150201_20170301_01_T1_B4_tif = arcpy.Raster("LC08_L1TP_012031_20151116_20170225_01_T1_B4.tif")


# Process: Raster Calculator (Raster Calculator) (ia)
NDVI = "C:\\Users\\17065\\OneDrive\\Desktop\\NRS 528\\NDVI\\ndvi11"
Raster_Calculator = NDVI
NDVI = nvdi =  (LC08_L1TP_012031_20150201_20170301_01_T1_B5_tif-LC08_L1TP_012031_20150201_20170301_01_T1_B4_tif)/(LC08_L1TP_012031_20150201_20170301_01_T1_B5_tif+LC08_L1TP_012031_20150201_20170301_01_T1_B4_tif)
NDVI.save(Raster_Calculator)



## Davies Feedback - I was not able to test this as you have taken several short cuts to achieving the challenge by
# hard coding file paths throughout. Whilst your code works on your machine, to make it work for me will take as long as it would
# to write the code. You have to avoid taking such short cuts, you should be using directory searches and building lists of files
# to manipulate.