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
    #changes = csvReader[1]
    for row in csvReader:
        #seems like there should be a better way to do this.
        if monthsOfData > 0:
            changes += (lastMonth - int(row[1]))
        lastMonth = int(row[1])
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
print(f"Average Change: ${round(-changes/monthsOfData, 3)}")
#average change omited, for cleaverness
print(f"Greatest Increase in Profits: {increaseMonth} ({increaseValue})")
print(f"Greatest Decrease in Profits: {decreaseMonth} ({decreaseValue})")
#printing to file
bankFile = open("pyBankFile.txt", "w")

bankFile.write("Financial Analysis\n")
bankFile.write("-------------------------\n")
bankFile.write(f"Total Months: {monthsOfData}\n")
bankFile.write(f"Total: ${netProfit}\n")
bankFile.write(f"Average Change: ${round(-changes/monthsOfData, 3)}\n")
bankFile.write(f"Greatest Increase in Profits: {increaseMonth} ({increaseValue})\n")
bankFile.write(f"Greatest Decrease in Profits: {decreaseMonth} ({decreaseValue})")
bankFile.close()
# bankFilePrint = os.path.join("pyBankFile.txt")
# with open(bankFilePrint, mode='w', newline='') as csvTxt:
    
#     csvWriter = csv.writer(csvTxt, delimiter = ' ')

#     csvWriter.writerow(TestString)
#     csvWriter.writerow("-------------------------")
#     csvWriter.writerow(f"Total Months: {monthsOfData}")
#     csvWriter.writerow(f"Total: ${netProfit}")
#     csvWriter.writerow(f"Average Change: ${round(changes/monthsOfData, 3)}")
#     csvWriter.writerow(f"Greatest Increase in Profits: {increaseMonth} ({increaseValue})")
#     csvWriter.writerow(f"Greatest Decrease in Profits: {decreaseMonth} ({decreaseValue})")