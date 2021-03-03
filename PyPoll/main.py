import os
# Module for reading CSV files
import csv

#Set the csv path to get the data
csvpath = os.path.join('Resources','election_data.csv')

#Variables
vote_count = 0
candidate_name = []
votes_per_candidate = [0,0,0,0]
candidate_dict = {}
candidate_vote = {}
candidate_percent = {}

#Reads the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    #Loop through to get total vote count
    for rows in csvreader:
        #Adds 1 to each row in our vote_count
        vote_count += 1
        #look at our candidates 
        if rows[2] not in candidate_name:
            #adds our candidate to our list if not already in it
            candidate_name.append(rows[2])

        for i in range(len(candidate_name)):
            if rows[2] == candidate_name[i]:
                votes_per_candidate[i] += 1
#Adds each value from the lists to the corresponding dictionaries
for i in range(len(candidate_name)):
    candidate_dict[f"Candidate Name {i}"] = candidate_name[i]
    candidate_vote[f"Candidate Name {i}"] = votes_per_candidate[i]
#Adds the percents to its own dictionary
    candidate_percent[f"Candidate Name {i}"] = (candidate_vote[f"Candidate Name {i}"] / vote_count) * 100

#Set winner variable
winner = "Candidate Name 0"

#Compares the votes each candidate has, and sets the variable to the key of the dictionary
for i in range(len(candidate_name)-1):
   if candidate_vote[f"Candidate Name {i+1}"] > candidate_vote[f"Candidate Name {i}"]:
       winner = f"Candidate Name {i+1}"


#Output, Summary of the result
print("Election Results")
print("----------------------------------")
print(f"Total Votes: {vote_count}")
print("----------------------------------")
for i in range(len(candidate_name)):
    print(f"{candidate_dict[f'Candidate Name {i}']}: {candidate_percent[f'Candidate Name {i}']:.3f}% ({candidate_vote[f'Candidate Name {i}']})")
print("----------------------------------")
print(f"Winner: {candidate_dict[winner]}")
print("----------------------------------")

Pypoll_analysis = os.path.join("analysis", "Pypoll_analysis.txt")

with open (Pypoll_analysis , "w") as text:
    text.write("Election Results \n")
    text.write("---------------------------------- \n")
    text.write(f"Total Votes: {vote_count} \n")
    text.write("---------------------------------- \n")
    for i in range(len(candidate_name)):
        text.write(f"{candidate_dict[f'Candidate Name {i}']}: {candidate_percent[f'Candidate Name {i}']:.3f}% ({candidate_vote[f'Candidate Name {i}']}) \n")
    text.write("----------------------------------\n")
    text.write(f"Winner: {candidate_dict[winner]} \n")
    text.write("---------------------------------- \n")

    text.close()