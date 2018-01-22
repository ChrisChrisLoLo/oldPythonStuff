shipCost = False
print("Rip&Ship v.1.0")

print("\nThanks for shopping at the Royal Nigerian Market!")
purchaseAmount= float(input("How much is your purchase?\n"))

if purchaseAmount < 50:
    shipCost = True

if shipCost:
    totalAmount= purchaseAmount + 10
    print("Yeaaah, about that. Because you have spent so little you have displeased our prince.")
    print("A shipping cost of $10 will be added, making your total ${0:.2f}".format(totalAmount))
else:
    print("Thank you for your generous purchase!")
    print("Your total will be ${0:.2f}".format(purchaseAmount))

print("Have a good day you cheeky skrublord. :)")