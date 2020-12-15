# IMDI Maker
**Author:** Richard Griscom

**Description**: This script takes three CSV files as input: 1) session metadata, 2) project metadata, and 3) speaker metadata. The script lets the user specify the column name that corresponds to each of the required fields in a form. The script then compiles the information from the two spreadsheets and produces IMDI files according to the standards requested by the Endangered Languages Archive (ELAR) for each bundle. This is useful for linguists who are using the [ODK Metadata Method](https://zenodo.org/record/3871516) to create linguistic metadata during fieldwork. 

**Citation:**
Griscom, Richard T. 2020. *IMDI Maker*. DOI: 10.5281/zenodo.4308936 

**Dependencies**
[pandas](https://pandas.pydata.org/)

**Data Preparation**
Metadata must be formatted according to the provided templates, and divided according to project, recording/session, and particpant/speaker metadata. This allows the script to identify values within each table and combine them together to produce the XML output. Filenames for resource files should be identical to the corresponding value of the *name* column in the recording metadata.

**Using the script**
Download the script and place it in the same folder as the metadata files. [Python](https://www.python.org/) and [pandas](https://pandas.pydata.org/) must be installed in order to successfully run the script. 





