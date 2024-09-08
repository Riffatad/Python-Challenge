# Python-Challenge
# PYBANK
        
# The Challenge is to create a Python Script to analyze a company's financial records. The data set is in a csv file, and it has two columns. Column 1 "Date" and Column 2 "Profit/Loss"

The Script will calculate each of the following values through Python Script.
* The total number of months included in the dataset

* The net total amount of "Profit/Losses" over the entire period

* The changes in "Profit/Losses" over the entire period, and then the average of those changes

* The greatest increase in profits (date and amount) over the entire period

* The greatest decrease in profits (date and amount) over the entire period

The result should match the following:

Example Output should be like this:
Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)

The result should be displayed at the terminal and output in the text file.

Opens the CSV file and reads it using a CSV reader
Skips the header row and processes each subsequent row.
Initializes variables:
(sum, count, average change, highest and lowest change).        

# Calculate the following:
•	Total sum of profit/loss values.
•	Count of the number of months.
•	Average change in profit/loss values.
•	Greatest increase and decrease in profits, along with the corresponding dates.
     The results will not only output on the terminal but will also save into the Financial_analysis.txt this file is saved in Analysis folder.
# Error checks
If the header row does not have data after header row it prompts error message and will exit.
 Also, error check is on the csv file existence if the file is not it will be prompt an error message.
        

          
          
# PYPOLL
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
