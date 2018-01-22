import csv
running = True
print("FoodReader v.1.0")
while running:
    with open("FoodRating.txt","r") as foodData:
        foodList = csv.reader(foodData)
        quality = input("Do you want a list of bad, alright, or great foods/drinks?\n").lower()
        for lines in foodList:
            if quality == "bad" and int(lines[1]) <= 5:
                print(lines[0])
            if quality == "alright" and int(lines[1]) < 8 and int(lines[1]) >6:
                print(lines[0])
            if quality == "great" and  int(lines[1]) >= 8:
                print(lines[0])
    carryon = input("Would you like to run the search again?(y/n)\n").lower()
    if carryon == "n":
        break
print("Finished")
