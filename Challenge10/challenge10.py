# For this challenge, I have data folders of Landsat imagery from different months and their spectral bands.
# For this coding challenge, I extracted the .tif files of each month and their spectral bands in a list.
# I then use a raster calculator to calculate the NDVI of each month: ((B5-B4)/(B5+B4))

import arcpy, os
arcpy.env.overwriteOutput = True

# Cleaning up and creating the list of spectral bands from each month:
listMonths = ["02", "04", "05", "07", "10", "11"]
for month in listMonths:
    arcpy.env.workspace = r"C:\NRS_528\Coding_Challenges\NRS528_Justin\Challenge10\2015" + month
    outputDirectory = r"NDVI"
    if not os.path.exists(outputDirectory):
        os.mkdir(outputDirectory)
    listRasters = arcpy.ListRasters("LC*", "TIF")

    # Removing _BQA.tif files from months:
    listRasters = [x for x in listRasters if "_BQA.tif" not in x]

    # Sorting the spectral bands of each month in ascending order:
    noExtensionlistRasters = [os.path.splitext(x)[0] for x in listRasters]
    sorted_listRasters = sorted(noExtensionlistRasters, key=lambda x:int(x[42:]))
    sorted_listRasters = [x + ".tif" for x in sorted_listRasters]
    print("Spectral bands of month " + month + ": "+ str(sorted_listRasters))

    # My attempt at calculating the NDVI from the raster calculator copied script that I'm having issues with.
    outRaster = (sorted_listRasters("B5") - sorted_listRasters("B4")) / (sorted_listRasters("B5") + sorted_listRasters("B4"))
    os.path.join(outputDirectory, "NDVI" + month + ".tif")
