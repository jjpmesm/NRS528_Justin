# For this coding challenge, I want you to find a particular tool that you like in arcpy. It could be a tool that you
# have used in GIS before or something new. Try browsing the full tool list to get some insight here (click Tool
# Reference on the menu list to the left).
# Set up the tool to run in Python, add some useful comments, and importantly, provide some example data in your repository
# (try to make it open source, such as Open Streetmap, or RI GIS. You can add it as a zip file to your repository.
# My only requirements are:

# Comment your code well.
import arcpy
arcpy.env.workspace = r"C:\NRS_528\Coding_Challenges\NRS528_Justin\challenge4"

# I'll be using the natural heritage areas 2021 dataset from RIGIS for this coding challenge
# describing data:
desc_data = arcpy.Describe(
    "RI_Natural_Heritage_Area_Dec2021.shp")

# Dataset Type:
print("Dataset type: %s" % desc_data.datasetType)

# Spatial Reference Name, Type and Unit:
print("Spatial Reference Name: %s" % desc_data.spatialReference.name)
print("Spatial Reference Type: %s" % desc_data.spatialReference.type)
print("Spatial Unit: %s" % desc_data.spatialReference.linearUnitName)

# min Y and max Y extent:
print("Extent:\n  YMin: {0},\n YMax: {1}".format(desc_data.extent.YMin, desc_data.extent.YMax))

# Broken down Feature to Class tool:
in_features = "RI_Natural_Heritage_Area_Dec2021.shp"
out_feature_class = "points.shp"
point_location = 'CENTROID'
arcpy.FeatureToPoint_management(in_features, out_feature_class, point_location)