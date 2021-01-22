## PYPOLL SCRIPT ## WORK IT!!!!   COPIA ORIGINAL

#%%
##IMPORTING MODULES TO RUN THE SCRIPT
import os
import csv

##CREATING VARIABLES
total_votes=[]
unique_list=[]
candDict={}


#CREATING THE PATH TO THE DOCUMENT
csvpath = os.path.join ("Resources", "election_data.csv")
print(csvpath)

#READ THE CSV FILE
with open(csvpath, "r") as datafile: 
    csvreader = csv.reader(datafile, delimiter= ",")

    #OMIT THE HEADER AND STORE IT AS A VARIABLE
    csvheader = next(csvreader)

    counter= 0
    #FOR EACH ROW IN csv.reader:
    for row in csvreader:
        counter=counter+1
        candidates=row[2] ##TOTAL NUMBER OF VOTES.
        if candidates not in unique_list:
            unique_list.append(candidates) ##LIST OF CANDIDATES WHO RECEIVED VOTES.
       
print(f"The total number of votes is: {counter}.") ##TOTAL NUMBER OF VOTES.
print(f"The entire list of candidates is: {str(unique_list)}.") ##COMPLETE LIST OF CANDIDATES.