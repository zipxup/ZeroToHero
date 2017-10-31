def main():
    names = getNames()
    printNames(names)
    return

def getNames():
    names = ['Christopher', 'Susan', 'Danny']
    newName = input('Enter last guest: ').capitalize()
    names.append(newName)
    return names

def printNames(names):
    for name in names:
        print(name)
    return

#printMessage
main()

