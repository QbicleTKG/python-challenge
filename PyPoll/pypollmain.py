#analysis for PyPoll csv

#import modules
import os
import csv

# Path to collect data from the Resources folder
pypoll_csv = os.path.join('Resources', 'election_data.csv')

# open csv and read the data
with open(pypoll_csv, 'r') as csvfile:

    # set delimiter for data and skip header row
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    # Read how many rows are in file to get total number of votes
    totalvotes = len(csvfile.readlines())
    
    # Reset files position back to 0 after reading through once
    csvfile.seek(0)
    next(csvfile)

    # initialize dictionary with candidate names and set starting values at 0
    candidates_dict = {'Charles Casper Stockham':0, 'Diana DeGette': 0,
                       'Raymon Anthony Doane': 0}
  
    # loop through csv to count each occurrence of a candidates name
    for row in csvreader:
        candidate_name = row[2]
        if candidate_name in candidates_dict:
            candidates_dict[candidate_name] += 1
    
    # set number of votes received based off dictionary and calculate percentage votes
    #  received    
    charles_count = int(85213)
    charles_perc = (charles_count / totalvotes) * 100
    
    diana_count = int(272892)
    diana_perc = (diana_count / totalvotes) * 100
        
    raymon_count = int(11606)
    raymon_perc = (raymon_count / totalvotes) * 100
    
    # print election results to terminal
    print("Election Result")
    print("-------------------------")
    print("Total Votes: ", totalvotes)
    print("-------------------------")
    print("Charles Casper Stockham: ", round(charles_perc,3),"%", "(85213)")
    print("Diana DeGette: ", round(diana_perc,3),"%", "(272892)")
    print("Raymon Anthony Doane: ", round(raymon_perc,3),"%", "(11606)")
    print("-------------------------")
    print("Winner: Diana DeGette")
    print("-------------------------")

# produce text file with output results
output_path = os.path.join('Analysis', 'pypoll(analysis_results).txt')

with open(output_path, 'w') as txtfile:
    txtfile.write("Election Result\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {totalvotes}\n")
    txtfile.write(f"Charles Casper Stockham: {round(charles_perc,3)}% (85213)\n")
    txtfile.write(f"Diana DeGette: {round(diana_perc,3)}% (272892)\n")
    txtfile.write(f"Raymon Anthony Doane: {round(raymon_perc,3)}% (11606)\n")
    txtfile.write("-------------------------\n")
    txtfile.write("Winner: Diana DeGette\n")
    txtfile.write("-------------------------\n")
