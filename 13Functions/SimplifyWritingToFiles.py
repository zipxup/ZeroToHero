def WriteToFiles(text, fileName):
    file = open(fileName, "w")
    file.write(text + "\n")
    file.close()
    print("written succesfully")
    return

WriteToFiles("hello world", "demo.txt")