import arcpy


arcpy.env.overwriteOutput = True

arcpy.env.workspace=r"C:\Users\17065\OneDrive\Desktop\NRS 528\Midterm"

WA_coast_single_XY_correct_csv = "WA_coast_single_XY_correct.csv"
Boundary = "Boundary.shp"

 # Process: XY Table To Point (XY Table To Point) (management)
WA_coast_XY_TableToPoint = "WA_coast_XY_TableToPoint.shp"

arcpy.management.XYTableToPoint(in_table=WA_coast_single_XY_correct_csv,
                                out_feature_class=WA_coast_XY_TableToPoint,
                                x_field="correct_longitude",
                                y_field="correct_latitude",
                                z_field="",
                                coordinate_system="GEOGCS['GCS_WGS_1984',DATUM['D_WGS_1984',SPHEROID['WGS_1984',6378137.0,298.257223563]],\
                                PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]];\
                                -400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision")

 # Process: Project (Project) (management)
WA_coast_single_XY_correct_X = "WA_coast_single_XY_correct_X.shp"

arcpy.management.Project(in_dataset=WA_coast_XY_TableToPoint,
                         out_dataset=WA_coast_single_XY_correct_X,
                         out_coor_system="PROJCS['NAD_1983_2011_StatePlane_Rhode_Island_FIPS_3800',\
GEOGCS['GCS_NAD_1983_2011',DATUM['D_NAD_1983_2011',SPHEROID['GRS_1980',6378137.0,298.257222101]],\
PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],\
PARAMETER['False_Easting',100000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-71.5],\
PARAMETER['Scale_Factor',0.99999375],PARAMETER['Latitude_Of_Origin',41.08333333333334],UNIT['Meter',1.0]]",
                        transform_method=[],
                        in_coor_system="",
                        preserve_shape="NO_PRESERVE_SHAPE",
                        max_deviation="",
                        vertical="NO_VERTICAL")

# Process: Project (2) (Project) (management)
muni97d_Project = "muni97d_Project.shp"

arcpy.management.Project(in_dataset=Boundary, out_dataset=muni97d_Project, out_coor_system="PROJCS['NAD_1983_2011_StatePlane_Rhode_Island_FIPS_3800',\
GEOGCS['GCS_NAD_1983_2011',DATUM['D_NAD_1983_2011',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],\
PROJECTION['Transverse_Mercator'],PARAMETER['False_Easting',100000.0],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-71.5],PARAMETER['Scale_Factor',0.99999375],\
PARAMETER['Latitude_Of_Origin',41.08333333333334],UNIT['Meter',1.0]]",
                        transform_method=["WGS_1984_(ITRF00)_To_NAD_1983 + WGS_1984_(ITRF08)_To_NAD_1983_2011"],
                        in_coor_system="PROJCS['NAD_1983_StatePlane_Rhode_Island_FIPS_3800_Feet',\
GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],\
PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Transverse_Mercator'],\
PARAMETER['False_Easting',328083.3333333333],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-71.5],\
PARAMETER['Scale_Factor',0.99999375],PARAMETER['Latitude_Of_Origin',41.08333333333334],UNIT['Foot_US',0.3048006096012192]]",
                         preserve_shape="NO_PRESERVE_SHAPE",
                         max_deviation="",
                         vertical="NO_VERTICAL")


Output_Feature_Class_2_ = "muni97d_Project_PolygonToLin.shp"

arcpy.management.PolygonToLine(in_features=muni97d_Project, out_feature_class=Output_Feature_Class_2_, neighbor_option="IDENTIFY_NEIGHBORS")

# Process: Near (Near) (analysis)

Updated_Input_Features = arcpy.analysis.Near(in_features=WA_coast_single_XY_correct_X, near_features=[Output_Feature_Class_2_],
                                             search_radius="", location="NO_LOCATION", angle="NO_ANGLE", method="PLANAR",
                                             field_names=[["NEAR_FID", "NEAR_FID"], ["NEAR_DIST", "NEAR_DIST"]])[0]

# Process: Table To Excel (Table To Excel) (conversion)
Results = "Results.xls"

arcpy.conversion.TableToExcel(Input_Table=Updated_Input_Features, Output_Excel_File=Results, Use_field_alias_as_column_header="NAME", Use_domain_and_subtype_description="CODE")
