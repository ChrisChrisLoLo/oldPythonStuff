GST = 0.05
PST = 0.06
HST = 0.13
print("We Hate Canada v.1.0\n")

country = input("What country are you from?\n").lower()

amount = float(input("How much was your online purchase in dollars?\n"))



if country == "canada":
    print ("Whoopsies, looks like your'e going to have to pay a tax.")
    province = input ("What province are you from?\n").lower()
    if province == "alberta":
        print("Looks like you're going to have to pay GST ({0:.2f}%) on top of your purchase.".format(GST))
        total = amount + (amount * GST)
    elif province ==("ontario" or "new brunswick" or "nova scotia"):
        print("Looks like you're going to have to pay a harmonized tax of {0:.2f}% on top of your purchase.".format(HST))
        total = amount + (amount * HST)
    else:
        print("Looks like you're going to have to pay a provincial tax of {0:.2f}% and GST ({1:.2f}%) on top of your purchase.".format(PST,GST))
        total = amount + (amount * PST) + (amount * GST)
    print("Your total now comes to ${0:.2f}.".format(total))
    if total >= 100:
       print("Looks like you're eligible for a free toaster though!")
else:
    print("Alright, you're ready to go!")
print("Have a good day!")