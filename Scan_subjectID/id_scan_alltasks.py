import csv
import os

#EDIT LINE 22 TO CONTAIN EXACT HEADER NAMES IN STARTING CSV
#EDIT LINE 49 TO CONTAIN NAMES OF DIRECTORIES TO SEARCH. MUST MATCH HEADERS IN LINE 22 EXACTLY. CASE SENSITIVE.
#EDIT BASE PATH IN LINE 44. SHOULD BE THE DIRECTORY THAT CONTAINS ALL 12 TASK DIRECTORIES.
#PLACE MASTER_FILE.CSV IN YOUR BASE PATH DIRECTORY. MASTER HAS HEADERS 'ID' AND NAME OF EACH TASK. ADD SUB ID'S FOR SCRIPT TO CHECK IN COLUMN 1.

def write_csv(filepath, data):
    """
    This function takes a csv filepath and a list of dictionaries as arguments and outputs them
    to the specified csv file. 

    Parameters:
        filepath (str): A filepath of a csv file to be written to
        data (list): A list of dictionaries, each representing a subject and whether they completed the task

    Returns:
        None
    """
    with open(filepath, 'w') as csv_file:
        fieldnames = ['ID', 'PlusMinus', 'NumberLetter']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
        writer.writeheader()
        for line in data:
            writer.writerow(line)

def read_csv(filepath):
    """Returns a list of dictionaries where each dictionary is formed from the data.

    Parameters:
        filepath (str): a filepath that includes a filename with its extension

    Returns:
        list: a list of dictionaries where each dictionary is formed from the data
        example dictionary format it produces is:  {'ID': subjectIDnumber, 'taskname1': " ", 'taskname2': " ",}
        One dictionary is created for each subject ID listed in the master CSV. 
    """

    with open(filepath, mode='r', newline='', encoding='utf-8-sig') as file_obj:
        data = list(csv.DictReader(file_obj))
    return data

base_path = '/Users/daliak/Documents/umich/courses/si506/practice'
#read in master CSV
csv_dicts = read_csv(f"{base_path}/master_file.csv")
print(csv_dicts)
# create list of directory names. There is a directory for each task.
folder_list = ['PlusMinus', 'NumberLetter']
#loop through directory names
for folder in folder_list:
    #accumulator 
    file_list = []
    # read the names of each item in the folder
    with os.scandir(f"{base_path}/{folder}") as listOfEntries:
        for entry in listOfEntries:
            # if the entry is a file, add the first three characters of its name to the file_list accumulator
            # these first three characters represent the subject ID. File only exists with that subj ID if they completed that task.
            if entry.is_file():
                file_list.append(entry.name[0:3])
    #loop through list of dictionaries we created (one for each subject ID)
    #if that subject ID is present in the file_list, they must have completed that task so assign a value of 1 to that key associated with that task/folder (which share a name)
    #if subject  subject ID not present in file_list, assign value as 0.
    for subj in csv_dicts:
        if subj['ID'] in file_list:
            subj[folder] = 1
        else:
            subj[folder] = 0

print("")
print(csv_dicts)

#write out CSV that now containes 0's and 1's representing each subject's completion status for each task.
write_csv('completion_results.csv', csv_dicts)