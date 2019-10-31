#trivia animation
#mini game for the final project
#the following code is written by Naomi Reichmann
#except for the Button class, which I borrowed from Tech With Tim (YouTube channel)

import pygame, sys, random
from pygame.locals import *

pygame.init()
score = 0  #variable to track the score the user achieves, which decides whether they can open the door or not

fpsClock = pygame.time.Clock()
FPS = 30  #frames per second

#window set up
DISPLAYSURF = pygame.display.set_mode((900, 600), 0, 32)
pygame.display.set_caption("final project")  #caption of the window


WHITE = (255, 255, 255)  #color of the bar
PURPLE = (50, 0, 50)  #background color
BLACK = (0, 0, 0)  #text color


class button():  
    def __init__(self, color, x, y, width, height, text = ""):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, DISPLAYSURF, outline=None):  #call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(DISPLAYSURF, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)

        pygame.draw.rect(DISPLAYSURF, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != "":
            font = pygame.font.SysFont("freesansbold.ttf", 20)
            text = font.render(self.text, 1, (0, 0, 0))
            DISPLAYSURF.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #pos is the mouse position or a tuple of (x, y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False
   

#parameters     color   x   y   width height text
button1 = button(WHITE, 10, 300, 100, 50,     "") 
button2 = button(WHITE, 10, 360, 100, 50,     "")
button3 = button(WHITE, 10, 420, 100, 50,     "")
button4 = button(WHITE, 10, 480, 100, 50,     "")
buttonQuit = button(WHITE, 450, 350, 100, 50, "")
buttonAgain = button(WHITE, 300, 350, 100, 50, "")


font1 = pygame.font.Font("freesansbold.ttf", 65) #font for the text in the game
font2 = pygame.font.Font("freesansbold.ttf", 20)
text1 = font1.render("", True, BLACK, WHITE)  #the text is an empty string for now, it will be inserted later 
textSurfaceObj = font2.render("", True, BLACK, WHITE)
textrect1 = text1.get_rect()
textRectObj = textSurfaceObj.get_rect()
textrect1 = (260, 170)
textrect2 = (310, 250)
textRectObj = (10, 250)  #x and y coordinates of the upper left corner of the rectangle
DISPLAYSURF.blit(textSurfaceObj, textRectObj)

x = 0

running=True
while running:  #main loop
    DISPLAYSURF.fill(PURPLE)  #filling the background with purple

    for event in pygame.event.get():
        #ending the game
        if event.type == QUIT:
            #the window closes when the user presses the x button
### KB: I added the text for context, since I changed the game to play the Lava_Schollen_Spiel automatically after either winning, losing or quitting
            print("\n\nSo you changed your mind and you would rather search for the key? Alright...\n")
            running=False
			
			#pygame.quit()
            #sys.exit()
			
			
        elif event.type == K_ESCAPE:
            #the window closes when the user presses the escape button
            #pygame.display.quit()
### KB: I added the text for context, since I changed the game to play the Lava_Schollen_Spiel automatically after either winning, losing or quitting
            print("\n\nSo you changed your mind and you would rather search for the key? Alright...\n")
            running=False
			
			#pygame.quit()
            #sys.exit()
			
			
        elif event.type == KEYDOWN and x == 7 and score >= 4:  #when the user wins they can press any key and Friederike's game will start
            print("\n\nYOU DID IT! Now you can walk through the door.\n")

            #importing Friederike's game
            #import Lava_Schollen_Spiel
            running=False
			
			#pygame.quit()
            #sys.exit()
            

        pos = pygame.mouse.get_pos()  #mouse position

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button1.isOver(pos) and x == 2:  
                #print("score + 1")  #I used the print statement just to make sure that the commands were working
                score += 1  #the answer is correct, so 1 is added to the score
                x += 1  #adding 1 to x, so that the next question is displayed after the user clicked on the display 
            elif button1.isOver(pos) and x == 4:  
                #print("score + 1")
                score += 1
                x += 1
            elif button2.isOver(pos) and x == 0:  
                #print("score + 1")
                score += 1
                x += 1
            elif button2.isOver(pos) and x == 3:
                #print("score + 1")
                score += 1
                x += 1
            elif button2.isOver(pos) and x == 6:
                #print("score + 1")
                score += 1
                x += 1
            elif button3.isOver(pos) and x == 1:  
                #print("score + 1")
                score += 1
                x += 1
            elif button4.isOver(pos) and x == 5:  
                #print("score + 1")
                score += 1
                x += 1
            elif buttonQuit.isOver(pos):  
                #quitting my game
                #user can change to hangman game 
                #import Lava_Schollen_Spiel
### KB: I added the text for context, since I changed the game to play the Lava_Schollen_Spiel automatically after either winning, losing or quitting
                print("\n\nSo you changed your mind and you would rather search for the key? Alright...\n")
                running=False
               
			   #pygame.quit()
                #sys.exit()
				
            elif buttonAgain.isOver(pos):  #if the user presses the play again button, the game restarts
                x = 0  #x is set to 0 again, so that the first question is displayed again
                score = 0  #the score is set to 0 because the game starts over
            else:
                #print("score = 0")
                score += 0  #the answer wasn't correct, so the score stays the same
                x += 1  #1 is added to x to move on to the next question
                
           
    if x == 0:  #question 1
        textSurfaceObj = font2.render("Question 1: Which 200-year old brand of bourbon is the largest selling in the world?", True, BLACK, WHITE)
        button1 = button(WHITE, 10, 300, 100, 50, "Blanton's")  #answer 1
        button1.draw(DISPLAYSURF, BLACK)
        button2 = button(WHITE, 10, 360, 100, 50, "Jim Beam")  #answer 2
        button2.draw(DISPLAYSURF, BLACK)
        button3 = button(WHITE, 10, 420, 100, 50, "Knob Creek")  #answer 3
        button3.draw(DISPLAYSURF, BLACK)
        button4 = button(WHITE, 10, 480, 100, 50, "W.L. Weller")  #answer 4
        button4.draw(DISPLAYSURF, BLACK)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)
       

    elif x == 1:  #question 2
        textSurfaceObj = font2.render("Question 2: What is the most spoken language in the world?", True, BLACK, WHITE)
        button1 = button(WHITE, 10, 300, 100, 50, "Spanish")  #answer 1
        button1.draw(DISPLAYSURF, BLACK)
        button2 = button(WHITE, 10, 360, 100, 50, "English")  #answer 2
        button2.draw(DISPLAYSURF, BLACK)
        button3 = button(WHITE, 10, 420, 100, 50, "Chinese")  #answer 3
        button3.draw(DISPLAYSURF, BLACK)
        button4 = button(WHITE, 10, 480, 100, 50, "Hindi")  #answer 4
        button4.draw(DISPLAYSURF, BLACK)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    elif x == 2:  #question 3
        textSurfaceObj = font2.render("Question 3: What is the longest river in the world?", True, BLACK, WHITE)
        button1 = button(WHITE, 10, 300, 100, 50, "Amazon")  #answer 1
        button1.draw(DISPLAYSURF, BLACK)
        button2 = button(WHITE, 10, 360, 100, 50, "Mississippi")  #answer 2
        button2.draw(DISPLAYSURF, BLACK)
        button3 = button(WHITE, 10, 420, 100, 50, "Río Grande")  #answer 3
        button3.draw(DISPLAYSURF, BLACK)
        button4 = button(WHITE, 10, 480, 100, 50, "Volga")  #answer 4
        button4.draw(DISPLAYSURF, BLACK)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    elif x == 3:  #question 4
        textSurfaceObj = font2.render("Question 4: The Earth's air is composed of about what percentage of CO2?", True, BLACK, WHITE)
        button1 = button(WHITE, 10, 300, 100, 50, "0.52%")  #answer 1
        button1.draw(DISPLAYSURF, BLACK)
        button2 = button(WHITE, 10, 360, 100, 50, "0.04%")  #answer 2
        button2.draw(DISPLAYSURF, BLACK)
        button3 = button(WHITE, 10, 420, 100, 50, "0.2%")  #answer 3
        button3.draw(DISPLAYSURF, BLACK)
        button4 = button(WHITE, 10, 480, 100, 50, "0.98%")  #answer 4
        button4.draw(DISPLAYSURF, BLACK)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    elif x == 4:  #question 5
        textSurfaceObj = font2.render("Question 5: What is the largest country based on surface area?", True, BLACK, WHITE)
        button1 = button(WHITE, 10, 300, 100, 50, "Russia")  #answer 1
        button1.draw(DISPLAYSURF, BLACK)
        button2 = button(WHITE, 10, 360, 100, 50, "USA")  #answer 2
        button2.draw(DISPLAYSURF, BLACK)
        button3 = button(WHITE, 10, 420, 100, 50, "Canada")  #answer 3
        button3.draw(DISPLAYSURF, BLACK)
        button4 = button(WHITE, 10, 480, 100, 50, "China")  #answer 4
        button4.draw(DISPLAYSURF, BLACK)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    elif x == 5:  #question 6
        textSurfaceObj = font2.render("Question 6: What is the northernmost country in Europe?", True, BLACK, WHITE)
        button1 = button(WHITE, 10, 300, 100, 50, "Sweden")  #answer 1
        button1.draw(DISPLAYSURF, BLACK)
        button2 = button(WHITE, 10, 360, 100, 50, "United Kingdom")  #answer 2
        button2.draw(DISPLAYSURF, BLACK)
        button3 = button(WHITE, 10, 420, 100, 50, "Finland")  #answer 3
        button3.draw(DISPLAYSURF, BLACK)
        button4 = button(WHITE, 10, 480, 100, 50, "Norway")  #answer 4
        button4.draw(DISPLAYSURF, BLACK)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    elif x == 6:  #question 7
        textSurfaceObj = font2.render("Question 7: Which country is closest to Africa?", True, BLACK, WHITE)
        button1 = button(WHITE, 10, 300, 100, 50, "Greece")  #answer 1
        button1.draw(DISPLAYSURF, BLACK)
        button2 = button(WHITE, 10, 360, 100, 50, "Spain")  #answer 2
        button2.draw(DISPLAYSURF, BLACK)
        button3 = button(WHITE, 10, 420, 100, 50, "Malta")  #answer 3
        button3.draw(DISPLAYSURF, BLACK)
        button4 = button(WHITE, 10, 480, 100, 50, "France")  #answer 4
        button4.draw(DISPLAYSURF, BLACK)
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

    elif x == 7:
        if score < 4:  #user loses
            #game over screen
            text1 = font1.render("YOU LOST", True, BLACK, WHITE)
            textSurfaceObj = font2.render("the door remains closed", True, BLACK, WHITE)
            DISPLAYSURF.blit(text1, textrect1)
            DISPLAYSURF.blit(textSurfaceObj, textrect2)

            #quit and play other minigame
            buttonQuit = button(WHITE, 450, 350, 100, 50, "find the key")
            buttonAgain.draw(DISPLAYSURF, BLACK)

            #play again
            buttonAgain = button(WHITE, 300, 350, 100, 50, "play again")
            buttonQuit.draw(DISPLAYSURF, BLACK)

        elif score >= 4:  
            #player wins and moves 1 step forward
            text1 = font1.render("YOU WON!", True, BLACK, WHITE)
            font2 = pygame.font.Font("freesansbold.ttf", 28)
            textSurfaceObj = font2.render("now you can open the door", True, BLACK, WHITE)

            #when the player presses the key, Friederike's game starts
            text3 = font2.render("press a key to exit", True, BLACK, WHITE)
            textRectObj = (250, 250)  
            textrect3 = (600, 500)
            DISPLAYSURF.blit(text1, textrect1)
            DISPLAYSURF.blit(textSurfaceObj, textRectObj)
            DISPLAYSURF.blit(text3, textrect3)    
        
            
    pygame.display.update()
    fpsClock.tick(FPS)
	
### KB: Close pygame window after escaping the loop by either winning, losing or quitting 
pygame.quit()

### KB: Play the second minigame
import Lava_Schollen_Spiel