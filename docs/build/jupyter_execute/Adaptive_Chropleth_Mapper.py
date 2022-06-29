#!/usr/bin/env python
# coding: utf-8

# # Example Visualizations using CyberGIS-Vis

# ### Documentations and Demos about CyberGIS-Vis are available at: https://github.com/cybergis/CyberGIS-Vis

# ## Setup environment

# In[1]:


import pandas as pd
import geopandas as gpd
from Adaptive_Choropleth_Mapper import Adaptive_Choropleth_Mapper_viz, Adaptive_Choropleth_Mapper_log


# ## Visualizations for Exploring Relationship between data

# ### Set input data: Socioeconomic and Demographic Data from LTDB

# In[2]:


input_attributes = pd.read_csv("attributes/Los_Angeles_1980_1990_2000_2010.csv", dtype={'geoid':str})
input_attributes = input_attributes.rename(columns={'geoid': 'geoid', 'year': 'period'})
input_attributes


# In[3]:


shapefile = gpd.read_file("shp/Los_Angeles_tract/Los_Angeles_2.shp")
shapefile = shapefile.rename(columns={'tractID': 'geoid', 'tract_key': 'name'})
shapefile


# ### Adaptive Choropleth Mapper with Scatter Plot

# In[4]:


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
    'Scatter_Plot': True,        
} 
Adaptive_Choropleth_Mapper_viz(param_Scatter)
Adaptive_Choropleth_Mapper_log(param_Scatter) 


# ### Adaptive Choropleth Mapper with Correlogram

# In[5]:


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
    'Correlogram': True,        
} 
Adaptive_Choropleth_Mapper_viz(param_Correlogram)
Adaptive_Choropleth_Mapper_log(param_Correlogram)  


# ### Adaptive Choropleth Mapper with Parallel Coordinate Plot (PCP) to visulize relationship between variables.

# In[6]:


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
    'NumOfMaps':4,
    'Map_width':"350px",
    'Map_height':"350px", 
    'Top10_Chart': True,    
    'Parallel_Coordinates_Plot': True,
    'NumOfPCP':4,
    'InitialVariablePCP': ["2010_% white (non-Hispanic)", "2010_% black (non-Hispanic)", "2010_% Hispanic", "2010_% Asian & PI race", "2010_% professional employees", "2010_% manufacturing employees", "2010_% in poverty", "2010_% foreign born", "2010_% 17 and under (total)", "2010_% 60 and older"]
}
Adaptive_Choropleth_Mapper_viz(param_PCP)
Adaptive_Choropleth_Mapper_log(param_PCP)  


# ### Adaptive Choropleth Mapper with Stacked Chart

# In[7]:


param_Stacked = {
    'title': "Adaptive Choropleth Mapper with Stacked Chart",
    'filename_suffix': "LA_Stacked",
    'inputCSV': input_attributes,   
    'shapefile': shapefile,
    'periods': [1980, 1990, 2000, 2010],
    'NumOfMaps': 4,
    'shortLabelCSV': "attributes/LTDB_ShortLabel.csv",       
    'variables': [         #enter variable names of the column you entered above.
            "p_nonhisp_white_persons",
    ],
    'Map_width':"350px",
    'Map_height':"350px",    
    'Stacked_Chart': True,  #Comment out if you do not want to visualize this chart       
}  
Adaptive_Choropleth_Mapper_viz(param_Stacked)
Adaptive_Choropleth_Mapper_log(param_Stacked)


# ### Adaptive Choropleth Mapper with Top 10 Bar Chart

# In[8]:


param_bar = {
    'title': "Adaptive Choropleth Mapper with Stacked Chart",
    'filename_suffix': "LA_bar",
    'inputCSV': input_attributes,   
    'shapefile': shapefile,
    'periods': [1980, 1990, 2000, 2010],
    'NumOfMaps': 3,
    'shortLabelCSV': "attributes/LTDB_ShortLabel.csv",      
    'variables': [         #enter variable names of the column you entered above.           
        "p_other_language",
        "p_female_headed_families",
        "per_capita_income",     
    ],
    'Top10_Chart': True,  #Comment out if you do not want to visualize this chart      
}  
Adaptive_Choropleth_Mapper_viz(param_bar)
Adaptive_Choropleth_Mapper_log(param_bar)


# ## Visualizations for Spatiotemporal Data

# ### Set input data: COVID-19 data and the number of visits estimated based on Twitter data

# In[9]:


Covid_Visits = pd.read_csv("attributes/Covid_Visits.csv", dtype={'geoid':str})
Covid_Visits = Covid_Visits.rename(columns={'geoid': 'geoid'})
Covid_Visits


# In[10]:


shapefile_MSA = gpd.read_file("shp/MSA_country/msa_country.shp", dtype={'GEOID':str})
shapefile_MSA = shapefile_MSA.rename(columns={'GEOID': 'geoid', 'NAME_1':'name'})
shapefile_MSA


# ### Adaptive Choropleth Mapper with Multiple Line Chart (MLC)

# In[11]:


param_MLC_COVID = {
    'title': "Covid-19 Risk Assessment using Twitter, Metropolitan Statistical Areas, USA",
    'Subject': "Temporal Patterns",
    'filename_suffix': "COVID_MLC",  # max 30 character      
    'inputCSV': Covid_Visits,   
    'shapefile': shapefile_MSA, 
    'periods': "All",
    'variables': [         #enter variable names of the column you entered above.
            "Confirmed Rate",
            "Death Rate",
            "The Number of Visits from Outside to Inside of the selected MSA"
        ],
    'NumOfMaps':2,
    'InitialLayers':["2020-03-15_Confirmed Rate" , "2020-12-27_Confirmed Rate"],
    'Initial_map_center':[37, -97],
    'Initial_map_zoom_level':4,    
    'Map_width':"650px",
    'Map_height':"400px", 
    'Top10_Chart': True,     
    'Multiple_Line_Chart': True,
    'NumOfMLC':3,
    'titlesOfMLC':["1. COVID-19 Confirmed Cases (/100k pop)", "2. COVID-19 Death Cases (/100k pop)", "3. The Number of Visits from Outside to Inside of the selected MSA"],
    'DefaultRegion_MLC':"35620" 
}
Adaptive_Choropleth_Mapper_viz(param_MLC_COVID)
Adaptive_Choropleth_Mapper_log(param_MLC_COVID)


# ### Adaptive Choropleth Mapper with Comparison Line Chart (CLC)

# In[12]:


param_CLC_COVID = {
    'title': "Comparison of COVID-19 Confirmed Rate between Metropolitan Statistical Areas, USA",
    'Subject': "Temporal Patterns",
    'filename_suffix': "COVID_CLC",                                      # max 30 character      
    'inputCSV': Covid_Visits,   
    'shapefile': shapefile_MSA, 
    'periods': "All",
    'variables': [         #enter variable names of the column you entered above.
            "Confirmed Rate"
        ],
    'NumOfMaps':2,
    'InitialLayers':["2020-04-19_Confirmed Rate" , "2020-11-01_Confirmed Rate"],
    'Initial_map_center':[37, -97],
    'Initial_map_zoom_level':4,    
    'Map_width':"650px",
    'Map_height':"400px",     
    'Top10_Chart': True,     
    'Comparision_Chart': True,
    'NumOfCLC': 46,
    'DefaultRegion_CLC': ["35620", "16980"] 
}
Adaptive_Choropleth_Mapper_viz(param_CLC_COVID)
Adaptive_Choropleth_Mapper_log(param_CLC_COVID)  


# ## More Examples

# ### Set input data: HIV data

# In[5]:


input_attributes_hiv = pd.read_csv("attributes/HIV_US_multiple_long.csv", dtype={'geoid':str})
input_attributes_hiv = input_attributes_hiv.rename(columns={'geoid': 'geoid'})
input_attributes_hiv


# In[6]:


shapefile_us = gpd.read_file("shp/US/counties.shp")
shapefile_us


# ### Adaptive Choropleth Mapper with Parallel Coordinate Plot (PCP) for Time Series Visualization

# In[15]:


param_PCP_hiv = {
    'title': "Adaptive Choropleth Mapper with Paralle Coordinate Plot",
    'filename_suffix': "HIV_PCP",                                      # max 30 character     
    'inputCSV': input_attributes_hiv,   
    'shapefile': shapefile_us, 
    'periods': [2012, 2013, 2014, 2015, 2016, 2017, 2018],
    'variables': [         #enter variable names of the column you entered above.
            "HIV",
            #"Health Care Center (/100k pop)"
        ],
    'NumOfMaps':2,
    'Initial_map_center':[37, -97],
    'Initial_map_zoom_level':4,    
    'Map_width':"650px",
    'Map_height':"410px",     
    'Top10_Chart': True,    
    'Parallel_Coordinates_Plot': True,
    'NumOfPCP':7,
}
Adaptive_Choropleth_Mapper_viz(param_PCP_hiv)
Adaptive_Choropleth_Mapper_log(param_PCP_hiv)  


# In[ ]:




