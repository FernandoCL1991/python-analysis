#CREATING FILE PATH
import os

#IMPORTING CSV READING MODULE
import csv

#CREATING THE PATH TO THE DOCUMENT
csvpath= os.path.join("Resources", "budget_data.csv")
print(csvpath)

#CREATING VARIABLES
sum_months=[]
total=[]

#READ THE CSV FILE
with open(csvpath, "r") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")

    #CONSIDER THE DATA AFTER THE HEADER , AND SAVING IT AS A HEADER
    csvheader= next(csvreader)

    #RETRIEVING TOTAL DATES IN DATASET
    for row in csvreader:
        sum_months.append(row[0])
    print(f"The total number of months in the dataset is: {len(sum_months)}")


