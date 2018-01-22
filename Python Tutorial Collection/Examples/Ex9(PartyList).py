running = True
partyList = []
print("Party Maker v.1.0")

print("Who is coming to your party?\n(Type 'done' to finish.)")
while running:
    name = input().capitalize()
    if name == "Done":
        break
    else:
        partyList.append(name)
        print ("Added "+ name +" to the list.")
partyList.sort()
print("These people will be coming to the party:")
for guests in partyList:
    print (guests)