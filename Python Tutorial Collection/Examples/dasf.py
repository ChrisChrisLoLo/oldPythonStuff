import csv
with open("pokemon_types.txt","r") as zoosFile:
    zoosData = csv.reader(zoosFile, delimiter = ",")
    for line in zoosData:
        if line[1] == "12":
            line[1] = "grass"
        print(",".join(line))
