salary = " "
bonus = " "
salary = input("please enter your salary: ")
bonus = input("please enter your bonus: ")

#float(value) converts value string to float number
#int(value) converts value string to int number
paycheckAmount = float(salary) + float(bonus)
print(paycheckAmount)
print("%.2f" % paycheckAmount)