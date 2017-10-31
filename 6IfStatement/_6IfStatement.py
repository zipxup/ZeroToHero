#if statements with strings
#answer = input("Would you like express shipping? ")
#answer = answer.lower()
#if answer == "yes":
#    print("there will be an extra $10.")
#if not answer == "no":
#    print("try not statement")
#print("Have a nice day.")

#if statements with numbers
deposit = input("how much do you want to deposit? ")
deposit = float(deposit)

freeToaster = False
if deposit > 100:
    freeToaster = True

if freeToaster:
    print("enjoy your toaster!")
else:
    print("enjoy your mug!")
print("Have a nice day!")