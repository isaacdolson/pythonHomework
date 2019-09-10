import os
import csv

#read in the file
csvPath = os.path.normpath(os.path.join("budget_data.csv"))

monthsOfData = 0
netProfit = 0
increaseMonth = ""
increaseValue = 0
decreaseMonth = ""
decreaseValue = 0
changes = 0
lastMonth = 0

with open(csvPath, newline='') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    #hopefully skipping the header.
    next(csvReader)
    changes = csvReader[1]
    for row in csvReader:
        monthsOfData +=1
        netProfit += int(row[1])
        #seems like there should be a better way to do this,
        #like take the first month minus the last
        #changes += (lastMonth - int(row[1]))
        if (int(row[1]) > increaseValue):
            increaseValue = int(row[1])
            increaseMonth = row[0]
        if (int(row[1]) < decreaseValue):
            decreaseValue = int(row[1])
            decreaseMonth = row[0]

#also still need print to file stuff.
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {monthsOfData}")
print(f"Total: ${netProfit}")
#average change omited, for cleaverness
print(f"Greatest Increase in Profits: {increaseMonth} ({increaseValue})")
print(f"Greatest Decrease in Profits: {decreaseMonth} ({decreaseValue})")