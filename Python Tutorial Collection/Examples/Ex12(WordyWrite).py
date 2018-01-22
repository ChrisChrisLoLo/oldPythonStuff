def writeToFile(fileName,text):
    with open(fileName+".txt","w") as openFile:
        openFile.write(text)
        print("(Writing to file successful)")
    return

writeToFile("applesauce","tastes good.")

inputName = input("What is the name of the file you want to write?\n")
text = input("What do you want to type in this file?\n")

writeToFile(inputName,text)