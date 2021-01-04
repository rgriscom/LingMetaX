# LingMetaX
**Author:** Richard Griscom

**Description**: This script converts linguistic metadata from a .csv format produced by [KoBoToolbox](https://www.kobotoolbox.org/) to the XML format used by [the Lameta linguistic metadata editor](https://sites.google.com/site/metadatatooldiscussion/). This is useful for linguists who are using the [ODK Metadata Method](https://zenodo.org/record/3871516) to create linguistic metadata during fieldwork. 

The script is available in two versions: 
* Google Colab Notebook - 
* Python Script - This version must be downloaded and run on your own computer. You must have Python and the pandas library installed. 

**Citation:**
Griscom, Richard T. 2020. *LingMetaX*. https://github.com/rgriscom/LingMetaX/

**Dependencies:** 
[pandas](https://pandas.pydata.org/)

**Data Preparation:** 
Metadata must be formatted according to the provided templates, and divided according to project, recording/session, and particpant/speaker metadata. This allows the script to identify values within each table and combine them together to produce the XML output. Filenames for resource files should be identical to the corresponding value of the *name* column in the recording metadata.

**Using the script:**
Download the script and place it in the same folder as the metadata files, and either in the same folder as the resource files or in the parent folder of the folders which contain the resource files. [Python](https://www.python.org/) and [pandas](https://pandas.pydata.org/) must be installed in order to successfully run the script. 





