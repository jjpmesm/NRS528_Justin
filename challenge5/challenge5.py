# Challenge #5: Heat maps for the bull shark and whale shark (sourced from obis).

# In this coding challenge I'll create two species distribution heat maps that are from a .csv file. The .csv file is
# split into two separate species .csv files and both are converted into point shapefiles that represent species
# locations. A fishnet is generated over these points to set up the final heat map for both species. You only need to
# change line 13 for the coding challenge to your file location.

# Creating a list of the species

import os
import csv
import arcpy
arcpy.env.workspace = r"C:\NRS_528\Coding_Challenges\NRS528_Justin\challenge5\Species_Directory"
arcpy.env.overwriteOutput = True


# Determining the species lists

species_list = []

with open("species_list.csv") as species_csv:
    next(species_csv)
    for row in csv.reader(species_csv):
        if row[0] not in species_list:
            species_list.append(row[0])
    print(species_list)

# Splitting the larger .csv species file into separate .csv files based on species

os.mkdir("Species_Directory")

for species in species_list:

    header = "species,longitude,latitude\n"
    file = open(r"Species_Directory/" + str(species) + ".csv", "w")
    file.write(header)

    with open("species_list.csv") as longitude_csv:
        for row in csv.reader(longitude_csv):
            if row[0] == species:
                file.write(header)
                s_count = 0
            file.write(",".join(row))
            file.write("\n")

    file.close()

# Now time to create point shapefiles for the species.csv files

    in_Table = r"Species_Directory/" + species + ".csv"
    x_coords = "longitude"
    y_coords = "latitude"
    out_Layer = species
    saved_Layer = r"Species_Directory/" + species + "_output.shp"

# Set the spatial reference for the point shapefiles
    spRef = arcpy.SpatialReference(4326)
    lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, "")

# Print the total rows and create the file for the shape files
    print("The total rows in " + species + ".csv are: " + str((arcpy.GetCount_management(out_Layer))))

    arcpy.CopyFeatures_management(lyr, saved_Layer)

    if arcpy.Exists(saved_Layer):
        print("Created " + species + " shapefile successfully!")


# describing the extent of species point shapefiles
    desc = arcpy.Describe(saved_Layer)
    XMin = desc.extent.XMin
    XMax = desc.extent.XMax
    YMin = desc.extent.YMin
    YMax = desc.extent.YMax

# designating the spatial reference for species point shapefiles
    arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)

# Creating the fishnet from the species point shapefiles
    outFeatureClass = r"Species_Directory/" + species + "_Fishnet.shp"

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
        print("Created " + species + " Fishnet file successfully!")

# creating the heatmap from the species fishnet

    target_features=r"Species_Directory/" + species + "_Fishnet.shp"
    join_features=r"Species_Directory/" + species + "_Output.shp"
    out_feature_class=r"Species_Directory/" + species + "_HeatMap.shp"
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
        print("Created " + species + "Heatmap file successfully!")
        arcpy.Delete_management(target_features)
        arcpy.Delete_management(join_features)

#
# # The next step is to create a shape file for the Rhincodon.csv
#
# in_Table = r"Rhincodon.csv"
# x_coords = "longitude"
# y_coords = "latitude"
# out_Layer = "Rhincodon"
# saved_Layer = r"Rhincodon_output.shp"
#
# # Set the spatial reference
# spRef = arcpy.SpatialReference(4326)
# lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, "")
#
# # Print the total rows
# print("The total rows in Rhincodon.csv are: " + str((arcpy.GetCount_management(out_Layer))))
#
# arcpy.CopyFeatures_management(lyr, saved_Layer)
# if arcpy.Exists(saved_Layer):
#     print("Created Rhincodon shapefile successfully!")
#
# desc = arcpy.Describe("Rhincodon_output.shp")
# XMin = desc.extent.XMin
# XMax = desc.extent.XMax
# YMin = desc.extent.YMin
# YMax = desc.extent.YMax
#
# # designating the spatial reference for Rhincodon_output.shp
# arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)
#
# # Creating the Rhincodon_output.shp
# outFeatureClass = "Rhincodon_Fishnet.shp"
#
# # Set the origin of the fishnet
# originCoordinate = str(XMin) + " " + str(YMin)
# yAxisCoordinate = str(XMin) + " " + str(YMin + 1)
# cellSizeWidth = "5"
# cellSizeHeight = "5"
# numRows = ""
# numColumns = ""
# oppositeCorner = str(XMax) + " " + str(YMax)
# labels = "NO_LABELS"
# templateExtent = "#"
# geometryType = "POLYGON"
#
# arcpy.CreateFishnet_management(outFeatureClass, originCoordinate, yAxisCoordinate,
#                                cellSizeWidth, cellSizeHeight, numRows, numColumns,
#                                oppositeCorner, labels, templateExtent, geometryType)
#
# if arcpy.Exists(outFeatureClass):
#     print("Created Rhincodon Fishnet file successfully!")
#
# # creating the heatmap for Rhincodon_HeatMap.shp
#
# target_features="Rhincodon_Fishnet.shp"
# join_features="Rhincodon_output.shp"
# out_feature_class="Rhincodon_HeatMap.shp"
# join_operation="JOIN_ONE_TO_ONE"
# join_type="KEEP_ALL"
# field_mapping=""
# match_option="INTERSECT"
# search_radius=""
# distance_field_name=""
#
# arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
#                            join_operation, join_type, field_mapping, match_option,
#                            search_radius, distance_field_name)
#
# if arcpy.Exists(out_feature_class):
#     print("Created Rhincodon Heatmap file successfully!")
#     arcpy.Delete_management(target_features)
#     arcpy.Delete_management(join_features)
