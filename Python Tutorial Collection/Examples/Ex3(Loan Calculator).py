#declaring variables
monthlyPayment = 0
loanAmount = 0
interestRate = 0
amountOfPayments = 0

print("Shark-B-Gone Ver.1")
print('"Protecting Kneecaps Since \'15!" \n')

#the input below only make the program more personal and does not affect the formula
currencyName = input("What currency are you paying in?\n")
currencyName = currencyName.lower()

loanAmount = input("How much do you owe in " + currencyName +"s? \n")
interestRate = input("What is the interest rate on this loan in percent?\n")
#converting percentage to decimal
interestRate = float(interestRate)/100
amountOfPayments = input("How many monthly payments are you going to make? \n")

#This is the formula for a loan, broken up into two lines. Float to convert string to float
monthlyPayment = float(loanAmount)*(float(interestRate)*(1+float(interestRate))*float(amountOfPayments))\
    /((1+float(interestRate))*float(amountOfPayments)-1)

print("In order to keep the sharks at bay, you're going to have to pay {0:.2f} ".format(monthlyPayment)\
      + currencyName + " a month. \nGood luck paying off that.")