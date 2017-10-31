shippingCharge = input("please enter the amount for your total purchase: ")

shippingCharge = float(shippingCharge)

freeShipping = True
if shippingCharge < 50:
    freeShipping = False

if freeShipping:
    print("Congratulation! you've got a free shipping")
else:
    print("there is an extra $10 for shipping")
print("have a nice day")