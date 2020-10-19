"""
#IMDI Maker (ELAR)
**Author:** Richard Griscom
**Last updated:** 2020-10-08
**Description:** This script takes three TSV files as input: 1) session metadata, 2) project metadata, and 3) speaker metadata. The script lets the user specify the column name that corresponds to each of the required fields from ELDP in a form. The script then compiles the information from the two spreadsheets and produces IMDI files according to the standards requested by the Endangered Languages Archive (ELAR) for each bundle. 

**Resources:** Please find template spreadsheets here:
1) Project Metadata Template (.ODS/.XLS)
2) Session Metadata Template (.ODS/.XLS) / Session Metadata Kobotoolbox form
3) Speaker Metadata Template (.ODS/.XLS) / Speaker Metadata Kobotoolbox form

**Idea for ComputEL:** Kobotoolbox form designed for ELDP depositors, which then can be used with this script to produce IMDI files. But what we really need is something like CMDI Maker that runs on a server with multiple users. But another issue is that there is often post-session metadata creation, such as the existence of resource files, their filesize, etc. This requires some sort of metadata management on the computer, as well. Propose that there be a PC app with 3 functions: 1) design forms for mobile metadata collection and computer collection using templates as a starting point, 2) filling out forms, 3) using filled out forms and resource files to produce IMDI files. In addition ideally there would be a mobile app. With Kobotoolbox, though, all of these steps except the 3) of the PC app seem to be taken care of.

Q: What about file size?
A: A script run on the user's computer could automatically detect resource files and then add them into the metadata, whereas a colab notebook cannot easily do this without having access to all of the resource files.


outline of script:
(assume all files either in the same folder or sub-folders for the time being, later add a GUI and config file)
1. opon the project, session, and speaker metadata files, load each into a DataFrame
2. make a third DataFrame which will have combined information (combined_df)
3. for each session in the session_df, pull out the corresponding information from the speaker_df
    3.b in a "IMDI_Maker_Output" folder, write an IMDI file for the session

*add section that 

   
"""
#Populate combined_df (this is currently specific to the Hadza data and involves some data creation, but later should be generalized such that it will only combine pre-formatted data into the combined_df)


#For TODAY: 
# X1. Change script to read project data from combined_df, this allows for data from multiple projects to be processed at the same time
# X2. Add a project_id column to the session_df
# X3. Write the section of code that combines the session data and project data using the project_id
# X4. Write the section of code that combines the session data with speaker data
# X5. Write the section that scans through all subfolders for written resources and media resources
# Debug the file

import os
import pandas as pd
from datetime import date

today = date.today()
print("Today's date:", today)

project_df = pd.read_csv('/home/richard/Dropbox/Academic Presentations/ComputEL 4/ELAR_Session_Metadata.csv',header=0)
project_df = project_df.applymap(str)
project_df = project_df.replace(to_replace="nan",value="")
combined_df = pd.read_csv('/home/richard/Dropbox/Academic Presentations/ComputEL 4/ELAR_Session_Metadata.csv',header=0)
combined_df = combined_df.applymap(str)
combined_df = combined_df.replace(to_replace="nan",value="")
speaker_df = pd.read_csv('/home/richard/Dropbox/Academic Presentations/ComputEL 4/ELAR_Session_Metadata.csv',header=0)
speaker_df = speaker_df.applymap(str)
speaker_df = speaker_df.replace(to_replace="nan",value="")

#Merge data from session_df, project_df, and speaker_df

for index, row in combined_df.iterrows():
    #Merge project info
    for p_index, p_row in project_df.iterrows():
        if row['project_name'] == p_row['name']:
            row['project_title'] = p_row['title']
            row['project_ID'] = p_row['ID']
            row['project_description'] = p_row['ID']
            row['project_contact1_name'] = p_row['contact1_name']
            row['project_contact1_address'] = p_row['contact1_address']
            row['project_contact1_email'] = p_row['contact1_email']
            row['project_contact1_organization'] = p_row['contact1_organization']
            row['project_contact2_name'] = p_row['contact2_name']
            row['project_contact2_address'] = p_row['contact2_address']
            row['project_contact2_email'] = p_row['contact2_email']
            row['project_contact2_organization'] = p_row['contact2_organization']
            row['project_contact3_name'] = p_row['contact3_name']
            row['project_contact3_address'] = p_row['contact3_address']
            row['project_contact3_email'] = p_row['contact3_email']
            row['project_contact3_organization'] = p_row['contact3_organization']
            row['project_contact4_name'] = p_row['contact4_name']
            row['project_contact4_address'] = p_row['contact4_address']
            row['project_contact4_email'] = p_row['contact4_email']
            row['project_contact4_organization'] = p_row['contact4_organization']
    
    #Merge speaker data
    actor_num = 1
    while actor_num <= int(row['total_actor_num']):
        for s_index, s_row in speaker_df.iterrows():

            #IF the first and second name match
            if row['actor' + str(actor_num) + '_name1'] == s_row['name1'] and row['actor' + str(actor_num) + '_name2'] == s_row['name2']:
                row['actor' + str(actor_num) + '_ethnicity'] = s_row['ethnicity']
                row['actor' + str(actor_num) + '_age'] = s_row['age']
                row['actor' + str(actor_num) + '_DOB'] = s_row['DOB']
                row['actor' + str(actor_num) + '_sex'] = s_row['sex']
                row['actor' + str(actor_num) + '_education'] = s_row['education']
                row['actor' + str(actor_num) + '_anonymized'] = s_row['anonymized']
                row['actor' + str(actor_num) + '_address'] = s_row['address']
                row['actor' + str(actor_num) + '_email'] = s_row['email']
                row['actor' + str(actor_num) + '_organisation'] = s_row['organisation']
                row['actor' + str(actor_num) + '_description'] = s_row['description']

                #Merge the language data for that speaker
                row['actor' + str(actor_num) + '_total_language_num'] = s_row['total_language_num']
                lang_num = 1
                while lang_num <= int(s_row['total_language_num']):
                    if s_row['language' + str(lang_num) + '_name'] != "":
                        row['actor' + str(actor_num) + '_language' + str(lang_num) + '_name'] = s_row['language' + str(lang_num) + '_name']
                        row['actor' + str(actor_num) + '_language' + str(lang_num) + '_ID'] = s_row['language' + str(lang_num) + '_ID']
                        row['actor' + str(actor_num) + '_language' + str(lang_num) + '_mother'] = s_row['language' + str(lang_num) + '_mother']
                        row['actor' + str(actor_num) + '_language' + str(lang_num) + '_primary'] = s_row['language' + str(lang_num) + '_primary']
                    lang_num+=1


        actor_num+=1
    row['total_media_file_num'] = 0
    row['total_written_file_num'] = 0
    #Search for resource files
    for root, dirs, files in os.walk("./"):
        for name in files:
            if name.split(".")[0] == row['name']:

                #Media resource files
                if name.endswith((".wav", ".WAV", ".mp4", ".MP4")):
                    row['total_media_file_num'] += 1
                    row['media_file' + str(media_file_num) + '_location'] = os.path.join(root, name)
                    row['media_file' + str(media_file_num) + '_size'] = str(os.path.getsize(name) * 1000)
                    row['media_file' + str(media_file_num) + '_quality'] = ""
                    row['media_file' + str(media_file_num) + '_conditions'] = ""
                    row['media_file' + str(media_file_num) + '_availability'] = row['availability']
                    row['media_file' + str(media_file_num) + '_access_date'] = str(today)
                    row['media_file' + str(media_file_num) + '_access_owner'] = ""
                    row['media_file' + str(media_file_num) + '_access_publisher'] = ""
                    row['media_file' + str(media_file_num) + '_access_contact_name'] = row['project_contact1_name']
                    row['media_file' + str(media_file_num) + '_access_contact_address'] = row['project_contact1_address']
                    row['media_file' + str(media_file_num) + '_access_contact_email'] = row['project_contact1_email']
                    row['media_file' + str(media_file_num) + '_access_contact_organisation'] = row['project_contact1_organization']
                    row['media_file' + str(media_file_num) + '_access_description'] = ""
                    row['media_file' + str(media_file_num) + '_equipment'] = row['equipment']

                    if name.endswith((".wav", ".WAV")):
                        row['media_file' + str(media_file_num) + '_type'] = 'Audio'
                        row['media_file' + str(media_file_num) + '_format'] = 'audio/x-wav'

                    if name.endswith((".mp4", ".MP4")):
                        row['media_file' + str(media_file_num) + '_type'] = 'Video'
                        row['media_file' + str(media_file_num) + '_format'] = 'video/mp4'

                #Written resource file    
                if name.endswith((".txt", ".TXT", ".csv", ".CSV", ".TextGrid", ".eaf", ".EAF", ".flextext", ".PDF", ".pdf")):
                    row['total_written_file_num'] += 1
                    row['written_file' + str(written_file_num) + '_location'] = os.path.join(root, name)
                    row['written_file' + str(written_file_num) + '_date'] = os.path.getmtime(row['media_file' + str(written_file_num) + '_location'])
                    row['written_file' + str(written_file_num) + '_size'] = str(os.path.getsize(name) * 1000)
                    row['written_file' + str(written_file_num) + '_derivation'] = "Unspecified"
                    row['written_file' + str(written_file_num) + '_anonymized'] = row['anonymized']
                    row['written_file' + str(written_file_num) + '_availability'] = row['availability']
                    row['written_file' + str(written_file_num) + '_access_date'] = str(today)
                    row['written_file' + str(written_file_num) + '_access_owner'] = ""
                    row['written_file' + str(written_file_num) + '_access_publisher'] = ""
                    row['written_file' + str(written_file_num) + '_access_contact_name'] = row['project_contact1_name']
                    row['written_file' + str(written_file_num) + '_access_contact_address'] = row['project_contact1_address']
                    row['written_file' + str(written_file_num) + '_access_contact_email'] = row['project_contact1_email']
                    row['written_file' + str(written_file_num) + '_access_contact_organisation'] = row['project_contact1_organization']
                    row['written_file' + str(written_file_num) + '_access_description'] = ""
                    
                    if name.endswith((".txt", ".TXT")):
                        row['written_file' + str(written_file_num) + '_type'] = 'Document'
                        row['written_file' + str(written_file_num) + '_format'] = 'text/plain'
                    if name.endswith((".csv", ".CSV")):
                        row['written_file' + str(written_file_num) + '_type'] = 'Document'
                        row['written_file' + str(written_file_num) + '_format'] = 'text/csv'
                    if name.endswith((".eaf", ".EAF")):
                        row['written_file' + str(written_file_num) + '_type'] = 'ELAN'
                        row['written_file' + str(written_file_num) + '_format'] = 'text/x-eaf+xml'
                    if name.endswith((".pdf", ".PDF")):
                        row['written_file' + str(written_file_num) + '_type'] = 'Document'
                        row['written_file' + str(written_file_num) + '_format'] = 'application/pdf'text/praat-textgrid
                    if name.endswith((".TextGrid")):
                        row['written_file' + str(written_file_num) + '_type'] = 'Document'
                        row['written_file' + str(written_file_num) + '_format'] = 'text/praat-textgrid'
                    if name.endswith((".flextext")):
                        row['written_file' + str(written_file_num) + '_type'] = 'Document'
                        row['written_file' + str(written_file_num) + '_format'] = 'text/x-flextext+xml'



with open('/home/richard/Dropbox/Academic Presentations/ComputEL 4/ELAR_Test_IMDI_1.imdi', 'w') as combined_file:
    for index, row in combined_df.iterrows():

        #Write text to output .IMDI file (this portion is as generalized as possible)
        combined_file.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
        #!!!Needs date_of_creation
        combined_file.write('<METATRANSCRIPT xmlns="http://www.mpi.nl/IMDI/Schema/IMDI" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ArchiveHandle="" Date="' + str(today) + '" FormatId="IMDI 3.03" Originator="IMDI Maker" Type="SESSION" Version="0" xsi:schemaLocation="http://www.mpi.nl/IMDI/Schema/IMDI ./IMDI_3.0.xsd">\n')
        combined_file.write('  <Session>\n')
        combined_file.write('    <Name>' + row['name'] + '</Name>\n')
        combined_file.write('    <Title>' + row['title'] + '</Title>\n')
        combined_file.write('    <Date>' + row['date'] + '</Date>\n')
        combined_file.write('    <Description LanguageId="" Link="">' + row['description'] + '</Description>\n')
        combined_file.write('    <MDGroup>\n')
        combined_file.write('      <Location>\n')
        combined_file.write('        <Continent Link="http://www.mpi.nl/IMDI/Schema/Continents.xml" Type="ClosedVocabulary">' + row['location_continent'] + '</Continent>\n')
        combined_file.write('        <Country Link="http://www.mpi.nl/IMDI/Schema/Countries.xml" Type="OpenVocabulary">' + row['location_country'] + '</Country>\n')
        combined_file.write('        <Region>' + row['location_region'] + '</Region>\n')
        combined_file.write('        <Address>' + row['location_address'] + '</Address>\n')
        combined_file.write('      </Location>\n')
        combined_file.write('      <Project>\n')
        combined_file.write('        <Name>' + row['project_name'] + '</Name>\n')
        combined_file.write('        <Title>' +  + '</Title>\n')
        combined_file.write('        <Id>' + project_df['project_ID'] + '</Id>\n')
        combined_file.write('        <Contact>\n')    
        combined_file.write('          <Name>' + row['project_contact1_name'] + '</Name>\n')
        combined_file.write('          <Address>' + row['project_contact1_address'] + '</Address>\n')
        combined_file.write('          <Email>' + row['project_contact1_email'] +  '</Email>\n')
        combined_file.write('          <Organisation>' + row['project_contact1_organization'] + '</Organisation>\n')
        combined_file.write('        </Contact>\n')
        if row['project_contact2_name'] != "":
            combined_file.write('        <Contact>\n')    
            combined_file.write('          <Name>' + row['project_contact2_name'] + '</Name>\n')
            combined_file.write('          <Address>' + row['project_contact2_address'] + '</Address>\n')
            combined_file.write('          <Email>' + row['project_contact2_email'] +  '</Email>\n')
            combined_file.write('          <Organisation>' + row['project_contact2_organization'] + '</Organisation>\n')
            combined_file.write('        </Contact>\n')
        if row['project_contact3_name'] != "":
            combined_file.write('        <Contact>\n')    
            combined_file.write('          <Name>' + row['project_contact3_name'] + '</Name>\n')
            combined_file.write('          <Address>' + row['project_contact3_address'] + '</Address>\n')
            combined_file.write('          <Email>' + row['project_contact3_email'] +  '</Email>\n')
            combined_file.write('          <Organisation>' + row['project_contact3_organization'] + '</Organisation>\n')
            combined_file.write('        </Contact>\n')
        if row['project_contact4_name'] != "":
            combined_file.write('        <Contact>\n')    
            combined_file.write('          <Name>' + row['project_contact4_name'] + '</Name>\n')
            combined_file.write('          <Address>' + row['project_contact4_address'] + '</Address>\n')
            combined_file.write('          <Email>' + row['project_contact4_email'] +  '</Email>\n')
            combined_file.write('          <Organisation>' + row['project_contact4_organization'] + '</Organisation>\n')
            combined_file.write('        </Contact>\n')
        combined_file.write('        <Description LanguageId="ISO639-3:eng" Link="">' + row['project_description'] + '</Description>\n')
        combined_file.write('      </Project>\n')
        combined_file.write('      <Keys/>\n')
        combined_file.write('      <Content>\n')
        combined_file.write('        <Genre Link="http://www.mpi.nl/IMDI/Schema/Content-Genre.xml" Type="OpenVocabulary">' + row['genre'] + '</Genre>\n')
        combined_file.write('        <SubGenre Link="http://www.mpi.nl/IMDI/Schema/Content-SubGenre.xml" Type="OpenVocabularyList">' + row['subgenre'] + '</SubGenre>\n')
        combined_file.write('        <Task Link="http://www.mpi.nl/IMDI/Schema/Content-Task.xml" Type="OpenVocabulary">' + row['task'] + '</Task>\n')
        combined_file.write('        <Modalities Link="http://www.mpi.nl/IMDI/Schema/Content-Modalities.xml" Type="OpenVocabularyList" >' + row['modalities'] + '</Modalities>\n')
        combined_file.write('        <Subject Link="http://www.mpi.nl/IMDI/Schema/Content-Subject.xml" Type="OpenVocabularyList">language description</Subject>\n')
        combined_file.write('        <CommunicationContext>\n')
        if row['interactivity'] != "":
            combined_file.write('          <Interactivity Link="http://www.mpi.nl/IMDI/Schema/Content-Interactivity.xml" Type="ClosedVocabulary">' + row['interactivity'] + '</Interactivity>\n')
        else:
            combined_file.write('          <Interactivity Link="http://www.mpi.nl/IMDI/Schema/Content-Interactivity.xml" Type="ClosedVocabulary">Unspecified</Interactivity>\n')
        if row['planning_type'] != "":  
            combined_file.write('          <PlanningType Link="http://www.mpi.nl/IMDI/Schema/Content-PlanningType.xml" Type="ClosedVocabulary">' + row['planning_type'] + '</PlanningType>\n')
        else:
            combined_file.write('          <PlanningType Link="http://www.mpi.nl/IMDI/Schema/Content-PlanningType.xml" Type="ClosedVocabulary">Unspecified</PlanningType>\n')
        if row['involvement'] != "":
            combined_file.write('          <Involvement Link="http://www.mpi.nl/IMDI/Schema/Content-Involvement.xml" Type="ClosedVocabulary">' + row['involvement'] + '</Involvement>\n')
        else:
            combined_file.write('          <Involvement Link="http://www.mpi.nl/IMDI/Schema/Content-Involvement.xml" Type="ClosedVocabulary">Unspecified</Involvement>\n')
        if row['social_context'] != "":
            combined_file.write('          <SocialContext Link="http://www.mpi.nl/IMDI/Schema/Content-SocialContext.xml" Type="ClosedVocabulary">' + row['social_context'] + '</SocialContext>\n')
        else:
            combined_file.write('          <SocialContext Link="http://www.mpi.nl/IMDI/Schema/Content-SocialContext.xml" Type="ClosedVocabulary">Unspecified</SocialContext>\n')
        if row['event_structure'] != "":
            combined_file.write('          <EventStructure Link="http://www.mpi.nl/IMDI/Schema/Content-EventStructure.xml" Type="ClosedVocabulary">' + row['event_structure'] + '</EventStructure>\n')
        else:
            combined_file.write('          <EventStructure Link="http://www.mpi.nl/IMDI/Schema/Content-EventStructure.xml" Type="ClosedVocabulary">Unspecified</EventStructure>\n')
        if row['channel'] != "":          
            combined_file.write('          <Channel Link="http://www.mpi.nl/IMDI/Schema/Content-Channel.xml" Type="ClosedVocabulary">' + row['channel'] + '</Channel>\n')
        else:
            combined_file.write('          <Channel Link="http://www.mpi.nl/IMDI/Schema/Content-Channel.xml" Type="ClosedVocabulary">Unspecified</Channel>\n')
        combined_file.write('        </CommunicationContext>\n')
        combined_file.write('        <Languages>\n')
        combined_file.write('          <Description LanguageId="ISO639-3:eng" Link=""/>\n')
        combined_file.write('          <Language>\n')
        combined_file.write('          <Id>' + row['language1_ID'] + '</Id>\n')
        combined_file.write('          <Name Link="http://www.mpi.nl/IMDI/Schema/MPI-Languages.xml" Type="OpenVocabulary">' + row['language1_name'] + '</Name>\n')
        combined_file.write('          <Dominant Link="http://www.mpi.nl/IMDI/Schema/Boolean.xml" Type="ClosedVocabulary">Unspecified</Dominant>\n')
        combined_file.write('          <SourceLanguage Link="http://www.mpi.nl/IMDI/Schema/Boolean.xml" Type="ClosedVocabulary">Unspecified</SourceLanguage>\n')
        combined_file.write('          <TargetLanguage Link="http://www.mpi.nl/IMDI/Schema/Boolean.xml" Type="ClosedVocabulary">Unspecified</TargetLanguage>\n')
        if row['language1_working_or_content'] == "content":
            combined_file.write('          <Description LanguageId="ISO639-3:eng" Link="">Content Language</Description>\n')
        else:
            combined_file.write('          <Description LanguageId="ISO639-3:eng" Link="">Working Language</Description>\n')
        combined_file.write('        </Language>\n')

        #Add Language 2 if it exists
        if row['language2_name'] != "":
            combined_file.write('          <Language>\n')
            combined_file.write('          <Id>' + row['language2_ID'] + '</Id>\n')
            combined_file.write('          <Name Link="http://www.mpi.nl/IMDI/Schema/MPI-Languages.xml" Type="OpenVocabulary">' + row['language2_name'] + '</Name>\n')
            combined_file.write('          <Dominant Link="http://www.mpi.nl/IMDI/Schema/Boolean.xml" Type="ClosedVocabulary">Unspecified</Dominant>\n')
            combined_file.write('          <SourceLanguage Link="http://www.mpi.nl/IMDI/Schema/Boolean.xml" Type="ClosedVocabulary">Unspecified</SourceLanguage>\n')
            combined_file.write('          <TargetLanguage Link="http://www.mpi.nl/IMDI/Schema/Boolean.xml" Type="ClosedVocabulary">Unspecified</TargetLanguage>\n')
            if row['language2_working_or_content'] == "content":
                combined_file.write('          <Description LanguageId="ISO639-3:eng" Link="">Content Language</Description>\n')
            else:
                combined_file.write('          <Description LanguageId="ISO639-3:eng" Link="">Working Language</Description>\n')
            combined_file.write('        </Language>\n')

        #Add Language 3 if it exists
        if row['language3_name'] != "":
            combined_file.write('          <Language>\n')
            combined_file.write('          <Id>' + row['language3_ID'] + '</Id>\n')
            combined_file.write('          <Name Link="http://www.mpi.nl/IMDI/Schema/MPI-Languages.xml" Type="OpenVocabulary">' + row['language3_name'] + '</Name>\n')
            combined_file.write('          <Dominant Link="http://www.mpi.nl/IMDI/Schema/Boolean.xml" Type="ClosedVocabulary">Unspecified</Dominant>\n')
            combined_file.write('          <SourceLanguage Link="http://www.mpi.nl/IMDI/Schema/Boolean.xml" Type="ClosedVocabulary">Unspecified</SourceLanguage>\n')
            combined_file.write('          <TargetLanguage Link="http://www.mpi.nl/IMDI/Schema/Boolean.xml" Type="ClosedVocabulary">Unspecified</TargetLanguage>\n')
            if row['language3_working_or_content'] == "content":
                combined_file.write('          <Description LanguageId="ISO639-3:eng" Link="">Content Language</Description>\n')
            else:
                combined_file.write('          <Description LanguageId="ISO639-3:eng" Link="">Working Language</Description>\n')
            combined_file.write('        </Language>\n')
        combined_file.write('        </Languages>\n')
        combined_file.write('        <Keys>\n')
        combined_file.write('          <Key Name="Topic" Type="OpenVocabulary">' + row['topic'] + '</Key>\n')
        combined_file.write('          <Key Name="Keyword" Type="OpenVocabulary">' + row['keyword1'] + '</Key>\n')
        combined_file.write('          <Key Name="Keyword" Type="OpenVocabulary">' + row['keyword2'] + '</Key>\n')
        combined_file.write('          <Key Name="Keyword" Type="OpenVocabulary">' + row['keyword3'] + '</Key>\n')
        combined_file.write('          <Key Name="Keyword" Type="OpenVocabulary">' + row['keyword4'] + '</Key>\n')
        combined_file.write('          <Key Name="Keyword" Type="OpenVocabulary">' + row['keyword5'] + '</Key>\n')
        combined_file.write('        </Keys>\n')
        combined_file.write('        <Description LanguageId="ISO639-3:eng" Link="">...</Description>\n')
        combined_file.write('      </Content>\n')
        combined_file.write('      <Actors>\n')

        #Add all actors, unlimited
        actor_num = 1
        while actor_num <= int(row['total_actor_num']):
            if row['actor' + str(actor_num) + '_name1'] != "": 
                combined_file.write('        <Actor>\n')
                combined_file.write('          <Role Link="http://www.mpi.nl/IMDI/Schema/Actor-Role.xml" Type="OpenVocabularyList">' + row['actor' + str(actor_num) + '_role'] + '</Role>\n')
                combined_file.write('          <Name>' + row['actor' + str(actor_num) + '_name1'] + '</Name>\n')
                combined_file.write('          <FullName>' + row['actor' + str(actor_num) + '_name1'] + ' ' + row['actor' + str(actor_num) + '_name2'] + '</FullName>\n')
                combined_file.write('          <Code/>\n')
                combined_file.write('          <FamilySocialRole Link="http://www.mpi.nl/IMDI/Schema/Actor-FamilySocialRole.xml" Type="OpenVocabularyList" />\n')
                combined_file.write('          <Languages>\n')
                combined_file.write('            <Description LanguageId="ISO639-3:eng" Link=""/>\n')
                
                #Add the languages for the actor, unlimited
                lang_num = 1
                while lang_num <= int(row['actor' + str(actor_num) + '_total_language_num']):
                    if row['actor' + str(actor_num) + '_language' + str(lang_num) + '_name'] != "": 
                        combined_file.write('            <Language>\n')
                        combined_file.write('              <Id>' + row['actor' + str(actor_num) + '_language' + str(lang_num) + '_ID'] + '</Id>\n')
                        combined_file.write('              <Name Link="http://www.mpi.nl/IMDI/Schema/MPI-Languages.xml" Type="OpenVocabulary">' + row['actor' + str(actor_num) + '_language' + str(lang_num) + '_name'] + '</Name>\n')
                        if row['actor' + str(actor_num) + '_language' + str(lang_num) + '_mother'] != "":
                            combined_file.write('              <MotherTongue Link="http://www.mpi.nl/IMDI/Schema/Boolean.xml" Type="ClosedVocabulary">' + row['actor' + str(actor_num) + '_language' + str(lang_num) + '_mother'].lower() + '</MotherTongue>\n')
                        else:
                            combined_file.write('              <MotherTongue Link="http://www.mpi.nl/IMDI/Schema/Boolean.xml" Type="ClosedVocabulary">Unspecified</MotherTongue>\n')
                        if row['actor' + str(actor_num) + '_language' + str(lang_num) + '_primary'] != "":          
                            combined_file.write('              <PrimaryLanguage Link="http://www.mpi.nl/IMDI/Schema/Boolean.xml" Type="ClosedVocabulary">' + row['actor' + str(actor_num) + '_language' + str(lang_num) + '_primary'].lower() + '</PrimaryLanguage>\n')
                        else:
                            combined_file.write('              <PrimaryLanguage Link="http://www.mpi.nl/IMDI/Schema/Boolean.xml" Type="ClosedVocabulary">Unspecified</PrimaryLanguage>\n')
                                
                        combined_file.write('              <Description LanguageId="ISO639-3:eng" Link=""/>\n')
                        combined_file.write('            </Language>\n')
                    lang_num+=1
                
                combined_file.write('          </Languages>\n')
                if row['actor' + str(actor_num) + '_ethnicity'] != "":
                    combined_file.write('          <EthnicGroup Type="OpenVocabulary">' + row['actor' + str(actor_num) + '_ethnicity'] + '</EthnicGroup>\n')
                else:
                    combined_file.write('          <EthnicGroup Type="OpenVocabulary" />\n')
                if row['actor' + str(actor_num) + '_age'] != "":
                    combined_file.write('          <Age>' + row['actor' + str(actor_num) + '_age'] + '</Age>\n')
                else:
                    combined_file.write('          <Age>Unspecified</Age>\n')
                if row['actor' + str(actor_num) + '_DOB'] != "":
                    combined_file.write('          <BirthDate>' + row['actor' + str(actor_num) + '_DOB'] + '</BirthDate>\n')
                else:
                    combined_file.write('          <BirthDate>Unspecified</BirthDate>\n')
                combined_file.write('          <Sex Link="http://www.mpi.nl/IMDI/Schema/Actor-Sex.xml" Type="ClosedVocabulary">' + row['actor' + str(actor_num) + '_sex'] + '</Sex>\n')
                combined_file.write('          <Education>' + row['actor' + str(actor_num) + '_education'] + '</Education>\n')
                combined_file.write('          <Anonymized Link="http://www.mpi.nl/IMDI/Schema/Boolean.xml" Type="ClosedVocabulary">' + row['actor' + str(actor_num) + '_anonymized'].lower() + '</Anonymized>\n')            
                combined_file.write('          <Contact>\n')
                combined_file.write('            <Name>' + row['actor' + str(actor_num) + '_name1'] + ' ' + row['actor' + str(actor_num) + '_name2'] + '</Name>\n')
                if row['actor' + str(actor_num) + '_address'] != "":
                    combined_file.write('            <Address>' + row['actor' + str(actor_num) + '_address'] + '</Address>\n')
                else: 
                    combined_file.write('            <Address />\n')
                if row['actor' + str(actor_num) + '_email'] != "":
                    combined_file.write('            <Email>' + row['actor' + str(actor_num) + '_email'] + '</Email>\n')
                else: 
                    combined_file.write('            <Email />\n')
                if row['actor' + str(actor_num) + '_organisation'] != "":
                    combined_file.write('            <Organisation>' + row['actor' + str(actor_num) + '_organisation'] + '</Organisation>\n')
                else: 
                    combined_file.write('            <Organisation />\n')
                combined_file.write('          </Contact>\n')
                combined_file.write('          <Keys/>\n')
                if row['actor' + str(actor_num) + '_description'] != "":
                    combined_file.write('          <Description LanguageId="ISO639-3:eng" Link="">' + row['actor' + str(actor_num) + '_description'] + '</Description>\n')
                else:
                    combined_file.write('          <Description LanguageId="" Link="" />\n')
                combined_file.write('        </Actor>\n')
            actor_num+=1
        combined_file.write('      </Actors>\n')
        combined_file.write('    </MDGroup>\n')
        combined_file.write('    <Resources>\n')

        #Add each media file, unlimited
        media_file_num = 1
        while media_file_num <= int(row['total_media_file_num']):
            combined_file.write('      <MediaFile>\n')
            #This uses a variable that full file location, e.g. "../Media/Qustan059.wav"
            combined_file.write('        <ResourceLink ArchiveHandle="">' + row['media_file' + str(media_file_num) + '_location'] + '</ResourceLink>\n')
            combined_file.write('        <Type Link="http://www.mpi.nl/IMDI/Schema/MediaFile-Type.xml" Type="ClosedVocabulary">' + row['media_file' + str(media_file_num) + '_type'] + '</Type>\n')
            combined_file.write('        <Format Link="http://www.mpi.nl/IMDI/Schema/MediaFile-Format.xml" Type="OpenVocabulary">' + row['media_file' + str(media_file_num) + '_format'] + '</Format>\n')
            combined_file.write('        <Size>' + row['media_file' + str(media_file_num) + '_size'] + '</Size>\n')
            if row['media_file' + str(media_file_num) + '_quality'] != "":
                combined_file.write('        <Quality Type="ClosedVocabulary">' + row['media_file' + str(media_file_num) + '_quality'] + '</Quality>\n')
            else:
                combined_file.write('        <Quality Type="ClosedVocabulary">Unspecified</Quality>\n')
            combined_file.write('        <RecordingConditions>' + row['media_file' + str(media_file_num) + '_conditions'] + '</RecordingConditions>\n')
            combined_file.write('        <TimePosition>\n')
            combined_file.write('          <Start>Unspecified</Start>\n')
            combined_file.write('          <End>Unspecified</End>\n')
            combined_file.write('        </TimePosition>\n')
            combined_file.write('        <Access>\n')
            combined_file.write('          <Availability Type="OpenVocabulary">' + row['media_file' + str(media_file_num) + '_availability'] + '</Availability>\n')
            combined_file.write('          <Date>' + row['media_file' + str(media_file_num) + '_access_date'] + '</Date>\n')
            combined_file.write('          <Owner>' + row['media_file' + str(media_file_num) + '_access_owner'] + '</Owner>\n')
            combined_file.write('          <Publisher>' + row['media_file' + str(media_file_num) + '_access_publisher'] + '</Publisher>\n')
            combined_file.write('          <Contact>\n')
            combined_file.write('            <Name>' + row['media_file' + str(media_file_num) + '_access_contact_name'] + '</Name>\n')
            combined_file.write('            <Address>' + row['media_file' + str(media_file_num) + '_access_contact_address'] + '</Address>\n')
            combined_file.write('            <Email>' + row['media_file' + str(media_file_num) + '_access_contact_email'] + '</Email>\n')
            combined_file.write('            <Organisation>' + row['media_file' + str(media_file_num) + '_access_contact_organisation'] + '</Organisation>\n')
            combined_file.write('          </Contact>\n')
            combined_file.write('          <Description>' + row['media_file' + str(media_file_num) + '_access_description'] + '</Description>\n')
            combined_file.write('        </Access>\n')
            combined_file.write('        <Description LanguageId="" Link=""/>\n')
            combined_file.write('        <Keys>\n')
            combined_file.write('          <Key Name="RecordingEquipment" Type="OpenVocabulary">' + row['media_file' + str(media_file_num) + '_equipment'] + '</Key>\n')
            combined_file.write('        </Keys>\n')
            combined_file.write('      </MediaFile>\n')
            media_file_num +=1

        #Add each written resource file, unlimited
        written_file_num = 1
        while written_file_num <= int(row['total_written_file_num']):
            combined_file.write('      <WrittenResource>\n')
            #This uses a variable that full file location, e.g. "../Media/Qustan059.wav"
            combined_file.write('        <ResourceLink ArchiveHandle="">' + row['written_file' + str(written_file_num) + '_location'] + '</ResourceLink>\n')
            combined_file.write('        <MediaResourceLink/>\n')
            if row['written_file' + str(written_file_num) + '_date'] != "":
                combined_file.write('        <Date>' + row['written_file' + str(written_file_num) + '_date'] + '</Date>\n')
            else:
                combined_file.write('        <Date>Unspecified</Date>\n')
            combined_file.write('        <Type Link="http://www.mpi.nl/IMDI/Schema/WrittenResource-Type.xml" Type="OpenVocabulary">' + row['written_file' + str(written_file_num) + '_type'] + '</Type>\n')
            combined_file.write('        <SubType Link="http://www.mpi.nl/IMDI/Schema/WrittenResource-SubType.xml" Type="OpenVocabulary">Unspecified</SubType>\n')
            combined_file.write('        <Format Link="http://www.mpi.nl/IMDI/Schema/WrittenResource-Format.xml" Type="OpenVocabulary">' + row['written_file' + str(written_file_num) + '_format'] + '</Format>\n')
            combined_file.write('        <Size Type="OpenVocabulary">' + row['written_file' + str(written_file_num) + '_size'] + '</Size>\n')
            combined_file.write('        <Validation>\n')
            combined_file.write('          <Type Link="http://www.mpi.nl/IMDI/Schema/Validation-Type.xml" Type="ClosedVocabulary">Unspecified</Type>\n')
            combined_file.write('          <Methodology Link="http://www.mpi.nl/IMDI/Schema/Validation-Methodology.xml" Type="ClosedVocabulary">Unspecified</Methodology>\n')
            combined_file.write('          <Level>Unspecified</Level>\n')
            combined_file.write('          <Description LanguageId="" Link=""/>\n')
            combined_file.write('        </Validation>\n')
            combined_file.write('        <Derivation Link="http://www.mpi.nl/IMDI/Schema/WrittenResource-Derivation.xml" Type="ClosedVocabulary">' + row['written_file' + str(written_file_num) + '_derivation'] + '</Derivation>\n')
            combined_file.write('        <CharacterEncoding/>\n')
            combined_file.write('        <ContentEncoding/>\n')
            combined_file.write('        <LanguageId Type="OpenVocabulary"/>\n')
            combined_file.write('        <Anonymized Type="ClosedVocabulary">' + row['written_file' + str(written_file_num) + '_anonymized'] + '</Anonymized>\n')
            combined_file.write('        <Access>\n')
            combined_file.write('          <Availability Type="OpenVocabulary">' + row['written_file' + str(written_file_num) + '_availability'] + '</Availability>\n')
            combined_file.write('          <Date>' + row['written_file' + str(written_file_num) + '_access_date'] + '</Date>\n')
            combined_file.write('          <Owner>' + row['written_file' + str(written_file_num) + '_access_owner'] + '</Owner>\n')
            combined_file.write('          <Publisher>' + row['written_file' + str(written_file_num) + '_access_publisher'] + '</Publisher>\n')
            combined_file.write('          <Contact>\n')
            combined_file.write('            <Name>' + row['written_file' + str(written_file_num) + '_access_contact_name'] + '</Name>\n')
            combined_file.write('            <Address>' + row['written_file' + str(written_file_num) + '_access_contact_address'] + '</Address>\n')
            combined_file.write('            <Email>' + row['written_file' + str(written_file_num) + '_access_contact_email'] + '</Email>\n')
            combined_file.write('            <Organisation>' + row['written_file' + str(written_file_num) + '_access_contact_organisation'] + '</Organisation>\n')
            combined_file.write('          </Contact>\n')
            combined_file.write('          <Description>' + row['written_file' + str(written_file_num) + '_access_description'] + '</Description>\n')
            combined_file.write('        </Access>\n')
            combined_file.write('        <Description LanguageId="" Link=""/>\n')
            combined_file.write('        <Keys />\n')
            combined_file.write('      </WrittenResource>\n')
            written_file_num+=1
        combined_file.write('    </Resources>\n')
        combined_file.write('    <References />\n')
        combined_file.write('  </Session>\n')
        combined_file.write('</METATRANSCRIPT>\n')
combined_file.close()
