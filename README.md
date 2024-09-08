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
        Also, the final script should not only print the analysis to the terminal and export a text file with the results.
        
        Open and read the Election_data csv file. It should contain three columns 
        
        The script reads the csv and there is an error check if file does not exist the code will stop and exit.
        Next it counts the total number of votes overall.
        Then it counts the votes each candidate receives.
        Then the average number of votes and percentage of total votes per candidate will be calculated
        Once each candidate’s number of votes and percentage of total votes is calculated the winner will be decided based on the greatest number of votes one candidate receives.
        Out put will be displayed on the terminal and saved in the Election_Results in Analysis folder. 
