# CSV Template Descriptions

This document describes the requirements for the .csv files used as input for LingMetaX. Two template files are provided in the GitHub project. These templates are based on the data entry forms used in the ODK Linguistic Metadata Method.

## General Requirements
The two input files should have the filenames containing the word "Participant" or "Session". The default delimiter setting for LingMetaX is a semicolon, but this can be modified using the form of the LingMetaX Google Colab Notebook or directly in the code of the Python script. The column names included in the template files constitute the only required column names. Additional columns may be present in the .csv files and will not impact the output of LingMetaX.

## Participant CSV
**full_name** The full name of the participant, with spaces in between each name.

**nickname** A nickname for the participant 

**code** An anonymous code for the participant 

**gender** The gender of the participant (Female, Male, Unknown, Other)

**birth_year** The birth year of the participant (YYYY-01-01)

**education** The educational background of the participant

**ethnic_group** The ethnic group of the participant

**primary_occupation** The primary occupation of the participant

**description** A short description of the participant

**primary_language** The ISO 639-3 code of the participant's primary language

**primary_language_additional** Any additional notes on the participant's primary language

**other_languages** The ISO 639-3 code of the participant's other languages, each separated by a semicolon

**mother_language** The ISO 639-3 code of the participant's mother's primary language

**father_language** The ISO 639-3 code of the participant's mother's primary language


## Session CSV
**date** The date of the recording session (YYYY-MM-DD)

**title** The title of the recording session (e.g. "Gudo's story about hunting a lion in the bush")

**filename** The filename for the recording session (e.g. 20200127_RGb)

**description** A short description of the recording session

**location_region** The administrative region where the recording took place

**location_continent** The continent where the recording took place (Africa, Asia, Australia, Europe, North-America, Middle-America, Oceania, South-America)

**location_country** The country where the recording took place (as listed in Lameta, e.g. "Tanzania, United Republic of")

**location_local** The town, village, or neighborhood where the recording took place.

**archive_repository** The archive or repository where the recording will be deposited (AILCA, AILLA, ANLA, ELAR, PARADISEC, REAP, TLA, Custom)

**genre** The speech genre of the recording session (See [the list of speech genres](https://github.com/rgriscom/LingMetaX/blob/main/Documentation/Speech%20Genres.md))

**subgenre** The subgenre of the recording session

**topic** The topic of the recording session (e.g. the main discussion point, or a general category of discussion content)

**keywords** One or more specific keywords related to the content of the recording session

**involvement** The involvement of the researcher during the recording session (Elicited, Non-elicited, No-observer)

**planning** The planning type of the recording session (Planned, Semi-spontaneous, Spontaneous)

**social_context** The social context of the recording session (Family, Private, Public, Controlled Environment

**subject_languages** The ISO 639-3 code of the subject or target languages of the recording session, each separated by a semicolon.

**working_languages** The ISO 639-3 code of the working languages of the recording session, each separated by a semicolon.

**access_AILCA** The access level for the recording session, if depositing with AILCA (O, U, RC, C, S, unspecified)

**access_AILLA** The access level for the recording session, if depositing with AILLA (Level 1, Level 2, Level 3, Level 4)

**access_ANLA** The access level for the recording session, if depositing with ANLA (Unrestricted access, Time limit, Restricted access)

**access_ELAR** The access level for the recording session, if depositing with ELAR (O, U, S)

**access_PARADISEC** The access level for the recording session, if depositing with PARADISEX (O, C)

**access_TLA** The access level for the recording session, if depositing with TLA (Open, Restricted, Protected, Closed)

**access_REAP** The access level for the recording session, if depositing with REAP (Entity, REAP Users, Public)

**access_custom** The access level for the recording session, if not depositing with any of the other archives or repositories

**access_explanation** An explanation of or justification for the access level.

**video** The names of any video cameras used during the recording session, each separated by a comma

**microphone** The names of any microphones used during the recording session, each separated by a comma

**audio** The names of any audio recorders used during the recording session, each separated by a comma

**other_equipment** The names of any other equipment used during the recording session, each separated by a comma

**recording_conditions** The conditions during the recording (e.g. noise from poor weather or domestic animals)

**participant_1_full_name** The full name of the first participant, exactly as it is written in the Participants.csv file

**participant_1_role** The role of the first participant (see [list of participant roles](https://github.com/rgriscom/LingMetaX/blob/main/Documentation/Participant%20Roles.md))

**participant_2_full_name** The full name of the second participant, exactly as it is written in the Participants.csv file

**participant_2_role** The role of the second participant (see [list of participant roles](https://github.com/rgriscom/LingMetaX/blob/main/Documentation/Participant%20Roles.md))

**participant_3_full_name** The full name of the third participant, exactly as it is written in the Participants.csv file

**participant_3_role** The role of the third participant (see [list of participant roles](https://github.com/rgriscom/LingMetaX/blob/main/Documentation/Participant%20Roles.md))

**participant_4_full_name** The full name of the fourth participant, exactly as it is written in the Participants.csv file

**participant_4_role** The role of the fourth participant (see [list of participant roles](https://github.com/rgriscom/LingMetaX/blob/main/Documentation/Participant%20Roles.md))

**participant_5_full_name** The full name of the fifth participant, exactly as it is written in the Participants.csv file

**participant_5_role** The role of the fifth participant (see [list of participant roles](https://github.com/rgriscom/LingMetaX/blob/main/Documentation/Participant%20Roles.md))
