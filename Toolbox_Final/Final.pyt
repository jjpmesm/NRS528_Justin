# Justin Purcell, April 28, 2023.
#
# This python toolbox contains a total of three tools. The purpose of these tools is to find historical sites that
# are located within riparian buffer zones.
#
# The "Streams5k" shapefile from the example data shows the statewide data for rivers and streams in RI and is
# sourced from RIGIS. Additionally, the "histpnts" shapefile shows statewide point data for historical sites and is
# also sourced from RIGIS. The river and streams data is used for creating the riparian buffer zones and the historical
# points are used for the final tool to find which historical sites fall within that buffer zone.
#
# The first "Buffer Riparian Zones" tool creates a buffer around the provided rivers and streams shapefile. You can
# set a linear distance and a unit of measurement of your choice. For an example, try 200 US Survey Feet. The only
# input for this tool is the rivers and streams shapefile.
#
# The second "Clean up Buffers" tool cleans up the original buffer zone to create make the riparian zones more
# presentable. The original buffer output from the first tool has multiple overlaps and looks messy. The dissolve
# effect of this second tool merges the overlapping buffers to show more complete riparian buffer zones. The previously
# created buffer output is the only input for this tool. The tool also deletes the original buffer zone file from the
# previous toolbox to clean the file space.
#
# Finally, the "Clip Historical Sites to Riparian Zones" will show the historic site points that are found withing
# the riparian buffer zones. The historical sites points is the input dataset and the dissolved riparian buffer zones
# from the previous tool is the clip feature to get the output points.
#
# Enjoy!

import arcpy

arcpy.env.overwriteOutput = True


# Creating and labeling the toolbox with tools it contains:
class Toolbox(object):
    def __init__(self):
        self.label = "Riparian Zone Toolbox"
        self.alias = ""
        self.tools = [Buffer, Dissolve, Clip]


# Creating and labeling the buffering script:
class Buffer(object):
    def __init__(self):
        self.label = "1. Buffer Riparian Zones"
        self.description = ""
        self.canRunInBackground = False

    # Creating parameters for the buffer script:
    def getParameterInfo(self):
        params = []
        input_line = arcpy.Parameter(name="input_line",
                                     displayName="Input Features",
                                     datatype="Feature Layer",
                                     parameterType="Required",
                                     direction="Input",
                                     )
        params.append(input_line)
        output_Feature_class = arcpy.Parameter(name="out_feature_class",
                                               displayName="Output Buffer",
                                               datatype="DEFeatureClass",
                                               parameterType="Required",
                                               direction="Output",
                                               )
        params.append(output_Feature_class)
        buffer_distance_or_field = arcpy.Parameter(name="buffer_distance",
                                                   displayName="Distance",
                                                   datatype="Linear Unit",
                                                   parameterType="Required",
                                                   direction="Input",
                                                   )
        params.append(buffer_distance_or_field)
        return params

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    # Executing the buffer script:
    def execute(self, parameters, messages):
        input_line = parameters[0].valueAsText
        output_Feature_class = parameters[1].valueAsText
        buffer_distance_or_field = parameters[2].valueAsText
        arcpy.AddMessage("Creating buffers...")
        arcpy.analysis.Buffer(in_features=input_line,
                              out_feature_class=output_Feature_class,
                              buffer_distance_or_field=buffer_distance_or_field,
                              line_side="FULL",
                              line_end_type="ROUND",
                              dissolve_option="NONE",
                              dissolve_field=None,
                              method="PLANAR"
                              )

        # Checking to see if the output exists:
        if arcpy.Exists(output_Feature_class):
            arcpy.AddMessage("Successfully created riparian buffer zones!")

        # Describing the output from this script:
        desc = arcpy.Describe(output_Feature_class)
        arcpy.AddMessage("File Path = " + str(desc.path))
        arcpy.AddMessage("Shape Type = " + str(desc.shapeType))
        arcpy.AddMessage(
            "Extent = XMin: {0}, XMax: {1}, YMin: {2}, YMax: {3}".format(desc.extent.XMin, desc.extent.XMax,
                                                                         desc.extent.YMin, desc.extent.YMax))
        arcpy.AddMessage("Coordinate System name = " + str(desc.spatialReference.name))
        arcpy.AddMessage("Coordinate System type = " + str(desc.spatialReference.type))
        return


# Creating and labeling the dissolve buffers script:
class Dissolve(object):
    def __init__(self):
        self.label = "2. Clean Up Buffers"
        self.description = ""
        self.canRunInBackground = False

    # Creating parameters for the dissolve script:
    def getParameterInfo(self):
        params = []
        input_buffer = arcpy.Parameter(name="input",
                                       displayName="Input Buffer",
                                       datatype="DEFeatureClass",
                                       parameterType="Required",
                                       direction="Input",
                                       )
        params.append(input_buffer)
        output_dissolve = arcpy.Parameter(name="output",
                                          displayName="Output Dissolve",
                                          datatype="DEFeatureClass",
                                          parameterType="Required",
                                          direction="Output",
                                          )
        params.append(output_dissolve)
        return params

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    # Executing the dissolve script:
    def execute(self, parameters, messages):
        input_buffer = parameters[0].valueAsText
        output_dissolve = parameters[1].valueAsText
        arcpy.AddMessage("Running dissolve...")
        arcpy.management.Dissolve(in_features=input_buffer,
                                  out_feature_class=output_dissolve
                                  )

        # Checking to see if the output exists:
        if arcpy.Exists(output_dissolve):
            arcpy.AddMessage("Successfully dissolved riparian buffers!")

        # Describing the output dissolved buffer:
        desc = arcpy.Describe(output_dissolve)
        arcpy.AddMessage("File Path = " + str(desc.path))
        arcpy.AddMessage("Shape Type = " + str(desc.shapeType))
        arcpy.AddMessage(
            "Extent = XMin: {0}, XMax: {1}, YMin: {2}, YMax: {3}".format(desc.extent.XMin, desc.extent.XMax,
                                                                         desc.extent.YMin, desc.extent.YMax))
        arcpy.AddMessage("Coordinate System name = " + str(desc.spatialReference.name))
        arcpy.AddMessage("Coordinate System type = " + str(desc.spatialReference.type))

        # Deleting the input buffer used for the script and checking if it actually deleted, it's no longer needed for
        # the next script:
        arcpy.Delete_management(input_buffer)
        arcpy.AddMessage("Deleting intermediate data...")
        if not arcpy.Exists(input_buffer):
            arcpy.AddMessage("Deleted original riparian buffer file.")
        return


# Clipping points to zones
class Clip(object):
    def __init__(self):
        self.label = "3. Clip Historic Sites in Riparian Zones"
        self.description = ""
        self.canRunInBackground = False

    # Creating parameters for the clip script:
    def getParameterInfo(self):
        params = []
        input_points = arcpy.Parameter(name="input",
                                       displayName="Input Points",
                                       datatype="DEFeatureClass",
                                       parameterType="Required",
                                       direction="Input",
                                       )
        params.append(input_points)
        input_buffer = arcpy.Parameter(name="input_buffer",
                                       displayName="Input Clipping Buffer",
                                       datatype="DEFeatureClass",
                                       parameterType="Required",
                                       direction="Input",
                                       )
        params.append(input_buffer)
        output = arcpy.Parameter(name="output",
                                 displayName="Output Points",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",
                                 direction="Output",
                                 )
        params.append(output)
        return params

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    # Executing the clip script:
    def execute(self, parameters, messages):
        input_points = parameters[0].valueAsText
        input_buffer = parameters[1].valueAsText
        output = parameters[2].valueAsText
        arcpy.AddMessage("Running clip...")
        arcpy.Clip_analysis(in_features=input_points,
                            clip_features=input_buffer,
                            out_feature_class=output,
                            cluster_tolerance="")

        # Checking to see if the output exists:
        if arcpy.Exists(output):
            arcpy.AddMessage("Successfully clipped historical sites to riparian buffer zones!")

        # Describing the clipped points:
        desc = arcpy.Describe(output)
        arcpy.AddMessage("File Path = " + str(desc.path))
        arcpy.AddMessage("Shape Type = " + str(desc.shapeType))
        arcpy.AddMessage(
            "Extent = XMin: {0}, XMax: {1}, YMin: {2}, YMax: {3}".format(desc.extent.XMin, desc.extent.XMax,
                                                                         desc.extent.YMin, desc.extent.YMax))
        arcpy.AddMessage("Coordinate System name = " + str(desc.spatialReference.name))
        arcpy.AddMessage("Coordinate System type = " + str(desc.spatialReference.type))
        return
