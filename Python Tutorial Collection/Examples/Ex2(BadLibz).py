print ("BadLibz - Ver.1.0\n")
name = " "

name = input("Welcome to BadLibz 1.0, a beginner level code project.\nWhat is your name?\n")
name = name.capitalize()

print ("Hello, " + name + ". It's nice to meet you.")
print ("This version of BadLibz is a story about pirates")

pet = input("What kind of pet do you have/ pet do you want?\n")
pet = pet.lower()

petName = input("Alright, what's it's name?\n")
petName = petName.capitalize()

badPeeps = input("Excellent.\nSay, what kind of people bug you?\n")
badPeeps = badPeeps.capitalize()

badTraits = input("What adjective would you say best describes them?\n")
badTraits = badTraits.capitalize()
island = input("Those certainly do sound like annoying people.\nWhat's the name of the island you would like to visit one day?\n")
island = island.capitalize()

print("Alright, how's this for a story?\n")
print("Once upon a time, there was a pirate called " + name + ", who sailed the seven seas alongside " + petName + ", " + name + "'s " + pet+ ".")
print("The two have sailed to " + island + " and back, encountering savage apes and ape-ish savages.")
print("One day, "+ name + " and " + petName + " decided to pay a visit to the Island of the " + badTraits + " " + badPeeps+ ".")
print("They packed their ships up and began to head out to the island.")
print("However, much to their surprise, when their ship floated near to the island, they began to be bombarded by cannon balls")
badTraits = badTraits.lower()
print("As it turned out, the " + badPeeps + " were as violent as they were " + badTraits+ ".")
print("The ship then drowned and everybody died.")
print("R.I.P.")
badTraits = badTraits.capitalize()
print("\nThis concludes the story of the Island of the " + badTraits + " " + badPeeps +".")
print("Thanks for reading!")
#This is the Mad Libz part of the code. 'badTraits' is lowered and then captitalized again for proper capitalization.