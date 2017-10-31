country = input("What country are you from? ").upper()
orderTotal = input("Please enter your order total: ")
orderTotal = float(orderTotal)
province = " "
tax = 0.0
totalPayment = 0.0
GST = 0.05
HST = 0.13
PST = 0.06
if country == "CANADA":
    province = input("Which province are your from: ").upper()
    if province == "ALBERTA":
        tax = orderTotal * GST / 100
        print("You got charged with 0.05% General sales Tax. ")
    elif province == "ONTARIO" or province == "NEW BRUNSWICK" or \
        province == "NOVA SCOTIA":
            tax = orderTotal * HST / 100
            print("You got charged with 0.13% Harmonized sales Tax. ")
    else:
        tax = orderTotal * (PST + GST) / 100
        print("You got charged with 0.06% provincial sales Tax and 0.05% General sales Tax. ")
    totalPayment = orderTotal + tax;
else:
    tax = 0
    totalPayment = orderTotal + tax
    print("you don't need to pay tax")
print("Your total payment is $%.2f" %totalPayment)