import csv

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = None
profit_loss_changes = []
greatest_increase = {"date": "", "amount": float("-inf")}
greatest_decrease = {"date": "", "amount": float("inf")}

# Read data from CSV file
with open('Resources/budget_data.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    
    # Loop through each row in the CSV file
    for row in csv_reader:
        # Increment total months
        total_months += 1
        
        # Sum up the net total profit/loss
        net_total += int(row['Profit/Losses'])
        
        # Calculate profit/loss changes
        if previous_profit_loss is not None:
            change = int(row['Profit/Losses']) - previous_profit_loss
            profit_loss_changes.append(change)
            
            # Check for greatest increase and decrease
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = row['Date']
                greatest_increase["amount"] = change
            
            if change < greatest_decrease["amount"]:
                greatest_decrease["date"] = row['Date']
                greatest_decrease["amount"] = change
        
        # Update previous profit/loss for next iteration
        previous_profit_loss = int(row['Profit/Losses'])

# Calculate average change
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Output results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")
