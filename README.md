# LingMetaX
**Author:** Richard Griscom

**Description**: This script converts linguistic metadata from a .csv format produced by [KoBoToolbox](https://www.kobotoolbox.org/) to the XML format used by the [Lameta](https://sites.google.com/site/metadatatooldiscussion/) linguistic metadata editor. This is useful for linguists who are using the [ODK Metadata Method](https://zenodo.org/record/3871516) to create linguistic metadata during fieldwork. 

The script is available in two versions: 
* [Google Colab Notebook](https://colab.research.google.com/drive/149OpY8zxxSHA1u2deInzkegnUsEj1jiI?usp=sharing) - This interactive online version can be run without any installation or setup. 
* [Python Script](https://github.com/rgriscom/LingMetaX/blob/main/LingMetaX.py) - This version must be downloaded and run on your own computer. You must have Python and the pandas library installed. 

**Citation:**
Griscom, Richard T. 2020. *LingMetaX*. https://github.com/rgriscom/LingMetaX/

**Dependencies:** 
[pandas](https://pandas.pydata.org/)

**Data Preparation:** 
The script accepts two .csv files as input:

* [Participants.csv](https://github.com/rgriscom/LingMetaX/blob/main/Templates/Participants.csv) - Contains metadata about the participants who have contributed to the creation of linguistic data.
* [Sessions.csv](https://github.com/rgriscom/LingMetaX/blob/main/Templates/Sessions.csv) - Contains metadata about recording sessions involving participants. 

Metadata must be formatted according to the provided templates provided in this project. See the [CSV Template Descriptions](https://github.com/rgriscom/LingMetaX/blob/main/Documentation/CSV%20Template%20Descriptions.md) for more information. If you have used one of the XLS form templates from the [ODK Metadata Method](https://zenodo.org/record/3871516) and exported data from KoBoToolbox, then the data will already be in the correct format. 

**Using the downloadable script:**
The downloadable Python script version also has the capability of automatically organizing resource files together with metadata. For this feature to work correctly, the following must hold true:
1. Filenames for all resource files should be identical to the corresponding session ID in the session metadata
2. Resource files for consent should consist of the participant’s full name followed by “_Consent” (e.g. Mariamu Anyawire_Consent.wav)
3. Photos of participants should consist of the participant’s full name followed by “_Photo” (e.g. Mariamu Anyawire_Photo.jpg).
    
Download the script and place it in the same folder as the metadata files, and either in the same folder as the resource files or in the parent folder of the folders which contain the resource files. [Python](https://www.python.org/) and [pandas](https://pandas.pydata.org/) must be installed in order to successfully run the script. 





