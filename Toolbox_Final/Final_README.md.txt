# Final Toolbox Assignment: Finding Historical points in Riparian Buffer Zones in RI

## Background

For my final project, I decided to create a toolbox that gives users the output of finding historical sites that are in riparian buffer zones in the state of RI. This python toolbox contains a total of three tools to help perform the tasks. The all shapefiles used for the inputs are sourced from the RIGIS database. I decided not to rename the input data so users can trace back the data to the online source. The "Streams5k" shapefile shows the statewide data for rivers and streams in RI. The river and streams data is used for creating the riparian buffer zones. Additionally, the "histpnts" shapefile shows statewide point data for historical sites in RI. These historical sites points are used to find which historical sites fall within the buffer zone.

![input_data](https://user-images.githubusercontent.com/123785630/233861071-a9061106-e80a-4899-a03c-d9b6ddefbad0.png)

## Workflow

###### Step 1: Buffer Riparian Zones

For this tool, the rivers and streams shapefile will be the input for creating the riparian buffer zone. You can select your output workspace and designated buffer distance in a linear unit. For example, try 200 US survey feet! This script will make sure the file output was created and also describe some details about your output file.

![Tool_1](https://user-images.githubusercontent.com/123785630/233861098-7abe0bee-0b67-4314-a41c-6038b99ecb4d.png)

###### Step 2: Clean Up Buffers

When you look at the output buffers created by step 1, you may notice overlaps between different riparian buffer zones. This result may look messy for analysis. The purpose of this tool is to use a dissolving effect that combines buffer zones that overlap to create a more presentable riparian buffer zone. The main input for this tool is the original buffer zones created from step 1. This script will make sure the file output was created and also describe some details about your output file. Furthermore, the tool will delete the original riparian buffer zone output from step 1 to clean up the file space and for the final analysis. The tool will also check is the original buffer zone file was actually deleted.

![Tool_2](https://user-images.githubusercontent.com/123785630/233861128-a4c0fab0-ac4a-4acf-b13a-14ef5452f5b9.png)

###### Step 3: Clip Historic Sites in Riparian Zones

The final tool in my toolbox will then clip the statewide historic sites that are inside the riparian buffer zones. The Historical sites are the input points, and the riparian buffer zone output from step 2 is the input clipping buffer. This script will make sure the file output was created and also describe some details about your output file.

![Tool_3](https://user-images.githubusercontent.com/123785630/233861154-13b93e90-1b03-434b-bf51-29c40540dc91.png)

