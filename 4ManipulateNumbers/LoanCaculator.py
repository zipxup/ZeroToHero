#This program is used for calculating monthly payment.
#The formula is M = L[i(1 + i)n] / [(1 + i)n-1]
# M = monthly payment
# L = loan amount
# i = interest rate(for an interest rate of 5%, i = 0.05)
# n = number of years


loanCost = input("please input the cost of the loan: ")
interestRate = input("please input the interest rate: ")
numberOfYears = input("please input the number of years: ")

loanCost = float(loanCost)
interestRate = float(interestRate)
numberOfPayments = float(numberOfYears) * 12

monthlyPayment = loanCost * (interestRate * (1 + interestRate) * numberOfPayments)\
    /((1 + interestRate) * numberOfPayments - 1)
print("Your monthly payment will be $%.3f" % monthlyPayment)