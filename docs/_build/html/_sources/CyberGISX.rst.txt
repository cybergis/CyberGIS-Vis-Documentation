Getting Started with CyberGISX
======================================================
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
