import csv
with open("pokemon.csv","r") as pokemonFile:
    pokemonList = csv.reader(pokemonFile,delimiter = ",")
    for steps in pokemonList:
        print(steps)
    with open ("pokemon_types.csv","r") as pokemonTypesFile:
        pokemonTypesList = csv.reader(pokemonTypesFile,delimiter = ",")

