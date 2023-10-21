# analysis for PyBank csv

#import modules
import os
import csv

# Path to collect data from the Resources folder
pybank_csv = os.path.join('Resources', 'budget_data.csv')

# open csv and read the data
with open(pybank_csv, 'r') as csvfile:

    # set delimiter for data and skip header row
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Read how many rows are in file to get toal number of months
    totalmonths = len(csvfile.readlines())

    
    
    # Reset files position back to 0 after reading through once
    csvfile.seek(0)
    next(csvfile)

    # start getting csv data into lists to manipulate, 
    # set header names first
    date_index = header.index('Date')
    profit_loss_index = header.index('Profit/Losses')
    
    #create open lists
    months = []
    allprofits = []

    # loop through csv and append data to lists
    for row in csvreader:
        months.append(row[date_index])
        allprofits.append(int(row[profit_loss_index]))
    
    # set variable to hold total profits/losses amount
    total_profit_loss = sum(allprofits)
    

    # set dictionary and loop to find change between each line of profits
    # and losses
    changes = {}
    for i in range(1, len(allprofits)):
        month = months[i]
        change = allprofits[i] - allprofits[i - 1]
        changes[month] = change

    # average the changes in the new list to find average change
    average_change = sum(changes.values()) / len(changes)
    
    # find greatest increase and decrease between months
    month_greatest_increase = max(changes, key=changes.get)
    month_greatest_decrease = min(changes, key=changes.get)

    #print results
    print("Financial Analysis")
    print("----------------------------") 
    print("Total Months:", totalmonths)
    print("Total: $",total_profit_loss)
    print("Average Change: $",round(average_change, 2))
    print(f"Greatest Increase: {month_greatest_increase} (${changes[month_greatest_increase]})")
    print(f"Greatest Decrease: {month_greatest_decrease} (${changes[month_greatest_decrease]})")

# produce text file with output results
output_path = os.path.join('Analysis', 'pybank(analysis_results).txt')

with open(output_path, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {totalmonths}\n")
    txtfile.write(f"Total: ${total_profit_loss}\n")
    txtfile.write(f"Average Change: ${round(average_change, 2)}\n")
    txtfile.write(f"Greatest Increase: {month_greatest_increase} (${changes[month_greatest_increase]})\n")
    txtfile.write(f"Greatest Decrease: {month_greatest_decrease} (${changes[month_greatest_decrease]})\n")


