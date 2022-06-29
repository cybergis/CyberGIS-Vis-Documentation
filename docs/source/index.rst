.. CyberGIS-Vis-Documentation documentation master file, created by
   sphinx-quickstart on Wed Mar  2 16:56:18 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

CyberGIS-Vis-Documentation
======================================================
**CyberGIS-Vis is an open-source software tool for interactive geospatial visualization and scalable visual analytics.**

CyberGIS-Vis integrates cutting-edge cyberGIS and online visualization capabilities into a suite of software modules for visualization and visual analytical approaches to knowledge discovery based on geospatial data.
Key features of the current CyberGIS-Vis implementation include:

* comparative visualization of spatiotemporal patterns through choropleth maps
* dynamic cartographic mapping linked with charts to explore high-dimensional data
* reproducible visual analytics through integration with CyberGIS-Jupyter
* multi-language support including both Python and Javascript

'Firefox <https://www.mozilla.org/en-US/firefox/new/>'_ is the recommended web browser for reaping the best performance of CyberGIS-Vis.

Getting Started
------------------------------------------------------
You can run CyberGIS-Vis in your Jupyter Notebook installed on your PC as well as in CybearGISX. We recommend that you use CyberGISX because all the required packages have been integrated in CyberGISX.

=====================================================
Running in CyberGISX (Temporarily Unavailable)
=====================================================
To use it in CyberGISX, follow steps below:

If you do not have a CyerGISX account, create a CyberGISX account with your GitHub id at https://cybergisxhub.cigi.illinois.edu

Open up the CyberGIX, click the "new" button on the top right corner, and select python3 and enter the command line below to download CyberGIS-Vis.::

  !git clone https://github.com/cybergis/CyberGIS-Vis

Open Jupyter notebook below and run.::

  Quantitative_Data_Vis/Adaptive_Chropleth_Mapper.ipynb
  Categorical_Data_Vis/Qualitative_Analysis_Mapper.ipynb

=====================================================
Running in Local Environment
=====================================================
To run in a local environment, follow steps below.

Download and install Anaconda at https://www.anaconda.com/.

After installation is done, open "Anaconda Prompt" and enter command lines below to create an environment.::

  conda create -n geo-env -c conda-forge geopandas
  conda activate geo-env
  conda install -c conda-forge jupyterlab
  jupyter lab

Open Python Script below.::

  Quantitative_Data_Vis/Adaptive_Chropleth_Mapper.py
  Categorical_Data_Vis/Qualitative_Analysis_Mapper.py

Comment and uncomment like below. These are related to create URLs in the Jupyter Server.::

  #from notebook import notebookapp
  #servers = list(notebookapp.list_running_servers())
  #servers1 = 'https://cybergisx.cigi.illinois.edu'+servers[0]["base_url"]+ 'view'
  #servers2 = 'https://cybergisx.cigi.illinois.edu'+servers[0]["base_url"]+ 'edit'
  local_dir1 = cwd
  local_dir2 = cwd
  #local_dir1 = servers1 + cwd + '/'
  #local_dir2 = servers2 + cwd + '/'

Open Jupyter notebook below and run.::

  Quantitative_Data_Vis/Adaptive_Chropleth_Mapper.ipynb
  Categorical_Data_Vis/Qualitative_Analysis_Mapper.ipynb


Data
-------

Visualizations created by CyberGIS-Vis are using a small subset of 'LTDB <https://s4.ad.brown.edu/projects/diversity/researcher/LTDB.htm>'_.
'LTDB <https://s4.ad.brown.edu/projects/diversity/researcher/LTDB.htm>'_ provides socioeconomic and demographic data with harmonized boundaries from 1970 to 2010 decennially.
If you need the entire dataset, visit 'this website <https://s4.ad.brown.edu/projects/diversity/researcher/LTDB.htm>'_ to download.


Related Resources
------------------

* 'CyberGISX <https://cybergisxhub.cigi.illinois.edu/>'_
* 'Leaflet <https://leafletjs.com/>'_
* 'PlotlyJS <https://plot.ly/javascript/>'_
* 'D3 <https://d3js.org/>'_
* 'GEOSNAP VIZ <https://github.com/spatialucr/geosnap-viz>'_

Contributors
-----------------
The lead developer of CyberGIS-Vis is Dr. Su Yeon Han at the 'CyberGIS Center for Advanced Digital and Spatial Studies (CyberGIS Center) <https://cybergis.illinois.edu/>'_
and the Principal Investigator of CyberGIS-Vis is Dr. Shaowen Wang at CyberGIS Center.
This software repository is primarily maintained by CyberGIS Center. Please email any questions to help@cybergis.org.

License
---------------
This project is licensed under the Apache License 2.0 - see the 'LICENSE <https://github.com/cybergis/CyberGIS-Vis/blob/master/LICENSE>'_ file for details.

Funding
---------------
The CyberGIS-Vis project is supported by the CyberGIS Center for Advanced Digital and Spatial Studies at the University of Illinois at Urbana-Champaign.

iframe test
--------------------
.. raw:: html

  <iframe src="http://su-gis.iptime.org/VNE/Chicago/index.html" width=100% height="402">iframe show up?</iframe>

.. table of contents
.. --------------------------------------------
.. toctree::
  :maxdepth: 2
  :hidden:
  :caption: Quick Start

  CyberGISX

.. toctree::
  :maxdepth: 3
  :hidden:
  :caption: Visualization Modules

  QuantDataVis
  CatDataVis
  Adaptive_Chropleth_Mapper

.. toctree::
  :hidden:
  :maxdepth: 1
  :caption: Additional Resources

  GitHub Repository <https://github.com/cybergis/CyberGIS-Vis>

.. Contents
.. -------------------
.. * :ref:`modindex`
.. * :ref:`search`
