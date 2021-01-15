
import os, datetime, pandas as pd
from datetime import datetime
import os
CSV_Delimiter = ';'

list_of_roles = [
                'Annotator',
                'Author',
                'Careful Speech Speaker',
                'Compiler',
                'Consultant',
                'Data Inputter',
                'Depositor',
                'Developer',
                'Editor',
                'Illustrator',
                'Interpreter',
                'Interviewer',
                'Participant',
                'Performer',
                'Photographer',
                'Recorder',
                'Researcher',
                'Research Participant',
                'Responder',
                'Signer',
                'Singer',
                'Speaker',
                'Sponsor',
                'Transcriber',
                'Translator'
                ]

current_dir = os.path.dirname(__file__)
output_path = current_dir + os.sep + "LingMetaX_Output"
print(current_dir)
print(output_path)


os.mkdir(output_path)
  
list_of_files = []

if CSV_Delimiter == "Tab":
  formatted_delimiter = "\t"
else:
  formatted_delimiter = CSV_Delimiter

assert "Sessions.csv" in os.listdir(),"Sessions.csv file not uploaded."
assert "Participants.csv" in os.listdir(),"Participants.csv file not uploaded."

combined_df = pd.read_csv(current_dir + '/Sessions.csv',header=0,delimiter=formatted_delimiter)
speaker_df = pd.read_csv(current_dir + '/Participants.csv',header=0,delimiter=formatted_delimiter)

combined_df = combined_df.applymap(str)
combined_df = combined_df.replace(to_replace="nan",value="")
speaker_df = speaker_df.applymap(str)
speaker_df = speaker_df.replace(to_replace="nan",value="")

project_title = "Project"
project_folder = output_path + os.sep + project_title
description_folder = output_path + os.sep + project_title + os.sep + "DescriptionDocuments"
other_folder = output_path + os.sep + project_title + os.sep + "OtherDocuments"
people_folder = output_path + os.sep + project_title + os.sep + "People"
session_folder = output_path + os.sep + project_title + os.sep + "Sessions"
os.mkdir(project_folder)
print(project_folder)
os.mkdir(description_folder)
os.mkdir(other_folder)
os.mkdir(people_folder)
os.mkdir(session_folder)
with open(project_folder + "/"+ project_title + '.sprj', 'w') as project_file:
    project_file.write('<?xml version="1.0" encoding="utf-8" ?>\n')
    project_file.write('<Project>\n')
    project_file.write('\t<Iso639Code />\n')
    project_file.write('\t<transcriptionFont />\n')
    project_file.write('\t<freeTranslationFont />\n')
    project_file.write('\t<AutoSegmentersettings minSegmentLength="0" maxSegmentLength="0" preferrerdPauseLength="0" optimumLengthClampingFactor="0" />\n')
    project_file.write('\t<Title></Title>\n')
    project_file.write('\t<FundingProjectTitle></FundingProjectTitle>\n')
    project_file.write('\t<ProjectDescription></ProjectDescription>\n')
    project_file.write('\t<VernacularISO3CodeAndName></VernacularISO3CodeAndName>\n')
    project_file.write('\t<Location />\n')
    project_file.write('\t<Region></Region>\n')
    project_file.write('\t<Country></Country>\n')
    project_file.write('\t<Continent></Continent>\n')
    project_file.write('\t<ContactPerson />\n')
    project_file.write('\t<AccessProtocol>custom</AccessProtocol>\n')
    project_file.write('\t<ContentType />\n')
    project_file.write('\t<Applications />\n')
    project_file.write('\t<RightsHolder />\n')
    project_file.write('\t<Depositor />\n')
    project_file.write('\t<RelatedPublications />\n')
    project_file.write('\t<customAccessChoices>show,hide</customAccessChoices>\n')
    project_file.write('</Project>\n')


#Merge data from session_df, project_df, and speaker_df
for index, row in combined_df.iterrows():
    #Merge speaker data
    actor_num = 1
    combined_df.at[index, 'total_actor_num'] = 0
    speakers_not_found = []
    while actor_num < 6:
        actor_check = 0
        for s_index, s_row in speaker_df.iterrows():

            #IF the first and second name match
            if row['speaker_' + str(actor_num) + '_full_name'] == s_row['full_name'] and actor_check == 0:
                if actor_num == 1:
                  all_actor_names_list = []
                  all_actor_names_list.append(row['speaker_' + str(actor_num) + '_full_name'])
                else:
                  all_actor_names_list.append(row['speaker_' + str(actor_num) + '_full_name'])                
                actor_check = 1

                #Make the .person file
                person_folder = "LingMetaX_Output/" + project_title + "/People/" + s_row['full_name'].replace(" ","\ ").replace("\'","\\'")
                os.mkdir(person_folder)              
                with open(person_folder.replace("\ "," ").replace("\\'","\'") + '/' + s_row['full_name'] + '.person', 'w') as person_file:
                  person_file.write('<?xml version="1.0" encoding="utf-8" ?>\n')
                  person_file.write('<Person minimum_lameta_version_to_read="0.0.0">\n')
                  person_file.write('\t<name type="string">' + s_row['full_name'] + '</name>\n')
                  person_file.write('\t<nickName type="string">' + s_row['nickname'] + '</nickName>\n')
                  person_file.write('\t<code type="string">' + s_row['code'] + '</code>\n')
                  if s_row['primary_language'] != "other":
                    person_file.write('\t<primaryLanguage type="string">' + s_row['primary_language'] + '</primaryLanguage>\n')
                  else: 
                    person_file.write('\t<primaryLanguage type="string">' + s_row['primary_language_other'] + '</primaryLanguage>\n')
                  
                  person_file.write('\t<primaryLanguageLearnedIn type="string">' + s_row['primary_language_additional'] + '</primaryLanguageLearnedIn>\n')
                  
                  if s_row['other_languages'] != "other":
                    other_language_counter = 0
                    for other_language_entry in s_row['other_languages'].split(" "):
                      person_file.write('\t<otherLanguage' + str(other_language_counter) + ' type="string">' + other_language_entry + '</otherLanguage' + str(other_language_counter) + '>\n')
                      other_language_counter+=1
                  else:                 
                    person_file.write('\t<otherLanguage0 type="string">' + s_row['other_languages_other'] + '</otherLanguage0>\n')

                  if s_row['father_language'] != "other":
                    person_file.write('\t<fathersLanguage type="string">' + s_row['father_language'] + '</fathersLanguage>\n')
                  else: 
                    person_file.write('\t<fathersLanguage type="string">' + s_row['father_language_other'] + '</fathersLanguage>\n')

                  if s_row['mother_language'] != "other":
                    person_file.write('\t<mothersLanguage type="string">' + s_row['mother_language'] + '</mothersLanguage>\n')
                  else: 
                    person_file.write('\t<mothersLanguage type="string">' + s_row['mother_language_other'] + '</mothersLanguage>\n')
                  person_file.write('\t<education type="string">' + s_row['education'] + '</education>\n')
                  person_file.write('\t<birthYear type="string">' + s_row['birth_year'].split('-')[0] + '</birthYear>\n')
                  person_file.write('\t<gender type="string">' + s_row['gender'] + '</gender>\n')
                  if s_row['ethnic_group'] != "other":
                    person_file.write('\t<ethnicGroup type="string">' + s_row['ethnic_group'] + '</ethnicGroup>\n')
                  else:
                    person_file.write('\t<ethnicGroup type="string">' + s_row['ethnic_group_other'] + '</ethnicGroup>\n')
                  person_file.write('\t<primaryOccupation type="string">' + s_row['primary_occupation'] + '</primaryOccupation>\n')
                  person_file.write('\t<description type="string">' + s_row['description'] + '</description>\n')
                  
                  person_file.write('\t<CustomFields>\n')
                  person_file.write('\t</CustomFields>\n')
                  person_file.write('</Person>\n')
        actor_num+=1
    #Create session metadata
    session_folder = "LingMetaX_Output/" + project_title + "/Sessions/" + row['filename']
    os.mkdir(session_folder)              
    with open(session_folder + '/' + row['filename'] + '.session', 'w') as session_file:
      session_file.write('<?xml version="1.0" encoding="utf-8"?>\n')
      session_file.write('<Session minimum_lameta_version_to_read="0.0.0">\n')
      session_file.write('\t<title type="string">' + row['title'] + '</title>\n')
      session_file.write('\t<languages type="string">' + row['subject_languages'] + '</languages>\n')
      session_file.write('\t<workingLanguages type="string">' + row['working_languages'] + '</workingLanguages>\n')
      
      if row['genre'] != "other":
        session_file.write('\t<genre type="string">' + row['genre'] + '</genre>\n')
      else:
        session_file.write('\t<genre type="string">' + row['other_Genre'] + '</genre>\n')
      session_file.write('\t<Sub-Genre type="string">' + row['subgenre'] + '</Sub-Genre>\n')
      session_file.write('\t<location type="string">' + row['location'] + '</location>\n')
      if row['Archive_Repository'] == "ELAR":
        session_file.write('\t<access type="string">' + row['access_ELAR'] + '</access>\n')
      if row['Archive_Repository'] == "AILCA":
        session_file.write('\t<access type="string">' + row['access_AILCA'] + '</access>\n')
      if row['Archive_Repository'] == "AILLA":
        session_file.write('\t<access type="string">' + row['access_AILLA'] + '</access>\n')
      if row['Archive_Repository'] == "ANLA":
        session_file.write('\t<access type="string">' + row['access_ANLA'] + '</access>\n')
      if row['Archive_Repository'] == "PARADISEC":
        session_file.write('\t<access type="string">' + row['access_PARADISEC'] + '</access>\n')
      if row['Archive_Repository'] == "TLA":
        session_file.write('\t<access type="string">' + row['access_TLA'] + '</access>\n')
      if row['Archive_Repository'] == "REAP":
        session_file.write('\t<access type="string">' + row['access_REAP'] + '</access>\n')
      if row['Archive_Repository'] == "Custom":
        session_file.write('\t<access type="string">' + row['access_Custom'] + '</access>\n')
      session_file.write('\t<synopsis type="string">' + row['description'] + '</synopsis>\n')
      session_file.write('\t<status type="string">Incoming</status>\n')
      session_file.write('\t<date type="string">' + row['date'] + '</date>\n')
      session_file.write('\t<keyword type="string">' + row['keywords'] + '</keyword>\n')
      session_file.write('\t<topic type="string">' + row['topic'] + '</topic>\n')
      all_actor_names_string = ""
      i = 1
      print(all_actor_names_list)
      for actor_name in all_actor_names_list:
          j = 0
          while j <= row['participant_' + str(i) + '_role'].count(" "):
            all_actor_names_string += actor_name + ";"
            j+=1
          i+=1
      print(all_actor_names_string)
      session_file.write('\t<participants type="string">' + all_actor_names_string + '</participants>\n')
      session_file.write('\t<contributions type="xml">\n')
      i = 1
      while i <= len(all_actor_names_list):
        for role_label in list_of_roles:
          session_file.write('\t\t<contributor>\n')
          session_file.write('\t\t\t<name>' + row['participant_' + str(i) + '_full_name'] + '</name>\n')
          session_file.write('\t\t\t<role>' + role_label + '</role>\n')   
          session_file.write('\t\t\t<date>0001-01-01</date>\n')
          session_file.write('\t\t</contributor>\n')
        i+=1
      session_file.write('\t</contributions>\n')
      session_file.write('\t<AdditionalFields type="xml">\n')
      session_file.write('\t\t<Involvement type="string">' + row['interactivity'] + '</Involvement>\n')
      session_file.write('\t\t<Location_Region type="string">' + row['location_region'] + '</Location_Region>\n')
      session_file.write('\t\t<Location_Country type="string">' + row['location_country'] + '</Location_Country>\n')
      session_file.write('\t\t<Location_Continent type="string">' + row['location_continent'] + '</Location_Continent>\n')
      session_file.write('\t\t<Planning_Type type="string">' + row['planning'] + '</Planning_Type>\n')
      if row['Social_Context'] != "":
        session_file.write('\t\t<Social_Context type="string">' + row['social_context'] + '</Social_Context>\n')
      session_file.write('\t</AdditionalFields>\n')
      session_file.write('</Session>\n')
