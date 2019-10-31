### The cave room bonus level ### 

import random, pygame, sys, time
from pygame.locals import *

def caveRoom():
	global FPSCLOCK, DISPLAYSURFACE, response, Health, score, coorTraveled
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURFACE = pygame.display.set_mode((windowWidth,windowHeight))
	gameFont = pygame.font.Font('freesansbold.ttf', 26)
	pygame.display.set_caption('The Hidden Cave: Bonus Round')
	
	startScreen()
	while True:
		playGame()

def drawText(size, message, color, posX, posY): 
		fontType = pygame.font.Font('freesansbold.ttf', size)
		text = fontType.render(message, True, color)
		textRect = text.get_rect()
		textRect.topleft = (posX,posY)
		DISPLAYSURFACE.blit(text, textRect)		
		
def startScreen():
	while True:
		DISPLAYSURFACE.fill(Black)	
					
		drawText(50, 'THE HIDDEN CAVE', Gold, 53, 40) 
		drawText(25, 'Grab as much treasure as you can!', DarkGray, 63, 105) 
		drawText(25, 'But only enter if you dare...', Maroon, 63, 140) 
		drawText(20, 'Press Enter to begin game', Green, 195, 300) 
		drawText(20, "Press 'h' key for help menu", Silver, 193, 335) 

		def scaryEyes(posX1, posY1, posX2, posY2): 
			scaryEye_surf1 = pygame.Surface((30, 15))
			scaryEye_surf2 = pygame.Surface((30, 15))
			eye1 = pygame.draw.ellipse(scaryEye_surf1, White,(0,0,25,12))
			eye2 = pygame.draw.ellipse(scaryEye_surf2, White,(0,0,25,12))
			scaryEye_rot1 = pygame.transform.rotate(scaryEye_surf1, -10)
			scaryEye_rot2 = pygame.transform.rotate(scaryEye_surf2, 10)
			DISPLAYSURFACE.blit(scaryEye_rot1, (posX1, posY1))
			DISPLAYSURFACE.blit(scaryEye_rot2, (posX2, posY2))
		
		scaryEyes(540, 180, 570, 178) 
		scaryEyes(50, 210, 80, 208) 
		scaryEyes(330, 255, 360, 253) 
		scaryEyes(485, 400, 515, 398) 
		scaryEyes(165, 375, 195, 373) 
	
	
		# interprets user input
		response = checkForKeyPress()
		if response == 'START':
			break
		elif response == 'HELP':
			helpMenu()
		elif response == None:
			None
			
		pygame.display.update()
		FPSCLOCK.tick(FPS)

def helpMenu():
	x = True
	backRequest = None
	while x == True:
		# Main Title
		DISPLAYSURFACE.fill(Black)
		
		drawText(45, "Help Menu", DarkGray, 20, 20) 
		
		helpTextFont = pygame.font.Font('freesansbold.ttf', 15)
		controlsFont = pygame.font.Font('freesansbold.ttf', 12)
		
### KB: draw controls 
		drawText(12, "|                  UP                      |            W ", White, 400, 20) 
		drawText(12, "|              /            \                OR       /      \ ", White, 400, 33) 
		drawText(12, "|  LEFT / DOWN \ RIGHT   |   A   /   S   \   D ", White, 400, 46) 
		
### KB: draw help text 
		drawText(15, "The goal of this game is to navigate through the cave and collect as much treasure", White, 30, 80) 
		drawText(15, "   as possible before losing all of your health (Your health has been restored to 100).", White, 30, 100) 
		drawText(15, "In order to advance to the next level, you must clear the board of all of the coins and", White, 30, 120) 
		drawText(15, "   then return to the purple 'safe zone' squares (shown below). The coins will", White, 30, 140) 
		drawText(15, "   reset after the completion of each round.", White, 30, 160) 
		drawText(15, "Information:", White, 30, 180) 
		drawText(15, "  -  Lava: lava is too hot for your hero to venture onto these squares", White, 50, 200) 
		drawText(15, "  -  Cave Wall: solid rock is too hard for your hero to break through them", White, 50, 220) 
		drawText(15, "  -  Portal Gates: these squares will teleport your hero to the portal on the ", White, 50, 240) 
		drawText(15, "                              opposite side of the cave where entered", White, 50, 260) 
		drawText(15, "  -  Cave Floor: your hero can move freely along these squares", White, 50, 280) 
		drawText(15, "  -  Safe Zone: where each level starts and ends (once all coins are collected)", White, 50, 300) 
		drawText(15, "     Coins: treasure needed to be collected on each square, score +5", White, 50, 320) 
		drawText(15, "BEWARE OF:", Red, 50, 340) 
		drawText(15, "  -  Monsters: if your hero shares the same square with them, health -25pts", White, 50, 360) 
		drawText(15, "  -  Acid: if your hero moves onto these squares, health -10pts", White, 50, 380)  
		
		# draws examples of cell types in game
		pygame.draw.rect(DISPLAYSURFACE, Red, (50, 200, 15, 15))
		pygame.draw.rect(DISPLAYSURFACE, Gray, (50, 220, 15, 15))
		pygame.draw.rect(DISPLAYSURFACE, White, (50, 240, 15, 15))
		pygame.draw.rect(DISPLAYSURFACE, Brown, (50, 280, 15, 15))
		pygame.draw.rect(DISPLAYSURFACE, Purple, (50, 300, 15, 15))
		pygame.draw.circle(DISPLAYSURFACE, Gold, (59, 327), 4,0)
		pygame.draw.rect(DISPLAYSURFACE, Blue, (50, 360, 15, 15))
		pygame.draw.rect(DISPLAYSURFACE, Lime, (50, 380, 15, 15))
		
		# return to main menu info
		drawText(12, "Press 'b' key to return to main", Silver, 415, 425) 
		
		# interprets user input
		response = checkForKeyPress()
		if response == 'BACK':
			break
		else:
			None
		
		pygame.display.update()
		FPSCLOCK.tick(FPS)
		
	caveRoom()
	
def checkForKeyPress():
	response = None
	for event in pygame.event.get():
		if event.type == QUIT:
			terminate()
		elif event.type == KEYDOWN:
			if event.key == K_RETURN:
				response = 'START'
			elif event.key == K_ESCAPE:
				terminate()
			elif event.key == K_h:
				response = 'HELP'
			elif event.key == K_b:
				response = 'BACK'
			else:
				response = None
				
	return response
		
def drawGrid():
	# draw vertical lines
	for x in range(0, windowWidth, CELLSIZE): 
		pygame.draw.line(DISPLAYSURFACE, Black, (x, 0), (x, windowHeight))
	# draw horizontal lines
	for y in range(0, windowHeight, CELLSIZE): 
		pygame.draw.line(DISPLAYSURFACE, Black, (0, y), (windowWidth, y))

def drawGates():
	# first gate (left)
	pygame.draw.rect(DISPLAYSURFACE, White, (20, 200, 20, 40))
	# second gate (right)
	pygame.draw.rect(DISPLAYSURFACE, White, (600, 200, 20, 40))
	# third gate (top)
	pygame.draw.rect(DISPLAYSURFACE, White, (300, 20, 40, 20))
	# fourth gate (bottom)
	pygame.draw.rect(DISPLAYSURFACE, White, (300, 400, 40, 20))

def drawFloor():
	pygame.draw.rect(DISPLAYSURFACE, Brown, (40, 40, 560, 360))
	
def drawBarriers():

	def drawRect(color, coordinates): 
		pygame.draw.rect(DISPLAYSURFACE, color, coordinates)
	
### KB: might look more confusing, but saves space 
	# (x-dist, y-dist, width, length)
	coordGray=((20, 20, 280, 20),(20, 40, 20, 160),(340, 20, 280, 20),(600, 40, 20, 160),(20, 400, 280, 20),(20, 240, 20, 160),(340, 400, 280, 20),(600, 240, 20, 160)) 
		
	coordRed=((260, 160, 80, 20),(260, 220, 20, 60),(280, 260, 40, 20),(360, 160, 20, 80),(340, 260, 40, 20),(260, 180, 20, 20),(60, 60, 100, 20),(60, 100, 60, 20),(60, 120, 20, 40),(100, 140, 100, 20),(140, 100, 40, 20),(180, 80, 20, 40),(180, 60, 100, 20),(260, 80, 20, 60),(220, 100, 20, 160),(180, 180, 20, 100),(140, 280, 100, 20),(60, 180, 100, 20),(140, 220, 20, 40),(100, 200, 20, 40),(60, 220, 20, 60),(60, 260, 60, 20),(420, 60, 80, 20),(520, 60, 60, 20),(440, 100, 20, 40),(480, 100, 20, 40),(520, 100, 20, 40),(560, 100, 20, 40),(440, 160, 140, 20),(60, 300, 20, 80),(80, 300, 40, 20),(100, 340, 20, 40),(140, 300, 20, 80),(180, 320, 120, 20),(180, 360, 100, 20),(260, 300, 40, 20),(300, 360, 40, 20),(320, 300, 20, 40),(360, 300, 20, 80),(360, 300, 20, 80),(380, 300, 60, 20),(440, 340, 20, 40),(400, 340, 40, 20),(560, 360, 20, 20),(520, 320, 20, 60),(540, 320, 40, 20),(480, 280, 20, 100),(460, 300, 20, 20),(500, 280, 80, 20),(500, 220, 20, 80),(500, 180, 20, 20),(540, 200, 40, 20),(560, 220, 20, 20),(540, 240, 40, 20),(400, 160, 20, 120),(420, 260, 40, 20),(440, 200, 40, 40),(300, 120, 120, 20),(400, 60, 20, 60),(300, 60, 80, 20),(320, 80, 40, 20))
	
	drawRect(Purple, (300, 200, 40, 40)) 
	
	for tuple in coordGray: 
		drawRect(Gray, tuple) 
	
	for tuple in coordRed: 
		drawRect(Red, tuple) 

def drawHealthBar(Health):
	pygame.draw.rect(DISPLAYSURFACE, DarkGray, (50, 405, 240, 30))
	if Health <= 0:					# Health is empty if below 0
		None
	elif Health > 0:				
		fraction = Health / 100		# if health is above 0, then the health bar is that percent out of 100%
		if Health > 25:
			pygame.draw.rect(DISPLAYSURFACE, Lime, (55, 410, 230*fraction, 20))		# green if above 25%
		elif Health <= 25 and Health > 0:
			pygame.draw.rect(DISPLAYSURFACE, Maroon, (55, 410, 230 * fraction, 20))	# red if 25% or below
	
def drawScoreCounter(score):
	scoreStr = str(score)
	
	pygame.draw.rect(DISPLAYSURFACE, DarkGray, (350, 405, 240, 30))
	
	# Writes text of score
	drawText(26, 'Score: %s' % (scoreStr), White, 360, 408) 

def drawCoins(coorTraveled):
	coinsNeeded = 0		# resets to count how many coins still need to be collected
	
# 2 for loops ( for x-dir and y-dir) cycle through the proper coordinates to draw a coin on every square
	for x in range(40,600,20):
		for y in range(40,400,20):
			cellColor = DISPLAYSURFACE.get_at((x,y))
			if cellColor != Red and cellColor != Lime and cellColor != Purple:		# coins are drawn after other squares so coins are not drawn on barriers
				if y not in coorTraveled[x]:											# dictionary keeps track of which squares the hero has visited
					pygame.draw.circle(DISPLAYSURFACE, Gold, (x + 10, y + 10), 4,0)			# if the hero hasn't been there yet, the coin is drawn
					coinsNeeded += 1														# once coinsNeeded remains at zero, then the user can end the level
	return coinsNeeded
	
def drawAcid():
	pygame.draw.rect(DISPLAYSURFACE, Lime, (120, 100, 20, 20))
	pygame.draw.rect(DISPLAYSURFACE, Lime, (240, 280, 20, 20))
	pygame.draw.rect(DISPLAYSURFACE, Lime, (440, 300, 20, 20))
	pygame.draw.rect(DISPLAYSURFACE, Lime, (560, 140, 20, 20))
	pygame.draw.rect(DISPLAYSURFACE, Lime, (120, 320, 20, 20))
	pygame.draw.rect(DISPLAYSURFACE, Lime, (280, 60, 20, 20))	
	
def monsterMovement(monsterPosition, playerPosition, Health):
	
	monsterStart={"M1":[40,40], "M2":[580,40], "M3":[40,380], "M4":[580,380]}
	
	M_colors = [Red, Gray, White, Blue, Purple]		# colors that monsters aren't allowed to travel onto
	
	heroPos_x = playerPosition['x']
	heroPos_y = playerPosition['y']
	
	for monster in monsterPosition.keys(): 
### KB: gets the value (=positions) of each key (=monster) and then splitting it in x and y coordinates 	
		MP_x = monsterPosition[monster][0]
		MP_y = monsterPosition[monster][1]
		
		upCheck    = DISPLAYSURFACE.get_at((MP_x,      MP_y - 1))
		downCheck  = DISPLAYSURFACE.get_at((MP_x,      MP_y + 21))
		leftCheck  = DISPLAYSURFACE.get_at((MP_x - 5,  MP_y))
		rightCheck = DISPLAYSURFACE.get_at((MP_x + 25, MP_y)) 
		
	# Initializing list for possible directions that can be traveled by each monster
		choices = []
		
	# If that direction is allowed (not a barrier, gate, safe zone, etc.), then its added to the list
	# UP = 0; DOWN = 1; LEFT = 2; RIGHT = 3
	
		if upCheck not in M_colors:
			choices.append(0)
		if downCheck not in M_colors:
			choices.append(1)
		if leftCheck not in M_colors:
			choices.append(2)
		if rightCheck not in M_colors:
			choices.append(3)
			
	# randomly choose a direction from the options within the list for each monster	
		randomDirection= random.randint(0,len(choices) - 1)
		
	# Calculate new position by changing which pixel the monster is drawn from:		
		if choices[randomDirection] == 0:
			MP_y = MP_y - 20
		elif choices[randomDirection] == 1:
			MP_y = MP_y + 20
		elif choices[randomDirection] == 2:
			MP_x = MP_x - 20
		elif choices[randomDirection] == 3:
			MP_x = MP_x + 20

	# Decrease health of hero if monster and hero are on the same spot
	#	and teleport monster back to its starting location
		if (MP_x == heroPos_x and MP_y == heroPos_y):
			Health -= 25
			MP_x = monsterStart[monster][0]
			MP_y = monsterStart[monster][1]		
			
	# Store new monster positions
		monsterPosition[monster] = [MP_x, MP_y]

	return monsterPosition, Health
	
def playerMovement(playerPosition, move, Health, score):
	# if the user pressed either the 'LEFT' or 'A' key 
	if move == 'left':
		color_code = DISPLAYSURFACE.get_at((playerPosition['x'] - 5,playerPosition['y']))			# checking color of cell to left of hero
		
		coinCheck  = DISPLAYSURFACE.get_at((playerPosition['x'] - 10, playerPosition['y'] + 10))	# checking if there is a coin to the left of the hero
		
		if color_code == Red or color_code == Gray:			# if the adjacent cell is a barrier
			move = None										
		elif color_code == White:							# if the adjacent cell is a gate
			playerPosition['x'] = 580							# teleport hero to opposite side of the board
		else:												# else		
			if color_code == Lime:								# if the adjacent cell is acid
				Health -= 10										# damage the hero's health
			if coinCheck == Gold:								# if there is a coin on the adjacent cell
				score += 5											# increase player's score
			playerPosition['x'] -= 20							# move hero to this cell 
	
	# if the user pressed either the 'RIGHT' or 'D' key
	elif move == 'right':
		color_code = DISPLAYSURFACE.get_at((playerPosition['x'] + 25,playerPosition['y']))			# checking color of cell to right of hero
		
		coinCheck = DISPLAYSURFACE.get_at((playerPosition['x'] + 30, playerPosition['y'] + 10))		# checking if there is a coin to the right of the hero
		
		if color_code == Red or color_code == Gray:			# if the adjacent cell is a barrier
			move = None
		elif color_code == White:							# if the adjacent cell is a gate
			playerPosition['x'] = 40							# teleport hero to opposite side of the board					
		else:												# else		
			if color_code == Lime:								# if the adjacent cell is acid
				Health -= 10										# damage the hero's health
			if coinCheck == Gold:								# if there is a coin on the adjacent cell
				score += 5											# increase player's score
			playerPosition['x'] += 20					
	
	# if the user pressed either the 'UP' or 'W' key			
	elif move == 'up':
		color_code = DISPLAYSURFACE.get_at((playerPosition['x'],playerPosition['y'] - 5))			# checking color of cell above the hero
		
		coinCheck = DISPLAYSURFACE.get_at((playerPosition['x'] + 10, playerPosition['y'] - 10))		# checking if there is a coin above the hero
		
		if color_code == Red or color_code == Gray:			# if the adjacent cell is a barrier
			move = None
		elif color_code == White:							# if the adjacent cell is a gate
			playerPosition['y'] = 380							# teleport hero to opposite side of the board
		else:												# else		
			if color_code == Lime:								# if the adjacent cell is acid
				Health -= 10										# damage the hero's health
			if coinCheck == Gold:								# if there is a coin on the adjacent cell
				score += 5											# increase player's score
			playerPosition['y'] -= 20							# move hero to this cell
	
	# if the user pressed either the 'DOWN' or 'S' key
	elif move == 'down':
		color_code = DISPLAYSURFACE.get_at((playerPosition['x'],playerPosition['y'] + 21))			# checking color of cell below the hero
		
		coinCheck = DISPLAYSURFACE.get_at((playerPosition['x'] + 10, playerPosition['y'] + 30))		# checking if there is a coin below the hero
		
		if color_code == Red or color_code == Gray:			# if the adjacent cell is a barrier
			move = None
		elif color_code == White:							# if the adjacent cell is a gate
			playerPosition['y'] = 40							# teleport hero to opposite side of the board
		else:												# else		
			if color_code == Lime:								# if the adjacent cell is acid
				Health -= 10										# damage the hero's health
			if coinCheck == Gold:								# if there is a coin on the adjacent cell
				score += 5											# increase player's score
			playerPosition['y'] += 20							# move hero to this cell

	newPosition_x  =  playerPosition['x'] 				# reassign hero's position in the x direction
	newPosition_y  =  playerPosition['y'] 				# reassign hero's position in the y direction 

	return {'x': newPosition_x, 'y': newPosition_y}, Health, score
	
def playGame():

### KB: Starting position of player	
	playerStart = {'x': 300, 'y': 200}
	
### KB: Starting positions of monsters 
	monsterStart = {"M1":[40,40], "M2":[580,40], "M3":[40,380], "M4":[580,380]}
	
### KB: Hero and monsters positions equals starting position in the beginning 
	playerPosition = playerStart
	monsterPosition = monsterStart
	
	drawHero(playerPosition)
	drawMonsters(monsterPosition)
	
	# initializing/ reseting variabels for the start of each level
	move = None
	Health = 100
	score = 0
	coinsNeeded = 100
	currentLevel = 1
	
	# Dictionary which keeps track of which cells the hero has traveled on		
	# This is used when determining how many coins must still be collected and where to draw the remaining ones
	# The keys are the x-coordinates and the values and the corresponding y-coordinates
	coorStart = {40: [20], 60: [20], 80: [20], 100: [20], 120: [20], 140: [20],
				160: [20], 180: [20], 200: [20], 220: [20], 240: [20], 260: [20],
				280: [20], 300: [20], 320: [20], 340: [20], 360: [20], 380: [20],
				400: [20], 420: [20], 440: [20], 460: [20], 480: [20], 500: [20],
				520: [20], 540: [20], 560: [20], 580: [20]}
	
	coorTraveled = coorStart
	
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				terminate()
			elif event.type == KEYDOWN:
				if (event.key == K_LEFT or event.key == K_a):
					move = 'left'
				elif (event.key == K_RIGHT or event.key == K_d):
					move = 'right'
				elif (event.key == K_UP or event.key == K_w):
					move = 'up'
				elif (event.key == K_DOWN or event.key == K_s):
					move = 'down'
				elif event.key == K_ESCAPE:
					terminate()
				
				playerPosition, Health, score = playerMovement(playerPosition, move, Health, score)
				
				coorTraveled[playerPosition['x']].append(playerPosition['y'])		
		
		# once all the coins are collected, the player can move onto the next level
			# this if statement checks if:
			#	- all coins are collected
			#	- if the hero has returned to the purple, 'safe zone' squares
			# and then, if true:
			#	- adds one to the current level counter
			#	- resets the dictionary of where the hero has traveled
			#	- resets the hero's position
			#	- resets the monsters' positions
			
		if coinsNeeded == 0:
			CC1 = DISPLAYSURFACE.get_at((playerPosition['x'] + 25, playerPosition['y'] + 5)) # right
			CC2 = DISPLAYSURFACE.get_at((playerPosition['x'] - 5, playerPosition['y'] + 5))  # left
			CC3 = DISPLAYSURFACE.get_at((playerPosition['x'] + 5, playerPosition['y'] - 5))  # up
			CC4 = DISPLAYSURFACE.get_at((playerPosition['x'] + 5, playerPosition['y'] + 25)) # down
			if (CC1 == Purple and CC3 == Purple) or (CC1 == Purple and CC4 == Purple) or (CC2 == Purple and CC3 == Purple) or (CC2 == Purple and CC4 == Purple):
				currentLevel += 1
				coorTraveled = coorStart
				playerPosition = playerStart			
				monsterPosition = monsterStart
				coinsNeeded = drawCoins(coorTraveled)
			
		drawFloor()
		drawGrid()
		drawGates()
		drawBarriers()
		drawAcid()
		nextLevel(currentLevel)
		coinsNeeded = drawCoins(coorTraveled)
		
		drawScoreCounter(score)
		
		monsterPosition, Health = monsterMovement(monsterPosition, playerPosition, Health)
		
		drawHealthBar(Health)
		
		drawMonsters(monsterPosition)
		
		drawHero(playerPosition)
		
		pygame.display.update()
		FPSCLOCK.tick(FPS)
		
		if Health <= 0:
			gameOver()

def drawMonsters(monsterPosition): 
	for monster in monsterPosition.keys(): 
		pygame.draw.rect(DISPLAYSURFACE, Blue, (monsterPosition[monster][0], monsterPosition[monster][1], 20, 20)) 

def drawHero(playerPosition):
	pygame.draw.rect(DISPLAYSURFACE, Aqua, (playerPosition['x'], playerPosition['y'], 20, 20))
	
def nextLevel(currentLevel):
	# draws the current level in the top left of the game window
	EndFont = pygame.font.Font('freesansbold.ttf', 18)
	ShowLevel = EndFont.render('Level %s' % (str(currentLevel)), True, White)
	ShowLevelRect = ShowLevel.get_rect()
	ShowLevelRect.topleft = (45,21)
	DISPLAYSURFACE.blit(ShowLevel, ShowLevelRect)

def gameOver():
	while True:
		# prints Game Over text
		EndFont = pygame.font.Font('freesansbold.ttf', 75)
		GameOver = EndFont.render('Game Over', True, Black)
		GameOverRect = GameOver.get_rect()
		GameOverRect.topleft = (115,60)
		DISPLAYSURFACE.blit(GameOver, GameOverRect)
	
		# informs user how to close the game with text
		CloseFont = pygame.font.Font('freesansbold.ttf', 20)
		CloseText = CloseFont.render("Press Esc to close game", True, Black)
		CloseTextRect = CloseText.get_rect()
		CloseTextRect.topleft = (195,300)
		DISPLAYSURFACE.blit(CloseText, CloseTextRect)
	
		# informs user how to play the game again with text
		ReplayFont = pygame.font.Font('freesansbold.ttf', 20)
		ReplayText = ReplayFont.render("Press Enter to play again", True, Black)
		ReplayTextRect = ReplayText.get_rect()
		ReplayTextRect.topleft = (195,325)
		DISPLAYSURFACE.blit(ReplayText, ReplayTextRect)
	
		pygame.display.update()
		FPSCLOCK.tick(FPS)
		
		# checks for user input
		response = checkForKeyPress()
		if response == 'START':
			playGame()

def terminate():
	pygame.quit()
	sys.exit()

FPS = 10
windowWidth = 640
windowHeight = 440
CELLSIZE = 20

# Color Codes
Aqua	=	(  0, 255, 255, 255)		# Hero
Black	=	(  0,   0,   0, 255)		# BGC / Grid
Blue	=	(  0,  0, 255, 255)			# Monsters
Brown	=	(199,  97,  20, 255)		# Cave Floor
DarkGray =  ( 91,  91,  91, 255)		# Box for Health and Score / Text
Gray	=	(128, 128, 128, 255)		# Barriers / Text
Green	=	(  0, 128,   0, 255)		# Main Menu Text
Gold	=	(255, 215,   0, 255)		# Coins
Lime	=	(  0, 255,   0, 255)		# Acid
Maroon	=	(128,  0,   0, 255)			# Low-Health Bar / Text
Purple	=	(128,  0, 128, 255)			# Start / Safe Zone
Red		=	(255,   0,   0, 255)		# Barriers
Silver	=	(192, 192, 192, 255)		# Text
Yellow	=	(255, 255,   0, 255)		# Text
White	=	(255, 255, 255, 255)		# Gates / Text / Scary Eyes

caveRoom()