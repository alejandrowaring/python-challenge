import os
import csv
csvpath = os.path.join('.','Resources','budget_data.csv')

differences = []
difference = 0
last_int = 0

with open(csvpath, 'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    next(csvreader)
    total = sum()
    for row in csvreader:
        #find the differences between current and last 
        difference = int(row[1]) - int(last_int)
        last_int = row[1]
        differences.append(difference)  

differences.pop(0)
difference_average = round(sum(differences) / len(differences),2)
difference_max = max(differences)
difference_min = min(differences)
#print(difference_average)
#print(len(differences))
#print(differences)

out_file = os.path.join('.','Analysis', 'budget_data_analysis.txt')
#Delete old contents of the file 
open(out_file,"w").close()

#Write the header into the file
f = open(out_file,'a')
f.write("Financial Analysis \n")
f.write("----------------------------")
f.write("\n")

#f.write("Total Months: " str(file_len))
f.write("Total: ")
f.write("Average  Change: $" + str(difference_average) + "\n" )
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits: Sep-2013 ($-2196167)
