import os
# Module for reading CSV files
import csv

#Set the csv path to get the data
csvpath = os.path.join('Resources','budget_data.csv')

month_count = 0
month = []
total_profit_loss = 0
profit_loss = []
delta_value = []
greatest_profit = 0
least_profit = 0


#Open the CSV and read it
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Tells the code the csv file has a header
    csv_header = next(csvreader)
    #Add 1 to our month count for every row
    for rows in csvreader:
        month_count += 1     
    #Appends the profit/loss values our list
        profit_loss.append(rows[1])
    #Also appends the month to the new list
        month.append(rows[0])
    #Find the total amount of profit and losses
    for delta in profit_loss:
        total_profit_loss += int(delta)

    #last value of the list    
        last = len(profit_loss)-1
        #Calculations
        #Delta last month value & first month value divided by the changes
        average_change = (int(profit_loss[last]) - int(profit_loss[0]))/(month_count-1)

        #Append Delta values
        #Appends the first value
        delta_value.append(profit_loss[0])
        #Appends the following delta values
        for i in range(len(profit_loss)-1):
            delta_value.append(int(profit_loss[i+1]) - int(profit_loss[i]))

        #Locate the greatest incease/decrease
        for i in range(len(profit_loss)):
            num = delta_value[i]
            if int(num) > greatest_profit:
                greatest_profit = int(num)
                profit = i
            elif int(num) < least_profit:
                least_profit = int(num)
                loss = i
            else:
                continue

#Output, Financial Analysis
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {month_count}")   
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {month[profit]} (${greatest_profit})")
print(f"Greatest Decrease in Profits:  {month[loss]} (${least_profit})")


#Creates a .txt file
PyBank_analysis = os.path.join("analysis", "PyBank_analysis.txt")

with open (PyBank_analysis , "w") as text:
    text.write("Financial Analysis\n")
    text.write("-------------------------\n")
    text.write(f"Total Months: {month_count}\n")
    text.write(f"Total: ${total_profit_loss}\n")
    text.write(f"Average Change: ${average_change:.2f}\n")
    text.write(f"Greatest Increase in Profits: {month[profit]} (${greatest_profit})\n")
    text.write(f"Greatest Decrease in Profits:  {month[loss]} (${least_profit})\n")
    text.close()
