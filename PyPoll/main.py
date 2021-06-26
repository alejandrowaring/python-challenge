#Imports
import os
import csv
#paths to files we are going to read and write
csvpath = os.path.join('.','Resources','election_data.csv')
out_file = os.path.join('.','Analysis','election_results.txt')
#Define variables and lists we are going to use
cand_col = 2
total = 0
candidates = []
candidate_count = []
#open the csv file
with open(csvpath, 'r') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)
    #Loop over each row in the csv
    for row in csvreader:
        #if the name hasn't appeared before, add it to the list of candidates available
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_count.append(0)
        #find the index of the candidate of the voter, and add 1 to their corresponding index in the candidate_count list
        indx = candidates.index(row[2])
        candidate_count[indx] += 1

#find out how many candidates there were and the total number of votes
num_cand = len(candidates) 
total = sum(candidate_count)
#Find who the winner was
winner = candidates[candidate_count.index(max(candidate_count))]

#clear out the old file
open(out_file,"w").close()
#start appending to the new, clean file
with open(out_file,'a') as text:
    #print out the headers
    text.write("Election Results \n------------------------- \n")
    #print out the total votes
    text.write("Total Votes: " + str(total) + "\n-------------------------\n")
    #Figure out the candidate's percentages
    for i in range(num_cand):
        current_candidate = candidates[i]
        current_count = candidate_count[i]
        perc = '{:.2%}'.format(round(current_count / total,2))
        #Print out all their results to the file
        text.write(current_candidate + ": " + str(perc) + " (" + str(current_count) + ") \n")
    #write out the winner
    text.write("-------------------------\n")
    text.write("Winner: " + winner + "\n-------------------------")

#Read out the file to the user in the terminal
with open(out_file, 'r') as text:
    lines = text.read()
    print(lines)
