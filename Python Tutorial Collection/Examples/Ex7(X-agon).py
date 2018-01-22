import turtle
print("X-Agon Shape Maker v.1.0")
sideNum = int(input("How many sides would you like on your shape?\n"))
sideLength = int(input("How many pixels would you like each side to be?\n"))
sideColor = input("What color would you like the sides to be?\n")
inception = input("Would you like to have shape-ception?(y/n)\n").lower()

for step in range(sideNum):
    turtle.color(sideColor)
    turtle.right(360/sideNum)
    turtle.forward(sideLength)
    if inception == "y":
        for step in range (sideNum):
            turtle.color(sideColor)
            turtle.right(360/sideNum)
            turtle.forward(sideLength/2)
turtle.exitonclick()