import os
import csv
csvpath = os.path.join('.','Resources','budget_data.csv')

differences = []
difference = 0
last_int = 0
total = 0
months = 0
largest_increase = 0
largest_increase_month = ""
largest_decrease = 0
largest_decrease_month = ""

with open(csvpath, 'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    next(csvreader)
    for row in csvreader:
        #find the differences between current and last 
        difference = int(row[1]) - int(last_int)
        last_int = row[1]
        if int(row[1]) > int(largest_increase):
            largest_increase = row[1]
            largest_increase_month = row[0]
        if int(row[1]) < int(largest_decrease):
            largest_decrease = row[1]
            largest_decrease_month = row[0]
        differences.append(difference)  
        total = total + int(row[1])
        months += 1

differences.pop(0)
difference_average = round(sum(differences) / len(differences),2)
difference_max = max(differences)
difference_min = min(differences)

out_file = os.path.join('.','Analysis', 'budget_data_analysis.txt')
#Delete old contents of the file 
open(out_file,"w").close()

#Write the header into the file
with open(out_file,'a') as f:
    f.write("Financial Analysis \n")
    f.write("----------------------------")
    f.write("\n")
    f.write("Total Months: " + str(months) + "\n")
    f.write("Total: $" + str(total) + "\n")
    f.write("Average  Change: $" + str(difference_average) + "\n" )
    f.write("Greatest Increase in Profits: " + largest_increase_month + " ($" + str(largest_increase) + ")\n")
    f.write("Greatest Decrease in Profits: " + largest_decrease_month + " ($" + str(largest_decrease) + ")\n")


with open(out_file, 'r') as text:
    lines = text.read()
    print(lines)
