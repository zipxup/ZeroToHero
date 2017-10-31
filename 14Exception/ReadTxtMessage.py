import csv

# this is the main function
# calls other functions from here
def main():
    print("please enter the text message: \n")
    textMessage = input(">").upper()

    textWords = textMessage.split()
    
    translationFileName = "GuestList.csv"

    hasFile = checkFile(translationFileName)

    if hasFile:
        dictionary = storeTranslation(translationFileName)
        finalTranslation = translateWords(textWords, dictionary)
        print(">" + finalTranslation)
    else:
         print("cannot translate message, file containing translations cannot be located")


#this is the function to check whether file exists or not.
#if file exists, return True, otherwise, return False
def checkFile(fileName):
    hasfileFlag = False
    try:
        myFile = open(fileName, mode =  "r")
        myFile.close()
        hasfileFlag = True
    except:
        print("Sorry, something went wrong")
        hasfileFlag = False
    finally:
        return hasfileFlag

#this is the function to store information from file into dictionary
def storeTranslation(fileName):
    dict = {}
    #if there is something wrong, this sentence will always close file
    with open(fileName, mode = "r") as myCSVFile:
        AllRowsList = csv.reader(myCSVFile, delimiter = ",")
        for currentRow in AllRowsList:
            lengthOfRow = len(currentRow)
            translation = ""
            for step in range(1, lengthOfRow):
                translation += currentRow[step] + " "
            currentRow[0] = currentRow[0].upper()
            dict[currentRow[0]] = translation
    return dict

#this is the function to translate text message from abbreviation to full text
def translateWords(textWords, dict):
    finalTranslation = ""
    for word in textWords:
        if word in dict.keys():
            finalTranslation += dict[word] + " "
    if finalTranslation == "":
        finalTranslation = "Sorry, no match result"
    return finalTranslation

# call to run whole program
main()



