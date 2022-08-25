# Import os and csv:

import os
import csv 


# Choose file's location to be the same as the .py file:
os.chdir(os.path.dirname(__file__))

# Print the current working directory:
print("This program is running from: " + os.getcwd())


# Use relative path to get to csv
csvpath = os.path.join('Resources', 'budget_data.csv')


# Print CSV path:
print("The csvpath is: " + csvpath)

# Open "budget_data.csv" file:
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# Read header row first:
    csv_header = next(csvreader)

# Create empty lists for the following:
    month_count = []
    profit = []
    profit_change = []
    
# Loop through all rows to populate month_count and profit lists:
    for row in csvreader:
        month_count.append(row[0])
        profit.append(int(row[1]))

# Loop through the profit list to calculate the profit change:
    for i in range(len(profit)-1):
        profit_change.append(profit[i+1] - profit[i])

# Find greatest increase and decrease in profit change:
increase = max(profit_change)
decrease = min(profit_change)

#Find the index of both the increase and decrease calculated above:
highest_change = profit_change.index(increase)+1
lowest_change = profit_change.index(decrease)+1

# Print vales as shown below:
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {month_count[highest_change]} (${increase})")
print(f"Greatest Decrease in Profits: {month_count[lowest_change]} (${decrease})")

# Write values to a new file called output.txt:
output_path = os.path.join("analysis", "output.txt")
with open(output_path, 'w') as csv_output:
    csv_output.write("Financial Analysis\n")
    csv_output.write("---------------------------\n")
    csv_output.write(f"Total Months: {len(month_count)}\n")
    csv_output.write(f"Total: ${sum(profit)}\n")
    csv_output.write(f"Average Change: ${round(sum(profit_change)/len(profit_change),2)}\n")
    csv_output.write(f"Greatest Increase in Profits: {month_count[highest_change]} (${increase})\n")
    csv_output.write(f"Greatest Decrease in Profits: {month_count[lowest_change]} (${decrease})\n")

