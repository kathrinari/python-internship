#group project
#by Hoa Do, Friederike Hohl and Naomi Reichmann
#dorvof

import pygame, sys

print("""\n\nYou find a door to a room where your next hint is. But the door is closed
and there is nobody around who can help you. Now you have two options: try
to break the door open or try to find a key.""")

choice = None #initialized

while choice == None:
    #user can choose between 1. break the door open or 2. finding the key
    #1. Naomi's mini game
    #2. Friederike's mini game
    #after the user successfully completes Naomi's mini game, Friederike's mini game will start
    #if user wins Friederike's game aswell, the program ends
    print("""\nYou can choose:
      1 - break it open  
      2 - find the key""")

    choice = input("\nWhat do you want to do?: ")

    #minigame 1
    if choice == "1":
        print("""\nSo, you think you can break open the door?
First, you need to answer some questions...""")
        #Naomi's game +  if user wins, Friederike's game starts
        import trivia

    #minigame 2
    elif choice == "2":
        print("\nGood luck finding the key.")
        #Friederike's game
        import Lava_Schollen_Spiel

    #invalid choice
    else:
        print(choice, "is invalid input. You can only enter 1 or 2.")
        choice = None


