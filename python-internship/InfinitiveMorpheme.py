#WELCOME TO OUR GAME!
# player learns the infinite morphemes of Dothraki

import pickle 


#introduction to the story
print("\nAfter your last adventure, you go on and try to find hints to open the closed door.")
print("\nSuddenly you hear a quiet voice. 'Helloo! What are you doing here?!'")
print("The voice sounds excited.")
print("You see a very small princess running around in front of you.")
input("\nPress the enter key to continue.")

print("\nprincess:'I know what you are trying to find. It is so boring here because I am all alone and there is no one to play with me.")
print("If I give you some information about the dothraki language, will you play with me?'")

#asks the player if he wants to start the game 
players_decision = input("""Will you play with the princess? y - yes, n - no
                               Enter your choice: """)
players_decision = players_decision.lower()

while players_decision != "n" and players_decision != "y": 
   print("Please enter a valid choice!\n")
   players_decision = input("""Will you play with the princess? y - yes, n - no
                               Enter your choice: """)
   players_decision = players_decision.lower()

#player says he doesn't want to play
if players_decision == "n":
    print("\nprincess: 'That's too bad...'")
    print("The princess walks away.")
    input("\nPress the enter key to continue.") 

#player decides to play the game
while players_decision == "y":
      print("\nprincess:'Let's start!'")

      #STARTING THE FIRST GAME
      #MIX AND MATCH ("MAM")
      # import the game

      import mam

      #go on with the story
      #princess is talking to the player
      
      print("\n\n...princess:'Well done, you completed my first game! This is so exciting!'")
      print("Lets go on!\n")
      input("Press the enter key to go on.")

      #CONTINUE WITH THE SECOND GAME
      #FUN WITH STEMS
      #import the second game

      import fws

  
      #adding the infinitive morphemes to the scripts inventory of our hero
      infinitive_morpheme1 = "Infinitive morpheme after consonant: /-at/"
      infinitive_morpheme2 = "Infinitive morpheme after vowel: /-lat/"

      f=open("hero.dat", "rb+")
      hero=pickle.load(f) 

      #continue with story
      #princess is talking to the player
      print("\n\n ....princess: 'Congratulations! You completed all my tasks.'")
      print("Here are your new clues to decipher the dothraki language: ")
      hero.scripts_append(infinitive_morpheme1)
      hero.scripts_append(infinitive_morpheme2)
      hero.show_scripts() 
      print("\n 'Thank you for playing with me.'")
      print("Says the princess as she walks away.")
      input("\nPress the enter key to go on.")


        #exit the while loop 
      players_decision = "n"



#end of the game       
#ANIMATION: MOVING PRINCESS
#source: Inventwithpython (Sveigart)

# import pygame, sys
# from pygame.locals import *

# pygame.init()

# FPS = 30 #frames per second setting
# fpsClock = pygame.time.Clock()

# #set up the window
# DISPLAYSURF = pygame.display.set_mode((400,300), 0, 32)
# pygame.display.set_caption("Animation")

# WHITE = (255, 255, 255)
# princessImg = pygame.image.load("princess.png")
# princessx = 10
# princessy = 10
# direction = "right"

# while True:
    # #the main game loop
    # DISPLAYSURF.fill(WHITE)

    # if direction == "right":
            # princessx += 5
            # if princessx == 280:
                # direction == "down"
    # elif direction == "down":
            # princessy += 5
            # if princessy == 220:
                # direction = "left"
    # elif direction == "left":
            # princessx -= 5
            # if princessx == 10:
                # direction = "up"
    # elif direction == "up":
            # princessy -= 5
            # if princessy == 10:
                # direction = "right"

    # DISPLAYSURF.blit(princessImg, (princessx, princessy))

    # for event in pygame.event.get():
            # if event.type == QUIT:
                # pygame.quit()
                # sys.exit()

    # pygame.display.update()
	
##############

f.close() 