## PYBANK SCRIPT

##IMPORTING MODULES TO RUN THE SCRIPT
import os
import math
from statistics import mean

##IMPORTING CSV READING MODULE
import csv

#CREATING THE PATH TO THE DOCUMENT
csvpath= os.path.join("Resources", "budget_data.csv")
print(csvpath)

#CREATING VARIABLES
sum_months=[]
net_change_list=[]

#READ THE CSV FILE
with open(csvpath, 'r') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')

    #CONSIDER THE DATA AFTER THE HEADER , AND SAVE IT AS HEADER
    csvheader= next(csvreader)
    
    first_row = next(csvreader)

    current_net = first_row[1]
    
    max_change = 0
    min_change = 0

    
    for row in csvreader:
        sum_months.append(row[0]) #TOTAL NUMBER OF MONTHS IN THE DATASET.
        previous_net = current_net #SETTING EQUALITY TO START THE FIRST LOOP AND ALSO APPLYING IT TO THE UPCOMING ONES.
        current_net=row[1]

        net_change = float(current_net) - float(previous_net) #NET TOTAL AMOUNT OF PROFIT/LOSSES OVER THE PERIOD.
        net_change_list.append(net_change)
        if net_change > max_change: #GREATEST INCREASE IN PROFIT.
            max_change = net_change
        if net_change < min_change: #GREATEST DECREASE IN PROFIT.
            min_change = net_change


net_change_average = mean(net_change_list) #RETRIEVING net_change AND APPLYING mean TO GET AVERAGE OF NET CHANGES.
total_amount= sum(net_change_list) #TOTAL AMOUNT OF NET CHANGES.

output_file = (
    "Financial Analysis"    
    "----------------------------------"
    f"Total Months: {len(sum_months)}"
    f"Total: ${total_amount}"
    f"Average Change: ${net_change_average}")
print(output_file)

#PRINT ANALYSIS TO THE TERMINAL AND EXPORT A TEXT FILE WITH THE RESULTS.

with open(output_file, "w", newline="") as datafile: #OPEN OUTPUT FILE.
    writer = csv.writer(datafile)

    # WRITE THE HEADER ROW.
    writer.writerow(["Date", "Profit/Losses"])
    