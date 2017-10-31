# myFile = open(fileName, accessMode)
# accessMode
#r -- read the file
#w -- write to the file
#a -- append to the existing file content
#b -- open a binary file

fileName = "demo.txt"
WRITE = "w"
APPEND = "a"
READ = "r"
READWRITE = "w+"

data = input("please enter file info:\n")
file = open(fileName, mode = WRITE)
file.write(data)
file.close()

#myFile = open(fileName, mode = READWRITE)
#myFile.write("Susan,29 \n")
#myFile.write("Christopher,31\n")
#myFile.close()

print("File written succesfully")