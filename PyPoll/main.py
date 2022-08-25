# Import os and csv:

import os
import csv 


# Choose file's location to be the same as the .py file:
os.chdir(os.path.dirname(__file__))

# Print the current working directory:
print("This program is running from: " + os.getcwd())

# Use relative path to get to csv
csvpath = os.path.join("Resources", "election_data.csv")

# Print CSV path:
print("The csvpath is: " + csvpath)

# Open "election_data.csv" file:
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


# Read header row first:
    csv_header = next(csvreader)

# Create the following empty lists to be populated later:
    total_votes = []
    candidates = []
    unique_candidates = []


# Finding out the total number of votes:
    for row in csvreader:
        total_votes.append(row[0])
        candidates.append(row[2])

# Finding candidate list:
    for i in candidates:
        if i not in unique_candidates:
            unique_candidates.append(i)


# Find total number of votes for each candidate: 
Charles_votes = candidates.count('Charles Casper Stockham')

Diana_votes = candidates.count('Diana DeGette')

Raymon_votes = candidates.count('Raymon Anthony Doane')

# Find out winner based on popular vote:
winner = Charles_votes

if Diana_votes > winner:
    winner = Diana_votes 
elif Raymon_votes > winner:
    winner = Raymon_votes

if Diana_votes == winner:
    winner = 'Diana DeGette'
elif Raymon_votes == winner:
    winner = 'Raymon Anthony Doane'
else:
    winner = 'Charles Casper Stockham'

# Print vales as shown below:
print("Election Results")
print("-------------------------")
print(f"Total Votes: {len(total_votes)}")
print("-------------------------")
print(f"Charles Casper Stockham: {round((Charles_votes/len(total_votes))*100,3)}% ({Charles_votes})")
print(f"Diana DeGette: {round((Diana_votes/len(total_votes))*100,3)}% ({Diana_votes})")
print(f"Raymon Anthony Doane: {round((Raymon_votes/len(total_votes))*100,3)}% ({Raymon_votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Write values to a new file called output.txt:
output_path = os.path.join("analysis", "output.txt")
with open(output_path, 'w') as csv_output:
    csv_output.write("Election Results\n")
    csv_output.write("-------------------------\n")
    csv_output.write(f"Total Votes: {len(total_votes)}\n")
    csv_output.write("-------------------------\n")
    csv_output.write(f"Charles Casper Stockham: {round((Charles_votes/len(total_votes))*100,3)}% ({Charles_votes})\n")
    csv_output.write(f"Diana DeGette: {round((Diana_votes/len(total_votes))*100,3)}% ({Diana_votes})\n")
    csv_output.write(f"Raymon Anthony Doane: {round((Raymon_votes/len(total_votes))*100,3)}% ({Raymon_votes})\n")
    csv_output.write("-------------------------\n")
    csv_output.write(f"Winner: {winner}\n")
    csv_output.write("-------------------------\n")





