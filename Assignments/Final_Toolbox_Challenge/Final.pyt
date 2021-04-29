# In your final assignment for this course, you should create a Python Toolbox that contains a minimum of three simple tools for undertaking geoprocessing and file management operations.
# These tools can be discrete or part of a larger workflow. However, the caveats are that you should create a "single file" toolbox (no includes, or external file tools)
# and you should aim to not exceed 2000 lines of code in its entirety (but if you do, no worries).
# You should document the toolbox using Github README.md and provide example data for running each of your tools. Grading and feedback will focus on:
#     1) Does the toolbox install, and the tools run successfully?
#     2) cleanliness of code,
#     3) functionality and depth of processing operation, and
#     4) appropriate use of documentation. Plus,
#     5) provide example data that allows me to test your tools.


# This study is a mapping for suitable houses based on the following criteria.
# 1 Within 100 meters to the major roads
# 2 Housing prices are below 1,000,000




import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Python Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [XY_Table_To_Point, Buffer, Intersect, Select]

# Display housing locations on the map using coordinates in the csv file

class XY_Table_To_Point(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "XY_Table_To_Point tool"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        in_table = arcpy.Parameter(name="input_table",
                                     displayName="input_table",
                                     datatype="GPTableView",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        in_table.value = r"D:\NRS 528\Final\Data\BI_houses.csv"  # This is a default value that can be over-ridden in the toolbox
        params.append(in_table)

        x_coords = arcpy.Parameter(name="x_coords",
                                        displayName="x_coords",
                                        datatype="Field",
                                        parameterType="Required",  # Required|Optional|Derived
                                        direction="Input",  # Input|Output
                                        )
        x_coords.value = "Longitude"  # This is a default value that can be over-ridden in the toolbox
        params.append(x_coords)

        y_coords = arcpy.Parameter(name="y_coords",
                                        displayName="y_coords",
                                        datatype="Field",
                                        parameterType="Required",  # Required|Optional|Derived
                                        direction="Input",  # Input|Output
                                        )
        y_coords.value = "Latitude"  # This is a default value that can be over-ridden in the toolbox
        params.append(y_coords)



        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="DEFeatureClass",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        output.value = r"D:\NRS 528\Final\Final.gdb\BI_houses"  # This is a default value that can be over-ridden in the toolbox
        params.append(output)
        return params


    def execute(self, parameters, messages):
        """The source code of the tool."""

        in_table = parameters[0].valueAsText
        x_coords = parameters[1].valueAsText
        y_coords = parameters[2].valueAsText
        output = parameters[3].valueAsText
        arcpy.management.XYTableToPoint(in_table,output,x_coords,y_coords)

# Create a buffer zone of roads

class Buffer(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Buffer"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input = arcpy.Parameter(name="input_feature",
                                     displayName="input_feature",
                                     datatype="Shapefile",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input.value = r"D:\NRS 528\Final\Data\BI_roads.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(input)

        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="Shapefile",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        output.value = r"D:\NRS 528\Final\Buffer.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(output)


        buffer_distance= arcpy.Parameter(name="output",
                        displayName="Output",
                        datatype="Linear Unit",
                        parameterType="Required",  # Required|Optional|Derived
                        direction="Output",  # Input|Output
                        )
        buffer_distance.value = 100  # This is a default value that can be over-ridden in the toolbox
        params.append(buffer_distance)
        return params

    def execute(self, parameters, messages):
        """The source code of the tool."""

        input = parameters[0].valueAsText
        output = parameters[1].valueAsText
        buffer_distance=parameters[2].valueAsText
        arcpy.analysis.Buffer(input,output,buffer_distance)

# Intersect houses with the buffer zone

class Intersect(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Intersect"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input1 = arcpy.Parameter(name="input_feature1",
                                     displayName="input_feature1",
                                     datatype="Shapefile",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input1.value = r"D:\NRS 528\Final\Final.gdb\BI_houses"  # This is a default value that can be over-ridden in the toolbox
        params.append(input1)

        input2 = arcpy.Parameter(name="input_feature2",
                                 displayName="input_feature2",
                                 datatype="Shapefile",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Input",  # Input|Output
                                 )
        input2.value = r"D:\NRS 528\Final\Buffer.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(input2)

        output = arcpy.Parameter(name="output",
                                 displayName="Output",
                                 datatype="Shapefile",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="Output",  # Input|Output
                                 )
        output.value = r"D:\NRS 528\Final\intersect.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(output)

        return params

    def execute(self, parameters, messages):
        """The source code of the tool."""

        input1 = parameters[0].valueAsText
        input2 = parameters[1].valueAsText
        output=parameters[2].valueAsText
        arcpy.Intersect_analysis([input1, input2], output)


# Calculate distance to the coast. A new column will add to the attribute table

class Select(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Select"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = []
        input = arcpy.Parameter(name="input_feature",
                                     displayName="input_feature",
                                     datatype="Shapefile",
                                     parameterType="Required",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        input.value = r"D:\NRS 528\Final\intersect.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(input)

        output = arcpy.Parameter(name="output_feature",
                                 displayName="output_feature",
                                 datatype="Shapefile",
                                 parameterType="Required",  # Required|Optional|Derived
                                 direction="output",  # Input|Output
                                 )
        output.value = r"D:\NRS 528\Final\Select.shp"  # This is a default value that can be over-ridden in the toolbox
        params.append(output)

        condition=arcpy.Parameter(name="where_clause",
                                     displayName="where_clause",
                                     datatype="SQL Expression",
                                     parameterType="Optional",  # Required|Optional|Derived
                                     direction="Input",  # Input|Output
                                     )
        condition.value = "Sales_pric < 1000000" # This is a default value that can be over-ridden in the toolbox
        params.append(condition)

        return params

    def execute(self, parameters, messages):
        """The source code of the tool."""

        input = parameters[0].valueAsText
        output = parameters[1].valueAsText
        condition=parameters[2].valueAsText
        arcpy.Select_analysis(input,output,condition)

