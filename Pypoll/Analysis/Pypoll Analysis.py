

import os 
import csv 

print("Election Results")

print("-------------------------------------")
#
#candidate = "Charles Casper Stolkholm"

#ballots = candidates

election_csv = os.path.join ("Pypoll", "Resources", "election_data.csv")

with open (election_csv, newline= '') as csvfile:
    csv_reader= csv.reader(csvfile, delimiter= ",")
    next(csv_reader)

    data = list(csv_reader)
    row_count = len(data)

    print("Total Votes: " + str(row_count))

    print("-------------------------------------")


    
   
        

    
    


    