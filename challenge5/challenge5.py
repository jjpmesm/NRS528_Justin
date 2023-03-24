# Challenge #5: Heat maps for the bull shark and whale shark (sourced from obis)

# Creating a list of the species

import os
import csv
import arcpy

arcpy.env.overwriteOutput = True

species_list = []

with open("species_list.csv") as species_csv:
    next(species_csv)
    for row in csv.reader(species_csv):
        if row[0] not in species_list:
            species_list.append(row[0])
    print(species_list)

# this part of the script is the attempt to split the list into two separate .csv files for the species.
# I get an error that says the file cannot be created when the file already exists, however, I still have the new
# file created with the two correct .csv files that split the two species. Commenting this code out afterwards makes the
# rest of the code successful when you run it

for species in species_list:
    os.mkdir("Species_Directory")

    header = "species,longitude,latitude\n"

    for s in species_list:
        s_count = 1
        with open("species_list.csv") as longitude_csv:
            for row in csv.reader(longitude_csv):
                if row[0] == s:
                    if s_count == 1:
                        file = open(r"Species_Directory/" + str(s) + ".csv", "w")
                        file.write(header)
                        s_count = 0
                    file.write(",".join(row))
                    file.write("\n")
        file.close()

Now time to create a shapefile for Carcharhinus.csv

arcpy.env.workspace = r"C:\NRS_528\Coding_Challenges\NRS528_Justin\challenge5\Species_Directory"

in_Table = r"Carcharhinus.csv"
x_coords = "longitude"
y_coords = "latitude"
out_Layer = "Carcharhinus"
saved_Layer = r"Carcharhinus_output.shp"

# Set the spatial reference for Carcharhinus_output.shp
spRef = arcpy.SpatialReference(4326)
lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, "")

# Print the total rows and create the file for Carcharhinus_output.shp
print("The total rows in Carcharhinus.csv are: " + str((arcpy.GetCount_management(out_Layer))))

arcpy.CopyFeatures_management(lyr, saved_Layer)

if arcpy.Exists(saved_Layer):
    print("Created Carcharhinus shapefile successfully!")


# describing the extent of Carcharhinus_output.shp
desc = arcpy.Describe("Carcharhinus_output.shp")
XMin = desc.extent.XMin
XMax = desc.extent.XMax
YMin = desc.extent.YMin
YMax = desc.extent.YMax

# designating the spatial reference for Carcharhinus_output.shp
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)

# Creating the Carcharhinus_Fishnet.shp
outFeatureClass = "Carcharhinus_Fishnet.shp"

# Set the origin of the fishnet
originCoordinate = str(XMin) + " " + str(YMin)
yAxisCoordinate = str(XMin) + " " + str(YMin + 1)
cellSizeWidth = "0.25"
cellSizeHeight = "0.25"
numRows = ""
numColumns = ""
oppositeCorner = str(XMax) + " " + str(YMax)
labels = "NO_LABELS"
templateExtent = "#"
geometryType = "POLYGON"

arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                               cellSizeWidth, cellSizeHeight, numRows, numColumns,
                               oppositeCorner, labels, templateExtent, geometryType)

if arcpy.Exists(outFeatureClass):
    print("Created Carcharhinus Fishnet file successfully!")

# creating the heatmap for Carcharhinus_HeatMap.shp

target_features="Carcharhinus_Fishnet.shp"
join_features="Carcharhinus_Output.shp"
out_feature_class="Carcharhinus_HeatMap.shp"
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
    print("Created Carcharhinus Heatmap file successfully!")
    arcpy.Delete_management(target_features)
    arcpy.Delete_management(join_features)


# The next step is to create a shape file for the Rhincodon.csv

in_Table = r"Rhincodon.csv"
x_coords = "longitude"
y_coords = "latitude"
out_Layer = "Rhincodon"
saved_Layer = r"Rhincodon_output.shp"

# Set the spatial reference
spRef = arcpy.SpatialReference(4326)
lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, "")

# Print the total rows
print("The total rows in Rhincodon.csv are: " + str((arcpy.GetCount_management(out_Layer))))

arcpy.CopyFeatures_management(lyr, saved_Layer)
if arcpy.Exists(saved_Layer):
    print("Created Rhincodon shapefile successfully!")

desc = arcpy.Describe("Rhincodon_output.shp")
XMin = desc.extent.XMin
XMax = desc.extent.XMax
YMin = desc.extent.YMin
YMax = desc.extent.YMax

# designating the spatial reference for Rhincodon_output.shp
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)

# Creating the Rhincodon_output.shp
outFeatureClass = "Rhincodon_Fishnet.shp"

# Set the origin of the fishnet
originCoordinate = str(XMin) + " " + str(YMin)
yAxisCoordinate = str(XMin) + " " + str(YMin + 1)
cellSizeWidth = "5"
cellSizeHeight = "5"
numRows = ""
numColumns = ""
oppositeCorner = str(XMax) + " " + str(YMax)
labels = "NO_LABELS"
templateExtent = "#"
geometryType = "POLYGON"

arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
                               cellSizeWidth, cellSizeHeight, numRows, numColumns,
                               oppositeCorner, labels, templateExtent, geometryType)

if arcpy.Exists(outFeatureClass):
    print("Created Rhincodon Fishnet file successfully!")

# creating the heatmap for Rhincodon_HeatMap.shp

target_features="Rhincodon_Fishnet.shp"
join_features="Rhincodon_output.shp"
out_feature_class="Rhincodon_HeatMap.shp"
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
    print("Created Rhincodon Heatmap file successfully!")
    arcpy.Delete_management(target_features)
    arcpy.Delete_management(join_features)
