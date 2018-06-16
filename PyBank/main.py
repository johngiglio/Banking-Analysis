# import packages
import csv
file = "budget_data.csv"


# create lists to store date and revenue
date = []
revenue = []

#read data
with open(file,encoding="utf8") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")

# iterate through csvreader and append to date and revenue lists
    header = next(csvreader) #skip headers
    for row in csvreader:
        date.append(row[0])
        revenue.append(row[1])
    # date.pop(0)
    # revenue.pop(0)
    # length of date list to get total number of months
    nummonths = len(date)


    # sum revenue
    revsum = int()
    # iterate to turn revenue into integer and add to sum
    for i in range(0,len(revenue)):
        revenue[i] = int(revenue[i])
        revsum += revenue[i]
    
    
    # average change in "Profit/Losses" between months over the entire period
    # create new integer to store total monthly changes,  divide by nummonths - 1
    # create new list to store monthly changes

    totalchange = int()
    monthchange = []
    for i in range(len(revenue)-1):
        totalchange += (revenue[i+1] - revenue[i])
        monthchange.append((revenue[i+1] - revenue[i]))

    avgchange = totalchange / (nummonths - 1)

# 'print total months
# 'print net profit/loss over entire period
# 'print average change in profit/loss between months
# 'print greatest increase in profits
# 'print greatest decrease in losses

    print("  Financial Analysis\n---------------------------- ")
    print("Total Months: " + str(nummonths) )
    print("Total: $" + str(totalchange))
    print ("Average  Change: $" + str(avgchange))
    print("Greatest Increase in Profits: " + date[monthchange.index(max(monthchange))] + " "+ str(max(monthchange)))
    print("Greatest Decrease in Profits: " + date[monthchange.index(min(monthchange))] + " " + str(min(monthchange)))




# write to csv
output_file = "PyBank_solved.csv"

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row

    writer.writerow(["  Financial Analysis"])
    writer.writerow(["---------------------------- "])
    writer.writerow(["Total Months: ",str(nummonths)])
    writer.writerow(["Total:",  " $"+str(totalchange)])
    writer.writerow(["Average  Change: $",str(avgchange)])
    writer.writerow(["Greatest Increase in Profits: ",date[monthchange.index(max(monthchange))],str(max(monthchange))])
    writer.writerow(["Greatest Decrease in Profits: ",date[monthchange.index(min(monthchange))],str(min(monthchange))])