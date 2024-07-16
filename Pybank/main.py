import os
import csv

# creats the path for the CSV file
csvpath = os.path.join('Desktop', 'Starter_Code', 'Pybank', 'Resources', 'budget_data.csv')

# create variables to store data
months = []  # store all months
profit_loss_changes = []  # List to store monthly changes in profit/loss
net_profit_loss = 0  #  keep track of the net total profit/loss
previous_month_profit_loss = None  # profit/loss of the previous month

# Open and read the CSV file
with open(csvpath, newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    
    for row in csv_reader:
        # Adding the month to the months list
        months.append(row['Date'])
        
        current_month_profit_loss = int(row['Profit/Losses'])
        
        net_profit_loss += current_month_profit_loss

        # help determine the change in profit/loss from the previous month 
        if previous_month_profit_loss is not None:
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss
            profit_loss_changes.append(profit_loss_change)

        # Update the previous month's profit/loss to the current month's value
        previous_month_profit_loss = current_month_profit_loss

# figures the total number of months
count_months = len(months)

# Calculate the average change in profit/loss
average_profit_loss = round(sum(profit_loss_changes) / len(profit_loss_changes), 2) if profit_loss_changes else 0

greatest_increase = max(profit_loss_changes) if profit_loss_changes else 0
greatest_decrease = min(profit_loss_changes) if profit_loss_changes else 0

# figure out the greatest increase and decrease in profit/loss in months
greatest_increase_month = months[profit_loss_changes.index(greatest_increase) + 1] if profit_loss_changes else "N/A"
greatest_decrease_month = months[profit_loss_changes.index(greatest_decrease) + 1] if profit_loss_changes else "N/A"

# Create a summary of the financial analysis
financial_analysis_summary = (
    f"Total: ${net_profit_loss}\n"
    f"Average Change: ${average_profit_loss}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
)

# header for the financial analysis
financial_analysis = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {count_months}\n"
)

# Print the financial analysis results in gitbash
print(financial_analysis, end="")
print(financial_analysis_summary)

# Write the financial analysis results to a text file
output_file = 'financial_analysis.txt'
with open(output_file, 'w') as datafile:
    datafile.write(financial_analysis)
    datafile.write(financial_analysis_summary)

print(f"\nResults have been written to {output_file}")
