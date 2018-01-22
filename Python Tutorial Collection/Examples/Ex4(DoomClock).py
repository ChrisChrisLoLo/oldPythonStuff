import datetime
presentDate = datetime.date.today()

print("DoomClock v.1.0")
print('"The End Is Nigh"\n')

userInput= input("When is your project due?(dd/mm/yyyy)\n")
endDate= datetime.datetime.strptime(userInput,"%d/%m/%Y").date()

dateLeft = endDate - presentDate
dateLeft = float(dateLeft.days)

#The process below is breaking up the time left into days and weeks.
# This is done by finding the remainder of the days left by dividing our total time by 7
# and then perfectly dividing the remaining quotient by 7
daysLeft = dateLeft%7
weeksLeft = (dateLeft-daysLeft)/7

print("You have {0:.0f} week(s)".format(weeksLeft)+ " and {0:.0f} day(s) left.".format(daysLeft))
print("Better get on it!")