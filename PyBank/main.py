# Data importing with os
import os
import csv

# Define file paths
budget_csv = os.path.join("Resources", "budget_data.csv")
output_txt = os.path.join("Analysis", "financial_analysis.txt")

# Check if the file exists
if not os.path.isfile(budget_csv):
    print(f"Error: The file {budget_csv} does not exist.")
    exit(1)

# Open the CSV file
with open(budget_csv, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # Read and skip the header row
    csv_header = next(csv_reader, None)
    
    # Ensure there is at least one data row
    first_row = next(csv_reader, None)
    if first_row is None:
        print("Error: The file does not contain data rows.")
        exit(1)

    # Initialize variables
    sum = 0               # Total sum of the values
    count = 0             # Count of the number of months
    average = 0           # Total change in values for average calculation
    
    highest = float('-inf')  # Highest change value
    lowest = float('inf')    # Lowest change value

    highest_date = ""     # Date of the highest change
    lowest_date = ""      # Date of the lowest change
    
    # Process the first row
    previous_row = int(first_row[1])  # Initialize the previous_row value
    sum += previous_row               # Add the first value to the total sum
    count += 1                        # Increment the count of months

    # Iterate through the remaining rows
    for row in csv_reader:
        current_value = int(row[1])    # Convert the current value to an integer
        
        # Calculate the difference between the current and previous values
        difference = current_value - previous_row
        average += difference

        # Update the highest and lowest changes
        if difference > highest:
            highest = difference
            highest_date = row[0]


        if difference < lowest:
            lowest = difference
            lowest_date = row[0]


        # Update the total sum and previous_row for the next iteration
        sum += current_value
        count += 1
        previous_row = current_value

    # Calculate the average change, handle case with less than 2 months
    average_change = average / (count - 1) if count > 1 else 0


    # Prepare the output content
    print("Financial Analysis\n")
    print("--------------------------\n")
    print(f"Total Months: {count}\n")
    print(f"Total: ${sum}\n")
    print(f"Average Change: ${average_change:.2f}\n")
    print(f"Greatest Increase in Profits: {highest_date} (${highest})\n")
    print(f"Greatest Decrease in Profits: {lowest_date} (${lowest})\n")

    output_content = (
        "Financial Analysis\n"
        "--------------------------\n"
        f"Total Months: {count}\n"
        f"Total: ${sum}\n"
        f"Average Change: ${average_change:.2f}\n"
        f"Greatest Increase in Profits: {highest_date} (${highest})\n"
        f"Greatest Decrease in Profits: {lowest_date} (${lowest})\n"
        
    )

    # Write the output content to the file
    with open(output_txt, 'w') as output_file:
        output_file.write(output_content)

# Inform the user that the results have been written
print(f"Results have been written to {output_txt}")
