import csv

READ = "r"
READWRITE = "r+"

fileName = "GuestList.csv"
myFile = open(fileName, mode = READ)

#read whole files
#fileContent = myFile.read()
#read line by line
#fileContent = myFile.readline()
#print(fileContent)

#program will always open a file, and close it when it is finished
with open(fileName, mode = READ) as myCSVFile:
    AllRowsList = csv.reader(myCSVFile, delimiter = ",")
    for currentRow in AllRowsList:
        #no square bracelet
        #SeparatorToDisplay.join()
        print(",".join(currentRow))
        #print(currentRow)
        #for currentWord in currentRow:
        #    print(currentWord)
