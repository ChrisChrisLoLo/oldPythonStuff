#Can be made into .csv file
fileName = "FoodRating.txt"
APPEND = "a"
running = True
print("Food Rate v.1.5")

foodTypeList = []
foodRatingList = []

file=open(fileName,mode= APPEND)
while running:
    foodType =input("Please enter a food/drink or press done to stop\n").capitalize()
    if foodType == "Stop":
        print("Here is the current list you have:")
        for steps in range(len(foodTypeList)):
            print (foodTypeList[steps] + "," + foodRatingList[steps] + "/10")
        yesNo = input("Is this good?(y/n)\n").lower()
        if yesNo =="y":
            for steps in range(len(foodTypeList)):
                file.write(foodTypeList[steps] + "," + foodRatingList[steps]+"\n")
                running = False
        elif yesNo == "n":
            del foodTypeList[:]
            del foodRatingList[:]
        else:
            print("invalid")
    else:
        foodRating = input("On a scale of 1-10, how would you rate that food/drink?\n")
        foodTypeList.append(foodType)
        foodRatingList.append(foodRating)
file.close()
print("Writing to file was successful")