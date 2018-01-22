#Rock,paper,scissors
import random

running = True
cheating = False
rock = "Rock"
paper = "Paper"
scissors = "Scissors"
gun = "Gun"
user_score= 0
comp_score= 0


print("Rock,Scissors,Paper")
start = input("Would you like to play? (Y/N) \n")
start = start.capitalize()
if start == "Y":
    print ("Enter 'Q' to quit")
    while running:

        user_pick = input("\nRock,Scissors,or Paper? \n")

        user_pick = user_pick.capitalize()
        if user_pick == "Q":
            break
        print("You picked " + user_pick + ".")

        comp_pick = random.sample(["Rock","Paper","Scissors"], 1)
        comp_pick = comp_pick[0]
        print("The computer picked " + comp_pick + ".")

        if user_pick == comp_pick:
            print ("Tie game.")

        elif user_pick == paper and comp_pick == rock:
            print ("You Win")
            user_score += 1
        elif user_pick == scissors and comp_pick == rock:
            print ("Computer Wins")
            comp_score += 1
        elif user_pick == scissors and comp_pick == paper:
            print ("You Win")
            user_score += 1
        elif user_pick == rock and comp_pick == paper:
            print ("Computer Wins")
            comp_score += 1
        elif user_pick == rock and comp_pick == scissors:
            print ("You Win")
            user_score += 1
        elif user_pick == paper and comp_pick == scissors:
            print ("Computer Wins")
            comp_score += 1
        elif user_pick == gun:
            print ("You Win,Cheater")
            user_score += 1
            cheating = True
        else:
            print("Error")

        print("\nThe Score Is Now "+ str(user_score) + ":" + str(comp_score) + "." )
print("Finished.")