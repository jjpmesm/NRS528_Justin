# In this coding challenge, my objective is to utilize the arcpy.da module to undertake some basic partitioning of my dataset.
# In this coding challenge, I work with the Forest Health Works dataset from RI GIS.

# Using the arcpy.da module , I extract all sites that have a photo of the invasive species (Field: PHOTO) into a new Shapefile,
# and do some basic counts of the dataset. In summary, I address the following:

# Count how many individual records have photos, and how many do not (2 numbers), print the results.

# Count how many unique species there are in the dataset, print the result.

# Generate two shapefiles, one with photos and the other without.

import os
import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\NRS_528\Coding_Challenges\NRS528_Justin\challenge9"
input_shp = r"RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp"

# Creating empty shapefile that will contain the data with photos.

# Setting local variables.

out_path = arcpy.env.workspace
out_name = "with_photos.shp"
geometry_type = "POINT"
template = "RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp"
has_m = "DISABLED"
has_z = "DISABLED"

# Using Describe to get a SpatialReference object.

spatial_ref = 4326

# Executing CreateFeatureclass.

arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template,
                                    has_m, has_z, spatial_ref)

if arcpy.Exists(out_name):
    print("Created the photos shapefile successfully!")

# Counting individual records that do have photos.


fields = ['Other']

expression = arcpy.AddFieldDelimiters(input_shp, 'Other') + " = 'PHOTO'"
count = 0

with arcpy.da.SearchCursor(input_shp, fields, expression) as cursor:
    with arcpy.da.InsertCursor(out_name, fields, "") as insert_cursor:
        for row in cursor:
            # print(u'{0}'.format(row[0]))
            count = count + 1
            insert_cursor.insertRow(row)

print("There are " + str(count) + " species with a photo.")

# Setting local variables.

out_path = arcpy.env.workspace
out_name = "without_photos.shp"
geometry_type = "POINT"
template = "RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp"
has_m = "DISABLED"
has_z = "DISABLED"

# Using Describe to get a SpatialReference object.

spatial_ref = 4326

# Executing CreateFeatureclass.

arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, template,
                                    has_m, has_z, spatial_ref)

if arcpy.Exists(out_name):
    print("Created the without photos shapefile successfully!")

# Counting individual records that do not have photos.

input_shp = r"RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp"
fields = ['Other']

expression = arcpy.AddFieldDelimiters(input_shp, 'Other') + " = ' '"
count = 0

with arcpy.da.SearchCursor(input_shp, fields, expression) as cursor:
    with arcpy.da.InsertCursor(out_name, fields, "") as insert_cursor:
        for row in cursor:
            # print(u'{0}'.format(row[0]))
            count = count + 1
            insert_cursor.insertRow(row)

print("There are " + str(count) + " species without a photo.")

# Counting how many unique species are listed.

input_shp = r"RI_Forest_Health_Works_Project%3A_Points_All_Invasives.shp"
fields = ['Species']
species_list = []
count = 0

with arcpy.da.SearchCursor(input_shp, fields, expression) as cursor:
    for row in cursor:
        if row[0] not in species_list:
            species_list.append(row[0])
            count = count + 1

print("There are " + str(count) + " unique species in the dataset: " + str(species_list))