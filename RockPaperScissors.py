#i am importing randint to generate random number
from random import randint
#here i am creating a list of the options for playing the rock, paper, scissors game
options = ["Rock", "Paper", "Scissors"]
#assigning a random option to the computer
computer = options[randint(0,2)]
#setting player to False
player = False
while player == False:
#setting player to True
    player = input("Which one will you choose? Rock, Paper or Scissors?\n")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("The Computer Wins!", computer, "Covers", player+". Better luck next time.")
        else:
            print("You Win YAY!", player, "Smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("The Computer Wins!", computer, "Cut", player+". Better luck next time.")
        else:
            print("You Win YAY!", player, "Covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("The Computer Wins!", computer, "Smashes", player+". Better luck next time.")
        else:
            print("You Win YAY!", player, "Cut", computer)
    else:
        print("Wrong spelling, try again.")
    #explanation: earlier, the player was set to True, but i want it to be False so the loop continues
    player = False
    computer = options[randint(0,2)]
