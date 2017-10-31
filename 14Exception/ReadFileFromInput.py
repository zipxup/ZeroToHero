fileName = input("please enter a file name: ")

try:
    myFile = open(fileName, mode = "r")
    myFile.close()
except FileNotFoundError:
    print("Sorry, there is no " + fileName)
except:
    print("Something went wrong")


