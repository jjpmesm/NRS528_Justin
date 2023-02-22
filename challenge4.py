# For this coding challenge, I want you to find a particular tool that you like in arcpy. It could be a tool that you have used in GIS
# before or something new. Try browsing the full tool list to get some insight here (click Tool Reference on the menu list to the left).

# Set up the tool to run in Python, add some useful comments, and importantly, provide some example data in your repository
# (try to make it open source, such as Open Streetmap, or RI GIS. You can add it as a zip file to your repository.

# My only requirements are:

# Comment your code well.
import arcpy

# I'll be using the natural heritage areas 2021 dataset from RIGIS for this coding challenge
# describing data:
desc_data = arcpy.Describe(r"C:\NRS_528\challenge4_data\natural_heritage_areas_2021\RI_Natural_Heritage_Area_Dec2021.shp")

# Dataset Type:
print("Dataset type: %s" % desc_data.datasetType)

# Spatial Reference Name, Type and Unit:
print("Spatial Reference Name: %s" %  desc_data.spatialReference.name)
print("Spatial Reference Type: %s" % desc_data.spatialReference.type)
print("Spatial Unit: %s" % desc_data.spatialReference.linearUnitName)

# min Y and max Y extent:
print("Extent:\n  YMin: {0},\n YMax: {1}".format(desc_data.extent.YMin, desc_data.extent.YMax))

# Ensure that the code will run on my machine with only a single change to a single variable (i.e. a base folder location).
#
# I'll be using the "Feature to Point" tool to convert the polygons of the natural heritage areas into point feature classes.

# I find this tool to be a helpful solution to problems with other tools such as using euclidean distance.

# More specifically, I find this tool very helpful when the euclidean distance tool has problems when it's missing distance values from cretain polygons.

# This tool can help solve this issue by now including the distance of points that were formally polygons that were missing those distance values.

# The CENTROID input places the points in the direct center of the polygons.

# Tool syntax: FeatureToPoint_management(in_features, out_feature_class, {point_location})

# Broken down Feature to Class tool:

in_features = r"C:\NRS_528\challenge4_data\natural_heritage_areas_2021\RI_Natural_Heritage_Area_Dec2021.shp"
out_feature_class = r"C:\NRS_528\challenge4_data\natural_heritage_areas_2021\points.shp"
point_location = 'CENTROID'
arcpy.FeatureToPoint_management(in_features, out_feature_class, point_location)
