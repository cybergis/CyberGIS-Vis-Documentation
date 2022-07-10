# CyberGIS-Vis-Documentation

This repository holds all Read the Docs & Sphinx codes and images for the CyberGIS-Vis technical documentation.
- [CyberGIS-Vis GitHub Repository](https://github.com/cybergis/CyberGIS-Vis)
- [CyberGIS-Vis Documentation Website](https://cybergis.github.io/CyberGIS-Vis-Documentation/)

# For editing: 
The documentation in this repo is created using [sphinx-doc](https://www.sphinx-doc.org/en/master/). The information below are the guide to edit the content of the documentation. 


The source code for this documentation are in [docs/source/](https://github.com/cybergis/CyberGIS-Vis-Documentation/tree/gh-pages/docs/source) folder. The folder content are as follows:

### Folders:
**_static**: contains all statics resources such as the images, video, etc. To reference to the resources in the template just put the resource in this folder and use the path "_static/\<resource file name\>"

### Page templates 

**index.rst**: template for the [index page](https://cybergis.github.io/CyberGIS-Vis-Documentation/) of the documentation  
**CyberGISX.rst**: template of the [Getting Start with CyberGISX](https://cybergis.github.io/CyberGIS-Vis-Documentation/build/CyberGISX.html) page  
**QuanData.rst**: template of the [quantification data visualization](https://cybergis.github.io/CyberGIS-Vis-Documentation/build/QuantDataVis.html) page  
**CatDataVis.rst**: template of the [categorical data visualization](https://cybergis.github.io/CyberGIS-Vis-Documentation/build/CatDataVis.html) page  
**Example.rst**: template of the [Example Code](https://cybergis.github.io/CyberGIS-Vis-Documentation/build/QuantDataVis.html) page  

### Configurations 

**conf.py**: sphinx configurations file.   
**requirements.txt**: the required libraries for sphinx to build the documents. This can be used to create the environment for sphinx-doc using "pip install -r requirements.txt"  

# To update documentation content 

## Preapre the enviroenment
1. Clone the repo. 
2. With command line, go to "./docs/source/"
3. run the command below 

`pip install -r requirements.txt`

4. Go back to "./docs/" folder
5. test your sphinx with the command below. 

`sphinx-build -ab html ./source ./build`

You should see the results like: 

> The HTML pages are in build.

## edit the page content 

1. Open the template of the page that you want the edit. 
    

