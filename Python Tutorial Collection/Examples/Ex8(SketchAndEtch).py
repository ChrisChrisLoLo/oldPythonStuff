#NOTE: GETCH DOES NOT WORK WITH THE PYCHARM IDE
#OPEN IN RAW INTERPRETER
import turtle
import msvcrt
running= True
legnth = 10
width = 2
color = "black"
print("Sketch and Etch v.1.0")
print("Press 'h' for help")
while running:
    command = msvcrt.getch()
#controls
    if command == b"w":
        turtle.forward(legnth)
    elif command == b"s":
        turtle.backward(legnth)
    elif command == b"a":
        turtle.left(30)
    elif command == b"d":
        turtle.right(30)
    elif command == b"c":
        turtle.clear()
#pen modifiers
    elif command == b"r" and legnth < 60:
        legnth += 10
        print ("Legnth={0:.0f}".format(legnth/10))
    elif command == b"f" and legnth > 10:
        legnth -= 10
        print ("Legnth={0:.0f}".format(legnth/10))
    elif command == b"t" and width <= 10:
        width += 2
        turtle.width(width)
        print ("Width={0:.0f}".format(width/2))
    elif command == b"g" and width >= 1:
        width -= 2
        turtle.width(width)
        print ("Width={0:.0f}".format(width/2))
    elif command == b"v":
        color = input("What color would you like?\n")
        turtle.color(color)
#misc.
    elif command == b"h":
        print("Press 'w' to go forwards")
        print("Press 's' to go backwards")
        print("Press 'a' to turn left")
        print("Press 'd' to turn right")
        print("Press 'r' to make the pen go farther")
        print("Press 'f' to make the pen go shorter")
        print("Press 'c' to clear the board")
        print("Type 'v' to change the color")
        print("Type 'p' to exit ")
    elif command == b"p":
        running = False
    else:
        print("invalid")

print("Done")