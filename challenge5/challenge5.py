# Challenge #5: Heat maps for the bull shark and whale shark (sourced from obis).

# In this coding challenge, I'll create two species distribution heat maps that are from a single .csv file. The .csv
# file is split into two separate species files and both are converted into point shapefiles that represent species
# locations. A fishnet is generated over these points to set up the final heat map for both species. You only need to
# change line 12 for the coding challenge to your file location.

# declaring my imports, file path, etc.
import os
import csv
import arcpy
arcpy.env.workspace = r"C:\NRS_528\Coding_Challenges\NRS528_Justin\challenge5\Species_Directory"
arcpy.env.overwriteOutput = True


# Determining the species in the list
species_list = []

with open("species_list.csv") as species_csv:
    next(species_csv)
    for row in csv.reader(species_csv):
        if row[0] not in species_list:
            species_list.append(row[0])
    print("The two species in species_file.csv are: " + str(species_list))

# Splitting the larger .csv species file into separate .csv files based on species
os.mkdir("Species_Directory")

for species in species_list:

    header = "species,longitude,latitude\n"
    file = open(r"Species_Directory/" + str(species) + ".csv", "w")
    file.write(header)

    with open("species_list.csv") as longitude_csv:
        for row in csv.reader(longitude_csv):
            if row[0] == species:
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

# Setting the spatial reference for the point shapefiles
    spRef = arcpy.SpatialReference(4326)
    lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, "")

# Print the total rows and create the file for the shape files
    print("The total rows in " + species + ".csv: " + str((arcpy.GetCount_management(out_Layer))))
    arcpy.CopyFeatures_management(lyr, saved_Layer)
    if arcpy.Exists(saved_Layer):
        print("Created " + species + " point shapefile successfully!")

# Describing the extent of species point shapefiles
    desc = arcpy.Describe(saved_Layer)
    XMin = desc.extent.XMin
    XMax = desc.extent.XMax
    YMin = desc.extent.YMin
    YMax = desc.extent.YMax

# Designating the spatial reference for species point shapefiles
    arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)

# Creating the fishnet from the species point shapefiles
    outFeatureClass = r"Species_Directory/" + species + "_Fishnet.shp"

# Setting the origin of the fishnet
    originCoordinate = str(XMin) + " " + str(YMin)
    yAxisCoordinate = str(XMin) + " " + str(YMin + 1)
    cellSizeWidth = "2"
    cellSizeHeight = "2"
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
        print("Created " + species + " fishnet file successfully!")

# Creating the heatmap from the species fishnet
    target_features=r"Species_Directory/" +species + "_Fishnet.shp"
    join_features=r"Species_Directory/" +species + "_Output.shp"
    out_feature_class=r"Species_Directory/" +species + "_HeatMap.shp"
    join_operation="JOIN_ONE_TO_ONE"
    join_type="KEEP_ALL"
    field_mapping=""
    match_option="INTERSECT"
    search_radius=""
    distance_field_name=""

    arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                               join_operation, join_type, field_mapping, match_option,
                               search_radius, distance_field_name)

# Checking for file existence and deleting excess files
    if arcpy.Exists(out_feature_class):
        print("Created " + species + " heatmap file successfully!")
        arcpy.Delete_management(target_features)
        arcpy.Delete_management(join_features)
        print("Excess " + str(species) + " files deleted...")