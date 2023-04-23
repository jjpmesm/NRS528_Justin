# Midterm Assignment: Clipping dam locations to the town of Glocester, RI

## Background

I decided to type up a python script that creates a point shapefile of Rhode Island dam locations from a .csv file that is clipped to the town of Glocester. 

The RI_dams.csv file is sourced from the National Inventory of Dams database. The .csv file was cleaned up outside of python to keep important columns (name, longitude, latitude, etc.)

The towns shapefile is sourced from the RIGIS database.

Arcpy and the csv were imported and the workspace environment was designated.

## Workflow

###### Step 1: .csv file to .shp file

This section of the code creates a point shapefile from the RI_dams.csv file. I counted the number of dams and set the spatial reference for the dataset. I also checked if the point shapefile was created.

###### Step 2: Projecting the RI dams shapefile

Since the towns shape file is projected in Rhode Island State Plane in units of feet, I decided to project the RI dams points into the same coordinate system. This will ensure there's no distortions in my results. I also checked if the projected point shapefile was created.

###### Step 3: Selecting the town of Glocester

I then decided to slect the town of Glocester from the towns shape file. This will extract the town from the dataset into a new shape file. I extracted the town by stating '"NAME" = \'GLOCESTER\'' for the clause to extract it. This will be used for the clip function. I also checked if the selected shapefile was created.

###### Step 4: Clipping the RI dams to the town of Glocester

I then used the selected town of Glocester as the clip feature and the projected RI dams as the input features. I counted the number of dams that were clipped into this town. I also checked if the clipped point shapefile was created.

###### Step 5: Cleaning up the file space

I then cleaned up the file space by deleting the original and projected RI dams point shapefiles, and the selected Glocester shapefile. It should only leave you with the input data (.csv and towns.shp) and the final clipped point dataset.

