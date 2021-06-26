#imports
import os
import csv

#files we are going to use
csvpath = os.path.join('.','Resources','budget_data.csv')
out_file = os.path.join('.','Analysis', 'budget_data_analysis.txt')
#Define all the variable values we are going to use
differences = []
difference = 0
last_int = 0
total = 0
months = 0
largest_increase = 0
largest_increase_month = ""
largest_decrease = 0
largest_decrease_month = ""
#Open the csv file
with open(csvpath, 'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csvheader=next(csvreader)
    #loop over each row and extract what we need
    for row in csvreader:
        #find the differences between current and last 
        difference = int(row[1]) - int(last_int)
        last_int = row[1]
        #find the largest increase row and extract the month and value
        if int(row[1]) > int(largest_increase):
            largest_increase = row[1]
            largest_increase_month = row[0]
        #find the largest decrease row and extract the month and value
        if int(row[1]) < int(largest_decrease):
            largest_decrease = row[1]
            largest_decrease_month = row[0]
        #Append the difference to the difference list
        differences.append(difference)
        #add the current loss/profit to the total
        total = total + int(row[1])
        #count the number of months
        months += 1

#Remove First entry since its not actually the difference between 2 results
differences.pop(0)
#find the average of all the differences
difference_average = round(sum(differences) / len(differences),2)



#Delete old contents of the file so we can start fresh
open(out_file,"w").close()

#Write the contents into the file
with open(out_file,'a') as f:
    f.write("Financial Analysis \n")
    f.write("----------------------------")
    f.write("\n")
    f.write("Total Months: " + str(months) + "\n")
    f.write("Total: $" + str(total) + "\n")
    f.write("Average  Change: $" + str(difference_average) + "\n" )
    f.write("Greatest Increase in Profits: " + largest_increase_month + " ($" + str(largest_increase) + ")\n")
    f.write("Greatest Decrease in Profits: " + largest_decrease_month + " ($" + str(largest_decrease) + ")\n")

#Read out the file to the user in the terminal
with open(out_file, 'r') as text:
    lines = text.read()
    print(lines)
