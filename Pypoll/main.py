import os
import csv

#trying to read in the file
csvPath = os.path.normpath(os.path.join("election_data.csv"))
numOfVotes = 0
#making a dictionary for counting votes.
candidateNumOfVotes = {}
#notes, .pop() can remove items, 
#       .update(key = value) can add things, or change things

#parsing the data
with open(csvPath, newline='') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')

    for vote in csvReader:
        #add candidates into the list if new, 
        # otherwise add one to their total votes.
        numOfVotes += 1
        if vote[2] in candidateNumOfVotes:
            #adding one if voted for
            candidateNumOfVotes[vote[2]] +=1
            #candidateNumOfVotes.update(vote[2] += 1)
        else:
            #adding a new key to 
            candidateNumOfVotes[vote[2]] = 1
            #candidateNumOfVotes.update(vote[2] = 1)

#removing candidate entry
candidateNumOfVotes.pop("Candidate")
numOfVotes -= 1

#Finding winner
checker = 0
tempNameStr = ""
for name in candidateNumOfVotes.keys():
    if candidateNumOfVotes[name] > checker:
        checker = candidateNumOfVotes[name]
        tempNameStr = name

#Time to print, add file stuff once learnt
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(numOfVotes))
print("-------------------------")
#from https://thispointer.com/python-how-to-add-append-key-value-pairs-in-dictionary-using-dict-update/
for(key, value) in candidateNumOfVotes.items():
    print(key + ": " + str(round(100*value/numOfVotes,4)) + "% (" + str(value) + ")")

print("-------------------------")
print("Winner: " + tempNameStr)
print("-------------------------")