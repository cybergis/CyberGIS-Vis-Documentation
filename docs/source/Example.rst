Example Code
===============

.. role:: python(code)
   :language: python

To try our interactive juoyter notebook, please check out our `CyberGIS-Vis notebook <https://cybergisxhub.cigi.illinois.edu/notebook/recent-advances-in-cybergis-viz-for-democratizing-access-to-scalable-geovisualization/>`_ on CyberGISX platform.

Setup Environment
-----------------

.. code-block:: python

        import pandas as pd
        import geopandas as gpd
        from Adaptive_Choropleth_Mapper import Adaptive_Choropleth_Mapper_viz, Adaptive_Choropleth_Mapper_log

Load Data
---------

CyberGIS-Vis requires 2 data files: 
    1. **Attribute data**: your data must contain "geoid" in the first column and the second column must be "period" which is the year of the data. 
    2. **Geometry data**: the geometry data must contain "geoid" in the first column and the second column must be "name" which is the test used to display in the visualization.

Load attribute data from csv file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
        
        #Load attribute data from csv file
        input_attributes = pd.read_csv("attributes/Los_Angeles_1980_1990_2000_2010.csv", dtype={'geoid':str})
        #Change the column name to "geoid" and "period"
        input_attributes = input_attributes.rename(columns={'geoid': 'geoid', 'year': 'period'})

.. image:: _static/attribute_data_table.png
    :height: 400px
    :alt: Attribute data result
    :align: center


Load geometry data from shapefile format
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
        
        #Load geometry from shapefile
        shapefile = gpd.read_file("shp/Los_Angeles_tract/Los_Angeles_2.shp")
        #Change the column name to "geoid" and "name"
        shapefile = shapefile.rename(columns={'tractID': 'geoid', 'tract_key': 'name'})

.. image:: _static/geometry_data_table.png
    :height: 400px
    :alt: geometry data result
    :align: center

Code Samples for the visualization
----------------------------------

1. Adaptive Choropleth Mapper with Scatter Plot
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The chloropleth maps visualize the data of each variable. The data of 2 selected attributes on x-axis and y-axis are visualized in the scatter plot. To show the scatter plot, add the :python:`'Scatter_Plot': True` in the parameter of the :python:`Adaptive_Choropleth_Mapper_viz()`.

.. code-block:: python

        param_Scatter = {
            'title': "Adaptive Choropleth Mapper with Scatter Plot",
            'filename_suffix': "LA_Scatter",
            'inputCSV': input_attributes,   
            'shapefile': shapefile,
            'periods': [2010],
            'shortLabelCSV': "attributes/LTDB_ShortLabel.csv",        
            'variables': [         #enter variable names of the column you entered above.
                "p_nonhisp_white_persons",
                "p_nonhisp_black_persons",
                "p_hispanic_persons",
                "p_asian_persons",
                "p_foreign_born_pop",
                "p_edu_college_greater",
                "p_unemployment_rate",
                "p_employed_manufacturing",
                "p_poverty_rate",
                "p_vacant_housing_units",
                "p_owner_occupied_units",
                "p_housing_units_multiunit_structures",
                "median_home_value",
                "p_structures_30_old",
                "p_household_recent_move",
                "p_persons_under_18",
                "p_persons_over_60",     
            ],
            'InitialLayers':["2010_% edu college greater", "2010_% employed manufacturing" ],
            'Map_width':"470px",
            'Map_height':"450px", 
            'Scatter_Plot': True,  # This is the activate the scatter plot visualization.
        } 
        Adaptive_Choropleth_Mapper_viz(param_Scatter)
        Adaptive_Choropleth_Mapper_log(param_Scatter) 

**Example result**

.. image:: _static/ACM_Scatter.png
    :width: 100%
    :alt: Two chloroplath maps with scatter plot
    :align: center

2. Adaptive Choropleth Mapper with Correlogram
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The chloropleth maps visualize the data of each variable. The correlogram visualizes the scatter plot of all pairs of the selected attributes and the distribution of each selected attributes. To show the scatter plot, add the :python:`'Correlogram': True` in the parameter of the :python:`Adaptive_Choropleth_Mapper_viz()`.

.. code-block:: python

        param_Correlogram = {
            'title': "Adaptive Choropleth Mapper with Correlogram",
            'filename_suffix': "LA_Correlogram",
            'inputCSV': input_attributes,   
            'shapefile': shapefile,
            'NumOfMaps':6,
            'periods': [2010],
            'shortLabelCSV': "attributes/LTDB_ShortLabel.csv",       
            'variables': [         #enter variable names of the column you entered above.
                "p_nonhisp_white_persons",
                "p_nonhisp_black_persons",
                "p_hispanic_persons",
                "p_asian_persons",
                "p_foreign_born_pop",
                "p_edu_college_greater",
                "p_unemployment_rate",
                "p_employed_manufacturing",
                "p_poverty_rate",
                "p_vacant_housing_units",
                "p_owner_occupied_units",
                "p_housing_units_multiunit_structures",
                "median_home_value",
                "p_structures_30_old",
                "p_household_recent_move",
                "p_persons_under_18",
                "p_persons_over_60",     
            ],
            'Map_width':"350px",
            'Map_height':"350px",
            'Correlogram': True, # This is the activate the correlogram visualization.    
        } 
        Adaptive_Choropleth_Mapper_viz(param_Correlogram)
        Adaptive_Choropleth_Mapper_log(param_Correlogram)

**Example result**

.. image:: _static/ACM_Correlogram.png
    :width: 100%
    :alt: four chloroplath maps with correlogram
    :align: center


3. Adaptive Choropleth Mapper with Parallel Coordinate Plot
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The chloropleth maps visualize the data of each variable. The correlogram visualizes the scatter plot of all pairs of the selected attributes and the distribution of each selected attributes. To show the scatter plot, add the :python:`'Correlogram': True` in the parameter of the :python:`Adaptive_Choropleth_Mapper_viz()`.

.. code-block:: python

        param_PCP = {
            'title': "Adaptive Choropleth Mapper with Paralle Coordinate Plot",
            'filename_suffix': "Census_PCP",                                      # max 30 character     
            'inputCSV': input_attributes,   
            'shapefile': shapefile, 
            'periods': [2010],
            'variables': [         #enter variable names of the column you entered above.
                    "p_nonhisp_white_persons",
                    "p_nonhisp_black_persons",
                    "p_hispanic_persons",
                    "p_asian_persons",
                    "p_employed_manufacturing",
                    "p_poverty_rate",
                    "p_foreign_born_pop",
                    "p_persons_under_18",
                    "p_persons_over_60",  
                    "p_edu_college_greater",
                    "p_unemployment_rate",
                    "p_employed_professional",
                    "p_vacant_housing_units",
                    "p_owner_occupied_units",
                    "p_housing_units_multiunit_structures",
                    "median_home_value",
                    "p_structures_30_old",
                    "p_household_recent_move",
            
                ],
            'shortLabelCSV': "attributes/LTDB_ShortLabel.csv",
            'NumOfMaps':4, # Number of chloropleth maps to be displayed.
            'Map_width':"350px",
            'Map_height':"350px",   
            'Parallel_Coordinates_Plot': True,
            'NumOfPCP':6, # number of the attributes to be displayed in the parallel coordinates plot.
            'InitialVariablePCP': ["2010_% white (non-Hispanic)", "2010_% black (non-Hispanic)", "2010_% Hispanic", "2010_% Asian & PI race", "2010_% professional employees", "2010_% manufacturing employees", "2010_% in poverty", "2010_% foreign born", "2010_% 17 and under (total)", "2010_% 60 and older"] # The list of attributes displayed in the parallel coordinates plot.
        }
        Adaptive_Choropleth_Mapper_viz(param_PCP)
        Adaptive_Choropleth_Mapper_log(param_PCP)  

**Example result**

.. image:: _static/ACM_Correlogram.png
    :width: 100%
    :alt: four chloroplath maps with correlogram
    :align: center