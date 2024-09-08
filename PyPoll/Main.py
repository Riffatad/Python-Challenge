import os
import csv

# Define file paths
budget_csv = os.path.join("Resources", "election_data.csv")  # Path to the input CSV file
output_txt = os.path.join("Analysis", "Election_Results.txt")  # Path to the output text file

# Check if the input file exists
if not os.path.isfile(budget_csv):
    print(f"Error: The file {budget_csv} does not exist.")
    exit()  # Exit the script if the file does not exist

# Initialize variables
vote_count = 0  # Total number of votes
candidates = {}  # Dictionary to store candidate names and their vote counts

# Open and read the CSV file
with open(budget_csv, mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)  # Create a CSV reader object
    
    # Read and skip the header row
    next(csv_reader)
    
    # Process each row in the CSV file
    for row in csv_reader:
        if len(row) >= 3:  # Ensure the row has at least 3 columns
            vote_count += 1  # Increment total vote count
            candidate_name = row[2]  # Get the candidate's name from the third column
            
            # Update the candidate's vote count
            candidates[candidate_name] = candidates.get(candidate_name, 0) + 1

# Create the output for the results
# prints at terminal
print("Election Results")
print("-----------------------------")
print(f"Total Votes: {vote_count}") # Total number of votes
print("-----------------------------")

# writes out the result in txt file
output_content = (
    "Election Results\n"
    "-----------------------------\n"
    f"Total Votes: {vote_count}\n" # Total number of votes
    "-----------------------------\n"
)

# Initialize variables to track the winner
winner = ""
winning_votes = 0

# Add each candidate's total votes and percentage to the output
for candidate, votes in candidates.items():
    percentage = (votes / vote_count) * 100  # Calculate the percentage of total votes
    print(f"{candidate}: {percentage:.2f}% ({votes})") #prints at terminal
    output_content += f"{candidate}: {percentage:.2f}% ({votes})\n"  # outputs to txt file

    
    # Determine if the current candidate has more votes than the previous winner
    if votes > winning_votes:
        winning_votes = votes  # Update the highest vote count
        winner = candidate  # Set the new winner

# prints at terminal 
print("-----------------------------")
print(f"Winner: {winner}") # Display the winner
print("-----------------------------")

# Add the winner's information to the txt file

output_content += (
    "-----------------------------\n"
    f"Winner: {winner}\n"  # Display the winner
    "-----------------------------\n"
)

# Write the output to the text file
with open(output_txt, 'w') as output_file:
    output_file.write(output_content)  # Save the results to the file


# Notify user that results have been written
print(f"Results also have been written to {output_txt}")
