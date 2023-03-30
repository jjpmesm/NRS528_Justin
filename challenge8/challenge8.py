# For this coding challenge, I'll be using the code from challenge #4 to turn it into a function.
# Only change code on line 6 for file path.

import arcpy
arcpy.env.overwriteOutput = True
arcpy.env.workspace = r"C:\NRS_528\Coding_Challenges\NRS528_Justin\challenge8\data"

# The function below describes the input polygon dataset:
def describe_shp(input_shapefile1):

    if arcpy.Exists(input_shapefile1):
        desc = arcpy.Describe(input_shapefile1)
        print("Describing: " + str(input_shapefile1))
        if desc.dataType == "ShapeFile":
            shapetype = desc.shapeType
            spreftype = desc.spatialReference.type
            sprefname = desc.spatialReference.name
            print("Feature Type:  " + shapetype)
            print("Coordinate System Type:  " + spreftype)
            print("Coordinate System Used:  " + sprefname)
        else:
            print("Input data not ShapeFile..")
        print(str(input_shapefile1) + " described!")
    else:
        print("Dataset not found, please check the file path..")

    return shapetype, sprefname, spreftype

input_shapefile1 = r"RI_Natural_Heritage_Area_Dec2021.shp"
shapetype, sprefname, spreftype = describe_shp(input_shapefile1)


# This next function generates the point dataset from the input polygon data using the Feature to Point tool.
def poly_to_point(input_shapefile2):
    print("Converting polygons to points...")
    if arcpy.Exists(input_shapefile2):
        in_features = input_shapefile2
        out_feature_class = "points.shp"
        point_location = 'CENTROID'
        arcpy.FeatureToPoint_management(in_features, out_feature_class, point_location)
        if arcpy.Exists(out_feature_class):
            print("Point shapefile created successfully!")
    else:
        print("Dataset not found, please check the file path..")

    return in_features, out_feature_class, point_location

input_shapefile2 = r"RI_Natural_Heritage_Area_Dec2021.shp"
in_features, out_feature_class, point_location = poly_to_point(input_shapefile2)