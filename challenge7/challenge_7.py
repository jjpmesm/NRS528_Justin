# Using coding challenge #5 example to improve it with the addition of file management
import glob
import os
import csv
import arcpy

arcpy.env.overwriteOutput = True
species_list = []

data_file = "species_list.csv"
input_directory = r"C:\NRS_528\Coding_Challenges\NRS528_Justin\challenge7"

# Creating file paths for the data
if not os.path.exists(os.path.join(input_directory, "output_files")):
    os.mkdir(os.path.join(input_directory, "output_files"))
if not os.path.exists(os.path.join(input_directory, "temporary_files")):
    os.mkdir(os.path.join(input_directory, "temporary_files"))

# Determining the species

species_list = []
with open(os.path.join(input_directory, data_file)) as species_csv:
    header_line = next(species_csv)
    for row in csv.reader(species_csv):
        try:
            if row[0] not in species_list:
                species_list.append(row[0])
        except:
            pass

print("..There are: " + str(len(species_list)) + " species to process..")

# Splitting the species files into the temporary file folder
if len(species_list) > 1:
    for s in species_list:
        s_count = 1
        with open(os.path.join(input_directory, data_file)) as species_csv:
            for row in csv.reader(species_csv):
                if row[0] == s:
                    if s_count == 1:
                        file = open(os.path.join(input_directory, "temporary_files", str(s.replace(" ", "_")) + ".csv"), "w")
                        file.write(header_line)
                        s_count = 0
                    #make well formatted line
                    file.write(",".join(row))
                    file.write("\n")
        file.close()


# Setting the file paths to extract data from .csv files in temporary folder and moving them to the output file path
os.chdir(os.path.join(input_directory, "temporary_files"))
arcpy.env.workspace = os.path.join(input_directory, "output_files")
species_file_list = glob.glob("*.csv")

count = 0
# Converting .csv files into shapefiles that will go into my output file path

for species_file in species_file_list:
    print(".. Processing: " + str(species_file) + " by converting to shapefile format")
    in_Table = species_file
    x_coords = "longitude"
    y_coords = "latitude"
    z_coords = ""
    out_Layer = "species" + str(count)
    saved_Layer = species_file.replace(".csv", "") + ".shp"

    # Setting the spatial reference
    spRef = arcpy.SpatialReference(4326)  # 4326 == WGS 1984

    lyr = arcpy.MakeXYEventLayer_management(in_Table, x_coords, y_coords, out_Layer, spRef, z_coords)
    arcpy.CopyFeatures_management(lyr, saved_Layer)
    count = count + 1
    arcpy.Delete_management(lyr)
    if arcpy.Exists(saved_Layer):
        print("Created species shapefiles successfully!")
#
    # Converting species shapefiles into fishnets that will go into my output file path

    print(".. Processing: " + " species shapefiles by converting to fishnet format")

    desc = arcpy.Describe(species_file.replace(".csv", "") + ".shp")
    XMin = desc.extent.XMin
    XMax = desc.extent.XMax
    YMin = desc.extent.YMin
    YMax = desc.extent.YMax

    # Designating the spatial reference
    arcpy.env.outputCoordinateSystem = arcpy.SpatialReference(4326)

    outFeatureClass = species_file.replace(".csv", "") +"_Fishnet.shp"

    # Setting the origin of the fishnet
    originCoordinate = str(XMin) + " " + str(YMin)
    yAxisCoordinate = str(XMin) + " " + str(YMin + 1)
    cellSizeWidth = "0.75"
    cellSizeHeight = "0.75"
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
        print("Created species fishnet file successfully!")

    # Converting species fishnets into heatmaps that will go into my output file path

    print(".. Processing: " + " species fishnets by converting to heat map format")
    target_features = species_file.replace(".csv", "") +"_Fishnet.shp"
    join_features = species_file.replace(".csv", "") + ".shp"
    out_feature_class = species_file.replace(".csv", "") + "_HeatMap.shp"
    join_operation = "JOIN_ONE_TO_ONE"
    join_type = "KEEP_ALL"
    field_mapping = ""
    match_option = "INTERSECT"
    search_radius = ""
    distance_field_name = ""

    arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class,
                               join_operation, join_type, field_mapping, match_option,
                               search_radius, distance_field_name)
    # Cleaning up data in my file paths
    if arcpy.Exists(out_feature_class):
        print("Created heatmap file successfully!")
        arcpy.Delete_management(target_features)
        arcpy.Delete_management(join_features)
arcpy.Delete_management(os.path.join(input_directory, "temporary_files"))
#
