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

`Firefox <https://www.mozilla.org/en-US/firefox/new/>`_ is the recommended web browser for reaping the best performance of CyberGIS-Vis.

Getting Started
------------------------------------------------------
You can run CyberGIS-Vis in your Jupyter Notebook installed on your PC as well as in CybearGISX. We recommend that you use CyberGISX because all the required packages have been integrated in CyberGISX.


1. Running in CyberGISX (Temporarily Unavailable)
------------------------------------------------------
To use it in CyberGISX, follow steps below:

If you do not have a CyerGISX account, create a CyberGISX account with your GitHub id at https://cybergisxhub.cigi.illinois.edu

Open up the CyberGIX, click the "new" button on the top right corner, and select python3 and enter the command line below to download CyberGIS-Vis.::

  !git clone https://github.com/cybergis/CyberGIS-Vis

Open Jupyter notebook below and run.::

  Quantitative_Data_Vis/Adaptive_Chropleth_Mapper.ipynb
  Categorical_Data_Vis/Qualitative_Analysis_Mapper.ipynb


2. Running in Local Environment
------------------------------------------------------
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

Comment out like below. These are related to create URLs in the Jupyter Server.::

  #from notebook import notebookapp
  #servers = list(notebookapp.list_running_servers())
  #servers1 = 'https://cybergisx.cigi.illinois.edu'+servers[0]["base_url"]+ 'view'
  #servers2 = 'https://cybergisx.cigi.illinois.edu'+servers[0]["base_url"]+ 'edit'
  #local_dir1 = servers1 + cwd + '/'
  #local_dir2 = servers2 + cwd + '/'

Open Jupyter notebook below and run.::

  Quantitative_Data_Vis/Adaptive_Chropleth_Mapper.ipynb
  Categorical_Data_Vis/Qualitative_Analysis_Mapper.ipynb

iframe test
--------------------
.. raw:: html

  <iframe src="http://su-gis.iptime.org/VNE/Chicago/index.html" width=100% height="402">iframe show up?</iframe>


.. toctree::
  :maxdepth: 3
  :caption: Contents

  CyberGISX
  QuantDataVis
  CatDataVis



Contents
-------------------
* :ref:`modindex`
* :ref:`search`
