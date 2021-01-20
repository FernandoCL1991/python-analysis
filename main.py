## PYPOLL SCRIPT ## WORK IT!!!!

#%%
##IMPORTING MODULES TO RUN THE SCRIPT
import os
import csv

##CREATING VARIABLES
total_votes=[]
total_votes = dict()


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
    print(f"The total number of voters is: {counter}.") ##TOTAL NUMBER OF VOTES CAST.

    candidate=row[2]
    print(candidate)
#%%
    if candidate not in total_votes:
        total_votes[candidate]=0
        total_votes[candidate]+=1
        print(total_votes)
#%%
    for candidate, vote_count in total_votes():
        print(f"{candidate} received {str(vote_count)} votes.") ##COMPLETE LIST OF CANDIDATES WHO RECEIVED VOTES




   
# %%
