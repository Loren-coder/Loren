import arcpy


arcpy.env.overwriteOutput = True

def XY_display(path,data,output,longitude,latitude,height,coordinate_system,points) :

    arcpy.env.workspace=path

    arcpy.management.XYTableToPoint(in_table=data,
                                out_feature_class=output,
                                x_field=longitude,
                                y_field=latitude,
                                z_field=height,
                                coordinate_system=coordinate_system)
    print(points+ " coordinates are displayed successfully")


XY_display(r"C:\Users\17065\OneDrive\Desktop\NRS 528\test","WA_coast_single_XY_correct.csv","houses.shp","correct_longitude","correct_latitude","","4326","Coastal houses")
XY_display(r"C:\Users\17065\OneDrive\Desktop\NRS 528\test","BI wind farm XY.csv","turbines.shp","Longitude","Latitude","","4326","Block Island wind turbines")
XY_display(r"C:\Users\17065\OneDrive\Desktop\NRS 528\test","RI_solar.csv","solar_farms.shp","Longitude","Latitude","","4326","RI solar farms")
