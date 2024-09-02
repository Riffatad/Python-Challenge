import os
import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
    
  
    sum = 0 
    count = 0 
    prow=0
    ave=0
    highest = 0
    lowest = 0
    Diff=0
    highest_date = ""  
    lowest_date = ""
    
    for row in csv_reader:

        
        if count != 0 :

            Diff = int(row[1])-prow
            ave = ave + Diff

            if Diff > highest: 
                highest = Diff
                highest_date = row[0]
            if Diff < lowest:
                lowest = Diff
                lowest_date = row[0]  

        sum = sum + int(row[1])
        count = count + 1
        prow= int (row[1])

        

    print(f"Total Months :{count}")
    print(f"Total Profit / Loss :{sum}")
    print(f"Average Difference= : {(ave/(count-1)):.2f}")
    print(f"Highest Difference is {highest} for month {highest_date}")
    print(f"Highest Difference is {lowest} for month {lowest_date}")
    

    
