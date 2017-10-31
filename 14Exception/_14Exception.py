import sys

firstNumber = input("enter a number: ")
secondNumber = input("enter a number: ")

firstNumber = float(firstNumber)
secondNumber = float(secondNumber)

try:
    result = firstNumber / secondNumber
    print(result)
except ZeroDivisionError:
    print("The answer is infinity") 
    #sys.exit()   
except:
    error = sys.exc_info()[0]
    print("something went wrong")    
    print(error)
finally:
    print("I wil always run")
print("This message always displays")