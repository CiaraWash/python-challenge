# Step 1a: Print these headers
print("Financial Analysis")
print("----------------------------")
# Step 1b: Import the csv file and prep it to be read
# Import the csv library
import csv 

# This code displays the file path of the csv file
with open ("PyBank/Resources/budget_data.csv", newline = '') as csvfile:

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

# This is how you read the header in the csv files... not all CSVs have headers
    # csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

# This is how you reader each row in the csv file (will not use because there is a lot of data)
    # for row in csvreader:
        # print(row)

# Step 2: Find the total number of months included in the dataset
    next(csvreader)
    data = list (csvreader)
    row_count = len(data)

print(f"Total Months: {row_count}")

# Step 3: Find the net total amount of "Profit/Losses" over the entire period
# create a loop to add up the total number of 
totalPL = 0
for PL in range(0, row_count):
    totalPL = totalPL + int(data[PL][1])

print(f"Total: ${totalPL}")

# Step 4: Find The changes in "Profit/Losses" over the entire period, and then the average of those changes
# Essentially, we just need to find the average
number1 = 0
number2 = int(data[0][1])
difference = 0
differencelist = list()
for aPL in range(1, row_count):
    number1 = int(data [aPL][1])
    difference = number1 - number2
    differencelist.append(difference)
    number2 = int(data[aPL][1])
averagePL = round(sum(differencelist)/len(differencelist),2)

print(f"Average Change: ${averagePL}")

# Step 5: Find the greatest increase in profits (date and amount) over the entire period
maxamount = max(differencelist)
maxmonth = differencelist.index(maxamount)+1

print(f"Greatest Increase in Profits: {data[maxmonth][0]} (${maxamount})")

#Step 6: Find the greatest decrease in profits (date and amount) over the entire period
minamount = min(differencelist)
minmonth = differencelist.index(minamount)+1

print(f"Greatest Decrease in Profits: {data[minmonth][0]} (${minamount})")

# Step 7: Now print the PyBank Results into text
print("Financial Analysis", file=open("PyBank.txt", "a"))
print("----------------------------", file=open("PyBank.txt", "a"))
print(f"Total Months: {row_count}", file=open("PyBank.txt", "a"))
print(f"Total: ${totalPL:,}", file=open("PyBank.txt", "a"))
print(f"Average Change: ${averagePL:,}", file=open("PyBank.txt", "a"))
print(f"Greatest Increase in Profits: {data[maxmonth][0]} (${maxamount:,})", file=open("PyBank.txt", "a"))
print(f"Greatest Decrease in Profits: {data[minmonth][0]} (${minamount:,})", file=open("PyBank.txt", "a"))