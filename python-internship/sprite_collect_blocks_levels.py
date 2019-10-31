# Sample Python/Pygame Programs
# Simpson College Computer Science
# http://programarcadegames.com/
# http://simpson.edu/computer-science/
 
import pygame, sys
from pygame.locals import *
import random

#initialize Pygame
pygame.init()

#height and width of the screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

#definition of colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255,   0,   0)

#how fast the screen updates
clock = pygame.time.Clock()
font = pygame.font.Font(None, 25)
 
frame_count = 0
frame_rate = 60
start_time = 90



#font for drawing text on the screen (size 36)
font = pygame.font.Font(None, 30)
 
#current score
score = 0
 
#current level
level = 1

# This class represents the ball        
# It derives from the "Sprite" class in Pygame
class Block(pygame.sprite.Sprite):
     
    # Constructor. Pass in the color of the block, 
    # and its x and y position
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__() 
 
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values 
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

class button():
    def __init__(self, color, x, y, width, height, text = ""):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, outline=None):
        #call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(screen, outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

    def isOver(self, pos):
        #pos is the mouse position or a tuple of (x, y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

buttonQuit = button(BLACK, 300, 350, 100, 50, "")
buttonAgain = button(BLACK, 300, 400, 100, 50, "")
font2 = pygame.font.Font("freesansbold.ttf", 20)
text2 = font2.render("", True, WHITE, BLACK)
textrect2 = text2.get_rect()
 
#list of 'sprites.'
block_list = pygame.sprite.Group()
 
#list of every sprite, all blocks & the player block
all_sprites_list = pygame.sprite.Group()

x = 0
if x == 0:
    for i in range(10):
        #this represents a block
        block = Block(WHITE, 15, 15)
     
        #random location for the block
        block.rect.x = random.randrange(SCREEN_WIDTH)
        block.rect.y = random.randrange(SCREEN_HEIGHT)
         
        #add the block to the list of objects
        block_list.add(block)
        all_sprites_list.add(block)
 
#RED player block
player = Block(RED, 20, 15)
all_sprites_list.add(player)


while True:  #main loop
    screen.fill(BLACK)

    for event in pygame.event.get():
        #ending the game
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            #return(buttonQuit)
            #choice = None

        #current mouse position.
        pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if buttonQuit.isOver(pos):
                pygame.quit()
                sys.exit()
            elif buttonAgain.isOver(pos):
                x = 0
                
            
     
    #fetch the x and y out of the list, 
    #just like we'd fetch letters out of a string.
    #set the player object to the mouse location
    player.rect.x = pos[0]
    player.rect.y = pos[1]
     
    #see if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)  
     
    #check the list of collisions.
    for block in blocks_hit_list:
        score += 1
        print( score )
 
    #check to see if all the blocks are gone.
    #if they are, level up.
    if len(block_list) == 0:
        # Add one to the level
        level += 1
 
        #add more blocks. How many depends on the level.
        #also, an 'if' statement could be used to change what
        # happens customized to levels 2, 3, 4, etc.
        for i in range(level * 10):
            # This represents a block
            block = Block(WHITE, 15, 15)
 
            # Set a random location for the block
            block.rect.x = random.randrange(SCREEN_WIDTH)
            block.rect.y = random.randrange(SCREEN_HEIGHT)
             
            # Add the block to the list of objects
            block_list.add(block)
            all_sprites_list.add(block)

 
    #clear the screen
    screen.fill(BLACK)

      # --- Timer going up ---
    #calculate total seconds
    total_seconds = frame_count // frame_rate
 
    #divide by 60 to get total minutes
    minutes = total_seconds // 60
 
    #use modulus (remainder) to get seconds
    seconds = total_seconds % 60
 
    #use python string formatting to format in leading zeros
    output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)

 
    #blit to the screen
    text = font.render(output_string, True, WHITE)
    screen.blit(text, [10, 70])

    
    total_seconds = start_time - (frame_count // frame_rate)

    
    #divide by 60 to get total minutes
    minutes = total_seconds // 60
 
    #use modulus (remainder) to get seconds
    seconds = total_seconds % 60

    #use python string formatting to format in leading zeros
    output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
 
    #blit to the screen
    text = font.render(output_string, True, WHITE)
    screen.blit(text, [10, 100])

    #draw all the spites
    all_sprites_list.draw(screen)

    #texts 
    text = font.render("Score: "+str(score), True, WHITE)
    screen.blit(text, [10, 10])
         
    text = font.render("Level: "+str(level), True, WHITE)
    screen.blit(text, [10, 40])
    
    frame_count += 1

    #if time is over
    if total_seconds < 0 and score < 5:
        total_seconds = 0
        screen.fill(BLACK)
        text = font.render("You didn't succeed in collecting enough sprites. Game Over.", True, WHITE)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])
        #play again
        buttonQuit = button(BLACK, 300, 300, 100, 50, "quit")
        text2 = font.render("quit", True, WHITE)
        buttonAgain.draw(screen, WHITE)
        textrect2 = (100, 40)
        screen.blit(text2, textrect2)
        #quit and play other minigame
        buttonAgain = button(BLACK, 400, 300, 100, 50, "play again")

        text2 = font.render("play again", True, WHITE)
        buttonQuit.draw(screen, WHITE)
        screen.blit(text2, textrect2)

    if total_seconds < 0 and score > 400:
        total_seconds = 0
        screen.fill(BLACK)
        text = font.render("You succeed in collecting enough sprites. Congrats! You get the key.", True, WHITE)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])
        text2 = font.render("Open the door", True, BLACK, WHITE)
        textrect2 = (250, 250)
        screen.blit(text2, textrect2)
        
        #lava schollen spiel
        #the following code up until 'input("\n\nPress the enter key to exit.")' is by Friederike
        import random

        HANGMAN = (
        """
        ____________________
        |  ~     ~   ~     |
        |   ~   _______  ~ |
        |   ~  /       \   |
        | ~   /    0    \~ |
        |   ~|   /-+-/  |  |
        |~   |     |    | ~|
        |  ~  \   | |  /   |
        |  ~   \______/  ~ |
        |__________________|
        """,
        """
        ____________________
        |  ~     ~   ~     |
        |   ~     _____  ~ |
        |   ~  __/     \   |
        | ~   /    0    \~ |
        |   ~|   /-+-/  |  |
        |~   |     |    | ~|
        |  ~  \   | |  /   |
        |  ~   \______/  ~ |
        |__________________|
        """,
        """
        ____________________
        |  ~     ~   ~     |
        |   ~     _____  ~ |
        |   ~  __/     \   |
        | ~   /    0    \~ |
        |   ~|   /-+-/  |  |
        |~   |__   |    | ~|
        |  ~    \ | |  /   |
        |  ~     \____/  ~ |
        |__________________|
        """,
        """
        ____________________
        |  ~     ~   ~     |
        |   ~   ~ ___    ~ |
        |   ~  __/   \  ~  |
        | ~   /    0  \_ ~ |
        |   ~|   /-+-/  |  |
        |~   |__   |    | ~|
        |  ~    \ | |  /   |
        |  ~    ~\____/  ~ |
        |__________________|
        """,
        """
        ____________________
        |  ~     ~   ~     |
        |   ~   ~ ___    ~ |
        |     ~  /   \  ~  |
        | ~     /  0  \_ ~ |
        |   ~  | /-+-/  |  |
        |~     |   |    | ~|
        |  ~    \ | |  /   |
        |  ~    ~\____/  ~ |
        |__________________|
        """,
        """
        ____________________
        |  ~     ~   ~     |
        |   ~   ~    ~   ~ |
        |     ~  _____  ~  |
        | ~     /  0  \_ ~ |
        |   ~  | /-+-/  |  |
        |~     |   |    | ~|
        |  ~    \ | |  /   |
        |  ~    ~\____/  ~ |
        |__________________|
        """,
        """
        ____________________
        |  ~     ~   ~     |
        |   ~   ~    ~   ~ |
        |     ~  _____  ~  |
        | ~     /  0  \ ~  |
        |   ~  | /-+-/|   ~|
        |~     |   |  | ~  |
        |  ~    \ | |/   ~ |
        |  ~    ~\__/  ~   |
        |__________________|
        """,
        """
        ____________________
        |  ~     ~   ~     |
        |   ~   ~    ~   ~ |
        |     ~  ___    ~  |
        | ~     /  0|  ~   |
        |   ~  | /-+-/    ~|
        |~     |   | \ ~   |
        |  ~    \ | |/   ~ |
        |  ~    ~\__/  ~   |
        |__________________|
        """,
        """
        ____________________
        |  ~     ~   ~     |
        |   ~   ~    ~   ~ |
        |     ~  ~      ~  |
        | ~    ~   0   ~   |
        |   ~  __/-+-/    ~|
        |~     |   | \ ~   |
        |  ~    \ | |/   ~ |
        |  ~    ~\__/  ~   |
        |__________________|
        """,
        """
        ____________________
        |  ~     ~   ~     |
        |   ~   ~    ~   ~ |
        |     ~  ~      ~  |
        | ~    ~   0   ~   |
        |   ~    /-+-/    ~|
        |~     ~___|__ ~   |
        |  ~    \ | |/   ~ |
        |  ~    ~\__/  ~   |
        |__________________|
        """,
        """
        ____________________
        |  ~     ~   ~     |
        |   ~       ~    ~ |
        |   ~   ~      ~   |
        | ~        ~     ~ |
        |   ~              |
        |~        ~       ~|
        |  ~   ~     ~     |
        |  ~      ~      ~ |
        |__________________|
        """)

        MAX_WRONG = len(HANGMAN) - 1
        WORD = ("DORVOF")

        gap = "-"
        soFar = "-" * len(WORD)
        wrongGuesses = 0
        hints = 0
        lettersUsed = []

        print("""After you enter the room, you find yourself standing on a float,
                 surronded by nothing but lava. To get back you have to guess
                 the word you were looking for. But be carful, every time your guess
                 is wrong a pice of the float breakes of. Don't let your space get to small!""")

        #while loop to be able to repeat the game when failed
        y = True
        while y:
            #main loop
            while wrongGuesses < MAX_WRONG and soFar != WORD:
                print(HANGMAN[wrongGuesses])
                print("\nYou've used the following letters:\n", lettersUsed)
                print("\nSo far the word is:\n", soFar)

                guess = input("\n\nEnter your guess: ")
                guess = guess.upper()

                while guess in lettersUsed:
                    print("You've already guessed letter", guess)
                    guess = input("\n\nEnter your guess: ")
                    guess = guess.upper()

                lettersUsed.append(guess)

                x = True
                while x:
                    #right guess
                    if guess in WORD:
                        print("\nYour guess was right!")
                        new = ""
                        for i in range(len(WORD)):
                            if guess == WORD[i]:
                                new += guess
                            else:
                                new += soFar[i]
                        soFar = new
                        x = False

                    #get hint after 5/8 wrong guesses
                    elif (wrongGuesses == 5 and hints == 0) or (wrongGuesses == 8 and hints == 1):
                        print("\nYou get a hint.")
                        new = ""
                        hint = ""
                        #get "D"
                        if gap == soFar[0]:
                            hint += "D"
                            lettersUsed.append(hint)
                            for i in range(len(WORD)):
                                if hint == WORD[i]:
                                    new += hint
                                else:
                                    new += soFar[i]
                            soFar = new
                        #get "O", soFar[1] and soFar[4]
                        elif soFar[1] == gap:
                            hint += "O"
                            lettersUsed.append(hint)
                            for i in range(len(WORD)):
                                if hint == WORD[i]:
                                    new += hint
                                else:
                                    new += soFar[i]
                            soFar = new
                        #get "R"
                        elif soFar[2] == gap:
                            hint += "R"
                            lettersUsed.append(hint)
                            for i in range(len(WORD)):
                                if hint == WORD[i]:
                                    new += hint
                                else:
                                    new += soFar[i]
                            soFar = new
                        #get "V"
                        elif soFar[3] == gap:
                            hint += "V"
                            lettersUsed.append(hint)
                            for i in range(len(WORD)):
                                if hint == WORD[i]:
                                    new += hint
                                else:
                                    new += soFar[i]
                            soFar = new
                        #get "F"
                        elif soFar[5] == gap:
                            hint += "F"
                            lettersUsed.append(hint)
                            for i in range(len(WORD)):
                                if hint == WORD[i]:
                                    new += hint
                                else:
                                    new += soFar[i]
                            soFar = new
                        hints += 1
                        x = False

                   #wrong guess
                    else: 
                        print("\nSorry,", guess, "isn't in the word.")

                        wrongGuesses += 1
                        x = False
                
            if wrongGuesses == MAX_WRONG:
                print(HANGMAN[wrongGuesses])
                print("\nThere was no space left, so you fell into the lava.")
                print("\nYou have to try again.")
                #set variables back
                wrongGuesses = 0
                lettersUsed = []
                soFar = "-" * len(WORD)
                hints = 0
                y = True
            else:
                print("\nYou guessed the word and land savly on solid grounds.")
                print("\nThe word is", WORD)
                y = False

        input("\n\nPress the enter key to exit.")


    pygame.display.flip()
    clock.tick(60)


