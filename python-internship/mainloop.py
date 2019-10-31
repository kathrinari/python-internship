# Python Final Project Pygame 
# by Team Carlotte, Shauni, Laila, Jule

# Mainloop

# Code for Mainloop by Charlotte
# Code for Player and animation within Mainloop by Laila
# Starting sequence with tkinter by Jule
# Both parts assembled to run smoothly and functional by Shauni

def Mainloop():
    # all imports
    import pygame
    import random
    from os import path
    img_dir = path.join(path.dirname(__file__), 'img') #including folder "img"
    #setting frame size and speed as constants so they can be referenced in the game
    WIDTH = 1100
    HEIGHT = 500
    FPS = 30 #frames per second
    #define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    # initialize pygame and create window
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Jump and Run - Run")
    clock = pygame.time.Clock()
    # loading all game graphics
    # https://opengameart.org/content/platformer-art-deluxe by Kenney
    player_img = pygame.image.load('standing.png')
    obstacle_img = pygame.image.load(path.join(img_dir, 'pokerMad.png')).convert()
    coin_img = pygame.image.load(path.join(img_dir, 'coinGold.png')).convert()
    flag_img = pygame.image.load(path.join(img_dir, 'flagRed.png')).convert()
    door_img = pygame.image.load(path.join(img_dir, 'portal.png')).convert()
    cactus_img = pygame.image.load(path.join(img_dir, 'cactus.png')).convert()
    # defining the object classes for the game
    class Player(pygame.sprite.Sprite): #player
        #initializing the Sprite
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)				#initializing funktions for self
            self.image = player_img							#loading image
            self.rect = self.image.get_rect()				#getting rectangle sprite can be referenced by
            self.radius = int(self.rect.width *.80 / 2)		#getting a radius for corcle collision
            self.rect.centerx = 60							#starting position x
            self.rect.bottom = HEIGHT - 30					#starting position y
            self.speedy = 0									#initializing speed y
            self.speedx = 0									#initializing speed x
            self.y = self.rect.y
            self.isJump = False								#initial position is not jumping
            self.jumpCount = 10
            self.walkCount= 0
            self.counter = 0
        #defining an update function for the player that allows movement
        def update(self):
            #setting speed back to 0 at the beginning of every update
            #eliminates need to refer to key up elements
            #unless the key IS pressed the speed is 0   
            self.speedx = 0
            #gets every input in a list
            keystate = pygame.key.get_pressed()
            #changing direction to left
            if keystate[pygame.K_LEFT]:
                self.speedx = -7
			#changing direction to right
            if keystate[pygame.K_RIGHT]:
                self.speedx = 7
			#changing position = movement
            self.rect.x += self.speedx
            #moves player back to starting point when hitting this position
            if self.rect.right> WIDTH-110:
                self.rect.right = 50
                self.counter +=1
                #keeps track of succesful crossing, referenced in the game loop
                #print (self.counter) # --> Control print statement, not relevant for actual game but helped with development 
            if self.counter == 3:
			#prevents player from leaving screen
                running = False                  
            if self.rect.left < 0:
                    self.rect.left = 0
			#Making sure Player can only start jump from non jumping position
            if (self.isJump)==False:
                if keystate[pygame.K_SPACE]:
                    self.isJump = True         
            else:
                if self.jumpCount >= -10:
                        neg = 1
                        if self.jumpCount < 0:
                                neg = -1
                        self.rect.y -= (self.jumpCount ** 2)//2 * neg
                        self.jumpCount -= 1               
                else:
                        self.isJump = False
                        self.jumpCount = 10

    # Original Player Animation written By Laila Purpus
    # unfortunately we were unable to properly implement it within this file
    # it can be found within the ZIP file we submitted in a Folder called Player Animation

    ##    def draw(self):
    ##        if self.walkCount + 1 >= 54:
    ##            self.walkCount = 0
    ##
    ##        if self.speedx == 7:
    ##            screen.blit(walkLeft[walkCount//6], (self.y))
    ##            self.walkCount += 1
    ##
    ##        elif self.speedx == -7:
    ##            screen.blit(walkRight[walkCount//6], (self.y))
    ##            self.walkCount +=1
    ##
    ##        else:
    ##            screen.blit(player_img, (self.y))           
    #Obstacle classes
    class Obstacle(pygame.sprite.Sprite):
        def __init__(self, placement):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(obstacle_img,(30,100))  # adjusting size because the original graphic is too big
            self.image.set_colorkey(BLACK)      #eliminates the black surrounding the original graphic
            self.rect = self.image.get_rect()	#gets rectangle the original sprite can be referenced by
            self.rect.bottom = HEIGHT- 30		#placement on Y axis
            self.rect.x = placement 			#as the obstacles need to be spawned at different locations, the x variable is an argument 
            self.speedx = -4					#setting their speed
        def update(self): 						#changing x plaement (=movement)
            self.rect.x += self.speedx      	#part that allows movement
            #deletes sprite when it hits a certain position (in the game equal to the position of the cactus)
            if self.rect.right <= 190: 
                self.kill()
                #print(len(obstacles)) #--> Control print statement
    #Object class for coins
    #collecting them is the goal of the game
    class Coin(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = coin_img
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.radius = int(self.rect.width / 4)
            self.rect.centerx = random.randrange(200, WIDTH-150)
            self.rect.centery = HEIGHT-200
    #Flag to signal finish line
    #basically just a picture to blitted in the last runthrough 
    class Finish(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = flag_img
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.bottom = HEIGHT - 30
            self.rect.right = WIDTH - 90
    # portal because it's prettier if it doesn't just spawn from one end to the other
    # unfortunately the player is being blitted behind the two portals
    # x is an argument because there are 2 Portals
    class Portal(pygame.sprite.Sprite):
        def __init__(self, x):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(door_img,(100,100))
            self.rect = self.image.get_rect()
            self.rect.bottom = HEIGHT - 30
            self.rect.left = x
    #cactus, for improving visuals
    class Cactus(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(cactus_img,(70,150))
            self.image.set_colorkey(BLACK)
            self.rect = self.image.get_rect()
            self.rect.bottom = HEIGHT - 30
            self.rect.centerx = 170            
    #Initializing all the variables that will be needed within the game loop/for spawning
    #first the placement needed for the obstacles
    placement = WIDTH + 10
    #and the one needed to respawn obstacles in the game loop
    restart_point = 3000 
    #the varaible for collected coins
    #called score to avoid confusion
    score = 0
    #initializing counter that will determine when the game is over
    counter = 0
    #also it will determinen respawning of coins when combined with this variable
    counter_coins = 1
    #SPAWNING THE INITIAL SPRITES                          
    #creating a group that allows to update all sprites at once
    #in the update section further down
    all_sprites = pygame.sprite.Group()
    #also grouping all sprites of one kind together in groups for better handling
    obstacles = pygame.sprite.Group()
    coins = pygame.sprite.Group()
    flags = pygame.sprite.Group()
    #now spawning a player
    player = Player()
    #and adding to all sprites Group
    all_sprites.add(player)
    #spawning obstacles off screen
    for i in range (8):
        o = Obstacle(placement)
        all_sprites.add(o)
        obstacles.add(o)
        placement += random.randrange(200,600)  #each one spawned further out so they appear one by one
    #spawning coins       
    while len(coins)< 2:     # while function used so spawning continues until there are two
        c = Coin()
        hits = pygame.sprite.spritecollide(c, coins, True) #making sure they don't overlap, True making sure the one it collides with is deleted
        all_sprites.add(c) #then its added to the group
        coins.add(c)            
    #spawning the other sprites/images seen on screen
    portal_end = Portal(WIDTH-150)
    all_sprites.add(portal_end)
    portal_start = Portal(20)
    all_sprites.add(portal_start)
    cactus = Cactus()
    all_sprites.add(cactus)
	
    #Main Game loop
    running = True
    while running:
        # keep loop running at the right speed
        clock.tick(FPS)       
        # Process input (events)--> input for movement is being taken care of in the update section
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #Update       
        all_sprites.update()#calling every sprite's update function since all sprites are in the all_sprites group
        #syncing the counter variable with the player counter 
        counter = player.counter
        #collison control functions to check if Player hit an obstacle
        hits = pygame.sprite.spritecollide(player, obstacles, False)
        if hits:
            score = 0
            print('Sorry, all your coins are lost. Try again.')
            running = False
        #check if Player collected coin            
        hits = pygame.sprite.spritecollide(player, coins, True, pygame.sprite.collide_circle)
        if hits:
            score +=1             
        if counter_coins == counter: #this only happens when the player reached the edge of the window
            #after this, the remaining coins get deleted
            if c in coins:
                coins.remove(c)
                all_sprites.remove(c)               
            if c in coins:
                coins.remove(c)
                all_sprites.remove(c)                                  
            #new coins spawned
            while len(coins)< 2:
                c = Coin()
                hits = pygame.sprite.spritecollide(c, coins, True)
                all_sprites.add(c)
                coins.add(c)
            counter_coins += 1 #new coins are only spawned when player reached the end of the window
        #respawning an obstacle as soon as one is deleted/hits the cactus
        while len(obstacles)< 8:
            placement = restart_point + random.randrange(100,300)
            o = Obstacle(placement)
            pygame.sprite.spritecollide(o, obstacles, True)
            all_sprites.add(o)
            obstacles.add(o)           
        #deleting end portal for final run through
        if counter == 2:
            all_sprites.remove(portal_end)
        #instead spawning a flag for the finish line
        if not flags:
            if counter == 2:
                flag = Finish()
                all_sprites.add(flag)
                flags.add(flag)                    
        if counter == 3:
            print('You collected ', score, 'coins.') #print result in the info-window
            running = False #stop the game
        screen.fill(WHITE)
        all_sprites.draw(screen)
        pygame.display.flip()
    pygame.quit() #end the game
    return score #return score value to the starting sequence for further use
	


