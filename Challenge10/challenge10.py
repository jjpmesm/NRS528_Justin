# For this challenge, I have data folders of Landsat imagery from different months and their spectral bands.
# For this coding challenge, I extracted the .tif files of each month and their spectral bands in a list.
# The next step is to calculate the NDVI of each month by using the appropriate bands: ((B5-B4)/(B5+B4)).
# Example input data is too large to upload, please download .zip file from the challenge 10 assignment folder!
# Only line 14 needs to be changed.
#
import arcpy, os
from arcpy.sa import *
arcpy.env.overwriteOutput = True

# Cleaning up and creating the list of spectral bands from each month:
listMonths = ["02", "04", "05", "07", "10", "11"]
for month in listMonths:
    arcpy.env.workspace = r"C:\NRS_528\Coding_Challenges\NRS528_Justin\Challenge10\2015\2015" + month
    outputDirectory = r"NDVI"
    if not os.path.exists(outputDirectory):
        os.mkdir(outputDirectory)
    listRasters = arcpy.ListRasters("LC*", "TIF")

# Removing "_BQA.tif" files from the months:
    listRasters = [x for x in listRasters if "_BQA.tif" not in x]

# Sorting the spectral bands of each month in ascending order:
    noExtensionlistRasters = [os.path.splitext(x)[0] for x in listRasters]
    sorted_listRasters = sorted(noExtensionlistRasters, key=lambda x:int(x[42:]))
    sorted_listRasters = [x + ".tif" for x in sorted_listRasters]
    print("Spectral bands of month " + month + ": "+ str(sorted_listRasters))

# Identifying and labeling the spectral bands that will be used to calculate the NDVI for each month:
    B4 = Raster(sorted_listRasters[3])
    B5 = Raster(sorted_listRasters[4])

# Calculating the NDVI for each month with the bands I identified:
    outRaster = (B5 - B4) / (B5 + B4)
    print("Calculating NDVI for month " + month + "...")

# Creating the .tif files for the NDVI and saving them to my output directory:
    outfile = os.path.join(outputDirectory, "NDVI" + month + ".tif")
    outRaster.save(outfile)
    if arcpy.Exists(outfile):
        print("Created NDVI" + month + " file successfully!")