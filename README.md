# Python-Challenge
Python-Challenge (PY POLL)
Instructions
The task of this challenge is to integrate a faster and accurte vote count process for a small, rural town.

The Poll data file is called election_data.csv that provides information to analyze and script in Python.

It compromises three columns: "Voter ID", "County", and "Candidate".

The task is to create a Python script that analyzes the votes and calculates each of the following values:

• The total number of votes cast

• A complete list of candidates who received votes

• The percentage of votes each candidate won

• The total number of votes each candidate won

• The winner of the election based on popular vote

The analysis should match the following results:

          Election Results
          -------------------------
          Total Votes: 369711
          -------------------------
          Charles Casper Stockham: 23.049% (85213)
          Diana DeGette: 73.812% (272892)
          Raymon Anthony Doane: 3.139% (11606)
          -------------------------
          Winner: Diana DeGette
          -------------------------
Also the final script should not only print the analysis to the terminal and export a text file with the results.

Define file paths
        # Path to the input CSV file
        # Path to the output text file
Check if the input file exists
        # Exit the script if the file does not exist
Initialize variables
        # Total number of votes
        # Dictionary to store candidate names and their vote counts
Open and read the CSV file
        # Create a CSV reader object
Read and skip the header row
Process each row in the CSV file
        # Ensure the row has at least 3 columns
        # Increment total vote count
        # Get the candidate's name from the third column

# Update the candidate's vote count
Create the output for the results
prints at terminal
Title
Total Vote Result
writes out the result in txt file
Initialize variables to track the winner
Add each candidate's total votes and percentage to the output
Calculate the percentage of total votes
Add candidate's votes
prints at terminal
Output also in txt file
Determine if the current candidate has more votes than the previous winner
# Update the highest vote count
# Set the new winner
prints winner at terminal
Outputs also in txt file
Notify user that results have been written in txt file as well
