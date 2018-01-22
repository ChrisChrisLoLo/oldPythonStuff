import csv
import sys
print("Open File Style v.1.0")

def default(userInput):
    try:
        with open(userInput+".txt","r") as openFile:
            words = openFile.read()
            print(words)
        run = "no"
        return run
    except:
        print("File not found!")
        return
running = True
while running:
    userInput = input("What file would you like to open?(.txt files only!)\n")
    run = default(userInput)
    if run == "no":
        break
