WRITE = "w"
fileName = "GuestList.csv"
myFile = open(fileName, mode = WRITE)

keyword = "finish".lower()

name = input("please enter your guest name: ").lower()
while name != keyword:
    age = input("please enter your guest age: ")
    lineWords = name + "," + age + "\n";
    myFile.write(lineWords)
    name = input("please enter your guest name: ").lower()

myFile.close()
print("File written successfully")