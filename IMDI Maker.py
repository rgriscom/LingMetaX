"""
#IMDI Maker (ELAR)
**Author:** Richard Griscom
**Last updated:** 2020-10-08
**Description:** This script takes three TSV files as input: 1) session metadata, 2) project metadata, and 3) speaker metadata. The script lets the user specify the column name that corresponds to each of the required fields from ELDP in a form. The script then compiles the information from the two spreadsheets and produces IMDI files according to the standards requested by the Endangered Languages Archive (ELAR) for each bundle. 

**Resources:** Please find template spreadsheets here:
1) Project Metadata Template (.ODS/.XLS)
2) Session Metadata Template (.ODS/.XLS) / Session Metadata Kobotoolbox form
3) Speaker Metadata Template (.ODS/.XLS) / Speaker Metadata Kobotoolbox form



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
# X1. Run it
# #2. Debug
# 2.5 Add output CVS with each session name and the problem each one has (start with missing speakers)
# 3. Check output, fix errors
# 4. Add ability to detect written resources with version control _YYYYMMDD at the end of the filename


import os, datetime
import pandas as pd
from datetime import date

today = date.today()
print("Today's date:", today)
current_dir = os.path.dirname(__file__)
project_df = pd.read_csv(current_dir + '/ELAR_Project_Metadata.csv',header=0)
project_df = project_df.applymap(str)
project_df = project_df.replace(to_replace="nan",value="")
combined_df = pd.read_csv(current_dir + '/ELAR_Session_Metadata.csv',header=0)
combined_df = combined_df.applymap(str)
combined_df = combined_df.replace(to_replace="nan",value="")
speaker_df = pd.read_csv(current_dir + '/ELAR_Speaker_Metadata.csv',header=0)
speaker_df = speaker_df.applymap(str)
speaker_df = speaker_df.replace(to_replace="nan",value="")

#Merge data from session_df, project_df, and speaker_df
for index, row in combined_df.iterrows():
    #Merge project info
    for p_index, p_row in project_df.iterrows():
        if row['project_name'] == p_row['name']:
            combined_df.at[index, 'project_title'] = p_row['title']            
            combined_df.at[index, 'project_ID'] = p_row['ID']
            combined_df.at[index, 'project_description'] = p_row['description']
            combined_df.at[index, 'project_contact1_name'] = p_row['contact1_name']
            combined_df.at[index, 'project_contact1_address'] = p_row['contact1_address']
            combined_df.at[index, 'project_contact1_email'] = p_row['contact1_email']
            combined_df.at[index, 'project_contact1_organisation'] = p_row['contact1_organisation']
            combined_df.at[index, 'project_contact2_name'] = p_row['contact2_name']
            combined_df.at[index, 'project_contact2_address'] = p_row['contact2_address']
            combined_df.at[index, 'project_contact2_email'] = p_row['contact2_email']
            combined_df.at[index, 'project_contact2_organisation'] = p_row['contact2_organisation']
            combined_df.at[index, 'project_contact3_name'] = p_row['contact3_name']
            combined_df.at[index, 'project_contact3_address'] = p_row['contact3_address']
            combined_df.at[index, 'project_contact3_email'] = p_row['contact3_email']
            combined_df.at[index, 'project_contact3_organisation'] = p_row['contact3_organisation']
            combined_df.at[index, 'project_contact4_name'] = p_row['contact4_name']
            combined_df.at[index, 'project_contact4_address'] = p_row['contact4_address']
            combined_df.at[index, 'project_contact4_email'] = p_row['contact4_email']
            combined_df.at[index, 'project_contact4_organisation'] = p_row['contact4_organisation']
    
    #Merge speaker data
    actor_num = 1
    combined_df.at[index, 'total_actor_num'] = 0
    speakers_not_found = []
    while actor_num < 6:
        actor_check = 0
        for s_index, s_row in speaker_df.iterrows():

            #IF the first and second name match
            if row['actor' + str(actor_num) + '_name1'] == s_row['name1'] and row['actor' + str(actor_num) + '_name2'] == s_row['name2'] and actor_check == 0:
                
                combined_df.at[index, 'actor' + str(actor_num) + '_ethnicity'] = s_row['ethnicity']
                combined_df.at[index, 'actor' + str(actor_num) + '_age'] = s_row['age']
                combined_df.at[index, 'actor' + str(actor_num) + '_DOB'] = s_row['DOB']
                combined_df.at[index, 'actor' + str(actor_num) + '_sex'] = s_row['sex']
                combined_df.at[index, 'actor' + str(actor_num) + '_education'] = s_row['education']
                combined_df.at[index, 'actor' + str(actor_num) + '_anonymized'] = s_row['anonymized'].lower()
                combined_df.at[index, 'actor' + str(actor_num) + '_address'] = s_row['address']
                combined_df.at[index, 'actor' + str(actor_num) + '_email'] = s_row['email']
                combined_df.at[index, 'actor' + str(actor_num) + '_organisation'] = s_row['organisation']
                combined_df.at[index, 'actor' + str(actor_num) + '_description'] = s_row['description']
                combined_df.at[index, 'total_actor_num'] += 1
                
                #Merge the language data for that speaker
            
                lang_num = 1
                while lang_num <= 5:
                    if s_row['language' + str(lang_num) + '_name'] != "":
                        combined_df.at[index, 'actor' + str(actor_num) + '_language' + str(lang_num) + '_name'] = s_row['language' + str(lang_num) + '_name']
                        combined_df.at[index, 'actor' + str(actor_num) + '_language' + str(lang_num) + '_ID'] = s_row['language' + str(lang_num) + '_ID']
                        combined_df.at[index, 'actor' + str(actor_num) + '_language' + str(lang_num) + '_mother'] = s_row['language' + str(lang_num) + '_mother']
                        combined_df.at[index, 'actor' + str(actor_num) + '_language' + str(lang_num) + '_primary'] = s_row['language' + str(lang_num) + '_primary']
                        combined_df.at[index, 'actor' + str(actor_num) + '_total_language_num'] = lang_num
                    lang_num+=1
                actor_check = 1
        if actor_check == 0 and row['actor' + str(actor_num) + '_name1'] != "":
            speakers_not_found.append(row['actor' + str(actor_num) + '_name1'] + " " + row['actor' + str(actor_num) + '_name2'])
        actor_num+=1
        actor_check = 0
    #Check if all actors have been found
    counter = 1
    actor_counter = 0
    while counter < 6:
        if row['actor' + str(counter) + '_name1'] != "":
            actor_counter += 1
        counter+=1
    
    combined_df.at[index, 'total_media_file_num'] = 0
    combined_df.at[index, 'total_written_file_num'] = 0
    media_file_num = 0
    written_file_num = 0
    
    #Search for resource files
    for root, dirs, files in os.walk(current_dir):
        for name in files:
            written_resource_name_check = False
            if len(name.split("_")) > 2:
                if (name.split("_")[0] + "_" + name.split("_")[1])  == row['name']:
                    written_resource_name_check = True
            if name.split(".")[0] == row['name'] or written_resource_name_check == True:
                
                #Media resource files
                if name.endswith((".wav", ".WAV", ".mp4", ".MP4")):
                    media_file_num+=1
                    combined_df.at[index, 'total_media_file_num'] += 1
                    combined_df.at[index, 'media_file' + str(media_file_num) + '_location'] = root.split(current_dir)[1].split("/")[1] + os.sep + name
                    combined_df.at[index, 'media_file' + str(media_file_num) + '_size'] = str(int(os.path.getsize(root + os.sep + name) / 1000)) + "KB"
                    combined_df.at[index,  'media_file' + str(media_file_num) + '_quality'] = ""
                    combined_df.at[index,  'media_file' + str(media_file_num) + '_conditions'] = ""
                    combined_df.at[index,  'media_file' + str(media_file_num) + '_availability'] = combined_df.at[index,  'availability']
                    combined_df.at[index,  'media_file' + str(media_file_num) + '_access_date'] = str(today)
                    combined_df.at[index,  'media_file' + str(media_file_num) + '_access_owner'] = ""
                    combined_df.at[index,  'media_file' + str(media_file_num) + '_access_publisher'] = ""
                    combined_df.at[index,  'media_file' + str(media_file_num) + '_access_contact_name'] = combined_df.at[index,  'project_contact1_name']
                    combined_df.at[index,  'media_file' + str(media_file_num) + '_access_contact_address'] = combined_df.at[index,  'project_contact1_address']
                    combined_df.at[index,  'media_file' + str(media_file_num) + '_access_contact_email'] = combined_df.at[index,  'project_contact1_email']
                    combined_df.at[index,  'media_file' + str(media_file_num) + '_access_contact_organisation'] = combined_df.at[index,  'project_contact1_organisation']
                    combined_df.at[index,  'media_file' + str(media_file_num) + '_access_description'] = ""
                    combined_df.at[index, 'media_file' + str(media_file_num) + '_equipment'] = combined_df.at[index,  'equipment']

                    if name.endswith((".wav", ".WAV")):
                        combined_df.at[index, 'media_file' + str(media_file_num) + '_type'] = 'Audio'
                        combined_df.at[index, 'media_file' + str(media_file_num) + '_format'] = 'audio/x-wav'

                    if name.endswith((".mp4", ".MP4")):
                        combined_df.at[index, 'media_file' + str(media_file_num) + '_type'] = 'Video'
                        combined_df.at[index, 'media_file' + str(media_file_num) + '_format'] = 'video/mp4'

                #Written resource file    
                if name.endswith((".txt", ".TXT", ".csv", ".CSV", ".TextGrid", ".eaf", ".EAF", ".flextext", ".PDF", ".pdf")):
                    written_file_num+=1
                    combined_df.at[index, 'total_written_file_num'] += 1
                    combined_df.at[index, 'written_file' + str(written_file_num) + '_location'] = root.split(current_dir)[1].split("/")[1] + os.sep + name
                    combined_df.at[index, 'written_file' + str(written_file_num) + '_date'] = datetime.datetime.fromtimestamp(os.path.getmtime(root + os.sep + name)).strftime('%Y-%m-%d')
                    combined_df.at[index, 'written_file' + str(written_file_num) + '_size'] = str(int(os.path.getsize(root + os.sep + name) / 1000)) + "KB"
                    combined_df.at[index, 'written_file' + str(written_file_num) + '_derivation'] = "Unspecified"
                    combined_df.at[index, 'written_file' + str(written_file_num) + '_anonymized'] = combined_df.at[index, 'anonymized'].lower()
                    combined_df.at[index, 'written_file' + str(written_file_num) + '_availability'] = combined_df.at[index, 'availability']
                    combined_df.at[index, 'written_file' + str(written_file_num) + '_access_date'] = str(today)
                    combined_df.at[index, 'written_file' + str(written_file_num) + '_access_owner'] = ""
                    combined_df.at[index, 'written_file' + str(written_file_num) + '_access_publisher'] = ""
                    combined_df.at[index, 'written_file' + str(written_file_num) + '_access_contact_name'] = combined_df.at[index, 'project_contact1_name']
                    combined_df.at[index, 'written_file' + str(written_file_num) + '_access_contact_address'] = combined_df.at[index, 'project_contact1_address']
                    combined_df.at[index, 'written_file' + str(written_file_num) + '_access_contact_email'] = combined_df.at[index, 'project_contact1_email']
                    combined_df.at[index, 'written_file' + str(written_file_num) + '_access_contact_organisation'] = combined_df.at[index, 'project_contact1_organisation']
                    combined_df.at[index, 'written_file' + str(written_file_num) + '_access_description'] = ""
                    
                    if name.endswith((".txt", ".TXT")):
                        combined_df.at[index, 'written_file' + str(written_file_num) + '_type'] = 'Document'
                        combined_df.at[index, 'written_file' + str(written_file_num) + '_format'] = 'text/plain'
                    if name.endswith((".csv", ".CSV")):
                        combined_df.at[index, 'written_file' + str(written_file_num) + '_type'] = 'Document'
                        combined_df.at[index,  'written_file' + str(written_file_num) + '_format'] = 'text/csv'
                    if name.endswith((".eaf", ".EAF")):
                        combined_df.at[index,  'written_file' + str(written_file_num) + '_type'] = 'ELAN'
                        combined_df.at[index,  'written_file' + str(written_file_num) + '_format'] = 'text/x-eaf+xml'
                    if name.endswith((".pdf", ".PDF")):
                        combined_df.at[index,  'written_file' + str(written_file_num) + '_type'] = 'Document'
                        combined_df.at[index,  'written_file' + str(written_file_num) + '_format'] = 'application/pdf'
                    if name.endswith((".TextGrid")):
                        combined_df.at[index,  'written_file' + str(written_file_num) + '_type'] = 'Document'
                        combined_df.at[index,  'written_file' + str(written_file_num) + '_format'] = 'text/praat-textgrid'
                    if name.endswith((".flextext")):
                        combined_df.at[index,  'written_file' + str(written_file_num) + '_type'] = 'Document'
                        combined_df.at[index,  'written_file' + str(written_file_num) + '_format'] = 'text/x-flextext+xml'
    
    #Print out stats for each bundle

    with open(current_dir + os.sep + 'IMDI_Maker_Output_Dat.csv', 'a+') as output_data_file:   
        output_data_file.write(row['name'] + ",")
        print("\n" + row['name'])
        if actor_counter > combined_df.at[index, 'total_actor_num']:
            print('WARNING: Not all actors found')
            output_data_file.write("NOT_ALL_ACTORS")
        output_data_file.write(",")
        output_data_file.write(str(combined_df.at[index, 'total_actor_num']))
        output_data_file.write(",")
        output_data_file.write(str(actor_counter))
        output_data_file.write(",")
        if combined_df.at[index, 'total_actor_num'] == 0:
            print('ERROR: No actors found')  
            output_data_file.write("NO_ACTORS")
        output_data_file.write(",")
        i=1
        while i <= combined_df.at[index, 'total_actor_num']:
            output_data_file.write(row['actor' + str(i) + '_name1'])    
            output_data_file.write(",")
            output_data_file.write(row['actor' + str(i) + '_name2'])    
            output_data_file.write(",")
            i+=1
        for item in speakers_not_found:
            output_data_file.write("Not found: " + item)    
        output_data_file.write(",")
        """
        if combined_df.at[index, 'total_media_file_num'] == 0:
            print('WARNING: No media files found')
            output_data_file.write("NO_MEDIA")
        output_data_file.write(",")
        if combined_df.at[index, 'total_written_file_num'] == 0:
            print('No written files found')
            output_data_file.write("NO_WRITTEN")
        """
        output_data_file.write("\n")
        print("\n")


for index, row in combined_df.iterrows():
    with open(current_dir + os.sep + row['name'] + '.imdi', 'w') as combined_file:

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
        combined_file.write('        <Title>' + row['project_title'] + '</Title>\n')
        combined_file.write('        <Id>' + row['project_ID'] + '</Id>\n')
        combined_file.write('        <Contact>\n')    
        combined_file.write('          <Name>' + row['project_contact1_name'] + '</Name>\n')
        combined_file.write('          <Address>' + row['project_contact1_address'] + '</Address>\n')
        combined_file.write('          <Email>' + row['project_contact1_email'] +  '</Email>\n')
        combined_file.write('          <Organisation>' + row['project_contact1_organisation'] + '</Organisation>\n')
        combined_file.write('        </Contact>\n')
        if row['project_contact2_name'] != "":
            combined_file.write('        <Contact>\n')    
            combined_file.write('          <Name>' + row['project_contact2_name'] + '</Name>\n')
            combined_file.write('          <Address>' + row['project_contact2_address'] + '</Address>\n')
            combined_file.write('          <Email>' + row['project_contact2_email'] +  '</Email>\n')
            combined_file.write('          <Organisation>' + row['project_contact2_organisation'] + '</Organisation>\n')
            combined_file.write('        </Contact>\n')
        if row['project_contact3_name'] != "":
            combined_file.write('        <Contact>\n')    
            combined_file.write('          <Name>' + row['project_contact3_name'] + '</Name>\n')
            combined_file.write('          <Address>' + row['project_contact3_address'] + '</Address>\n')
            combined_file.write('          <Email>' + row['project_contact3_email'] +  '</Email>\n')
            combined_file.write('          <Organisation>' + row['project_contact3_organisation'] + '</Organisation>\n')
            combined_file.write('        </Contact>\n')
        if row['project_contact4_name'] != "":
            combined_file.write('        <Contact>\n')    
            combined_file.write('          <Name>' + row['project_contact4_name'] + '</Name>\n')
            combined_file.write('          <Address>' + row['project_contact4_address'] + '</Address>\n')
            combined_file.write('          <Email>' + row['project_contact4_email'] +  '</Email>\n')
            combined_file.write('          <Organisation>' + row['project_contact4_organisation'] + '</Organisation>\n')
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
                combined_file.write('        <Date>' + str(row['written_file' + str(written_file_num) + '_date']) + '</Date>\n')
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

