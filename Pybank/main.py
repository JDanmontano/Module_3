import os
import csv

csvpath = os.path.join('Desktop', 'Starter_Code', 'Pybank', 'Resources', 'budget_data.csv')

months = []
profit_loss_changes = []
net_profit_loss = 0
previous_month_profit_loss = None

with open(csvpath, newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        months.append(row['Date'])
        current_month_profit_loss = int(row['Profit/Losses'])
        net_profit_loss += current_month_profit_loss

        if previous_month_profit_loss is not None:
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss
            profit_loss_changes.append(profit_loss_change)

        previous_month_profit_loss = current_month_profit_loss

count_months = len(months)
average_profit_loss = round(sum(profit_loss_changes) / len(profit_loss_changes), 2) if profit_loss_changes else 0
greatest_increase = max(profit_loss_changes) if profit_loss_changes else 0
greatest_decrease = min(profit_loss_changes) if profit_loss_changes else 0
greatest_increase_month = months[profit_loss_changes.index(greatest_increase) + 1] if profit_loss_changes else "N/A"
greatest_decrease_month = months[profit_loss_changes.index(greatest_decrease) + 1] if profit_loss_changes else "N/A"

financial_analysis_summary = (
    f"Total: ${net_profit_loss}\n"
    f"Average Change: ${average_profit_loss}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
)

financial_analysis = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {count_months}\n"
)
print(financial_analysis, end="")
print(financial_analysis_summary)

output_file = 'financial_analysis.txt'
with open(output_file, 'w') as datafile:
    datafile.write(financial_analysis)
    datafile.write(financial_analysis_summary)

print(f"\nResults have been written to {output_file}")
