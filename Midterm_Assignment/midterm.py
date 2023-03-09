# For my midterm assignment, I'll be performing a clip function on a dataset of dams located in RI to the town of Glocester
#
# My RI_dams.csv file is sourced from the National Inventory of Dams database. The .csv file was cleaned up outside of
# python to keep important columns (name, longitude, latitude, etc.)
#
# My towns shapefile was extracted from the RIGIS database. The file was renamed from "muni97" to "towns".

import arcpy
import csv
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\NRS_528\Coding_Challenges\NRS528_Justin\Midterm_Assignment"

# Now we can convert the ri_dams.csv to a shapefile:

in_Table = r"RI_dams.csv"
x_coords = "longitude"
y_coords = "latitude"
out_Layer = "dams"
saved_Layer = r"ri_dams_output.shp"

# Setting the spatial reference for ri_dams_output.shp:
spRef = arcpy.SpatialReference(4326)
lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, "")

# Printing the total rows and creating the file for ri_dams_output.shp:
arcpy.CopyFeatures_management(lyr, saved_Layer)
print("The total number of RI dams are: " + str((arcpy.GetCount_management(out_Layer))))

# Double-checking that the ri dams shapefile was created:
if arcpy.Exists(saved_Layer):
    print("Created the RI dams shapefile successfully!")

# Now I'm projecting the RI dams shapefile into the Rhode Island State Plane using units of feet.
# The towns shape file is in this projection, so I'm just making sure everything will match up.

input_features = r"ri_dams_output.shp"
output_feature_class = r"ri_dams_RISP.shp"

# Creating a spatial reference object for the output coordinate system
out_coordinate_system = arcpy.SpatialReference('NAD 1983 StatePlane Rhode Island FIPS 3800 (US Feet)')

arcpy.Project_management(input_features, output_feature_class, out_coordinate_system)

# Double-checking that the projected RI dams shapefile was created:
if arcpy.Exists(output_feature_class):
    print("Created the RI dams (RISP) shapefile successfully!")

# Now we can select the town of Glocester as a standalone dataset from towns.shp:

# Setting local variables:
in_features = "towns.shp"
out_feature_class = "glocester.shp"
where_clause = '"NAME" = \'GLOCESTER\''

arcpy.analysis.Select(in_features, out_feature_class, where_clause)

# Double-checking that the town shapefile was created:
if arcpy.Exists(out_feature_class):
    print("Created the Glocester shapefile successfully!")

# Now I can clip the RI dams to the town of Glocester:

# Setting local variables:
in_features = "ri_dams_output.shp"
clip_features = "glocester.shp"
out_feature_class = "glocester_dams.shp"

arcpy.analysis.Clip(in_features, clip_features, out_feature_class)

# Getting a count of the clipped RI dams in the town of Glocester:
print("The total number of dams in Glocester are: " + str((arcpy.GetCount_management(out_feature_class))))

# Double-checking that the clip shapefile was created:
if arcpy.Exists(out_feature_class):
    print("Created the clipped dams in Glocester successfully!")

# Final step: deleting the excess dam and selected town shapefiles to only leave the input data and final result:
arcpy.Delete_management("ri_dams_output.shp")
arcpy.Delete_management("ri_dams_RISP.shp")
arcpy.Delete_management("glocester.shp")
print("Deleting intermediate files...")