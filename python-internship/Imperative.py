######### PYTHON GAME PROJECT: IMPERATIVE FORM #########

# Our names are written next to sections we have done:
#            Poppie Dryer: intro and ending, central game, bringing game together
#            Oguzhan Kuyrucku: Mini game 2 (Dragon game)
#            Zsofia Lelner: Mini game 1 (Sphynx game)

import random, sys, pickle 

f=open("hero.dat", "rb+")
hero=pickle.load(f)  

# KEY VARIABLES
########## Oguzhan
pot_inventory = [] #seperate inventory for potions so it's easy to count them (Oguzhan Kuyrukcu)
pots = len(pot_inventory)

#########Poppie
GAME=""
MC_choice=0
Parchment=[]

####### Zsofia
# Variables specific to the Sphynx Mini game:
field = 0
round = 0
points = 0
sphynx_gifts = ["knife", "sword", "gun", "lance"] # weapons offered by the sphynx in the game, added to the main inventory
monsters = ["witch", "ogre", "troll", "dragon"]
itinerary = []

# Mini games
def Mini_game1():

    ######### BEGINNING OF ZSOFIA LELNER'S SECTION #########
    ######### MINI GAME: THE BOARD GAME OF THE SPHYNX #########
    # Objective: obtain items needed in order to play the dragon game.
    # The hero takes 1-4 steps chosen ranadomly.
    # The phials and the health potions are added to different lists.
    # You must do 3 types of tasks in order to obtain the objects.

    # Introducing the variables from outside
    global field, round, points, sphynx_gifts, monsters
	
	# KEY VARIABLES: brought in from outside, used in the whole game
    global pot_inventory, itinerary, Parchment, pots

    # Dictionary with trivia quiz questions and answers (for knowledge fields)
    questions = {
    "The English language begins with the Anglo-Saxons. True or false?" : "true" ,
    "The sounds made by holding the lips together and then releasing the sound, such as p and b are called..." : "bilabial" ,
    "We can also use the upper teeth with the lower lip, for _________ sounds. This is how we make an f sound." : "labiodental" ,
    "What is the study of the meaning of languages?" : "semantics" ,
    "What is the study of language as it pertains to social classes, ethnic groups and genders?" : "sociolinguistics" ,
    "What is the smallest segment of sound, that comprises the basic building blocks of a language?" : "phoneme" ,
    "Any group of words which are taken to be less than a sentence, e.g. by lacking a finite verb, but which are regarded as forming a unit grammatically." : "phrase" ,
    "A term in grammar which denotes a class which does not have a pre-determined number of members." : "open" ,
    "An area within historical linguistics which is concerned with the origin and development of the form and meaning of words and the relationship of both these aspects to each other." : "etymology" ,
    "Which is the study of language with reference to human psychology?" : "psycholinguistics" ,
    "A type of structure where both subject and object have the same referent, e.g. He injured himself." : "reflexive"}
    # Sources: various trivia quizzes from all over the Internet

    lost = False # added by Oguz

    # FUNCTIONS
    def board():
        print ("""
    ______________________________________________________
    |     |     |     |     |     |     |     |     |     |
    |START|  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |
    |_____|_____|_____|_____|_____|_____|_____|_____|_____|
                                                    |     |
                                                    |  9  |
    _____________________________________           |_____|
    |     |     |     |     |     |     |           |     |
    |  22 |  23 |  24 |  25 |  26 | END |           |  10 |
    |_____|_____|_____|_____|_____|_____|           |_____|
    |     |                                         |     |
    |  21 |                                         |  11 |
    |_____|_________________________________________|_____|
    |     |     |     |     |     |     |     |     |     |
    |  20 |  19 |  18 |  17 |  16 |  15 |  14 |  13 |  12 |
    |_____|_____|_____|_____|_____|_____|_____|_____|_____|
    """)

    # Strength field scenarios

    def win():
        print ("You have defeated the evil monster! You may go along your way!")
    def lose():
        # When the player loses a STRENGTH round, 10 points are taken off of health
        hero.health -= 10
        print ("You have been defeated! Your health goes down by 10 points!")
        hero.status() 

    # Witches
    def witch_scenario():
        print ("An evil witch has come your way. Do you remember how to fight it?")
        fightchoice = input ("Type in the name of the weapon if you remember what is best against it - or type 'help' to look at your parchment!\t")
        fightchoice = fightchoice.lower()

        # If the player decides to look at the parchment:
        if "help" in fightchoice:
            print("\n\nHere, have a look at your parchment paper again for some help:")
            print("\n\t", Parchment)

            weaponchoice = input ("Now are you ready? Please type in the weapon of your choice.\t")
            weaponchoice = weaponchoice.lower()

            # Correct weapon
            if "gun" in weaponchoice:
                win()

            else:
                lose()

        # Corret weapon without help
        # The same pattern goes for all scenarios
        elif fightchoice == "gun":
            win()

        else:
            lose()

    # Ogres
    def ogre_scenario():
        print ("An evil ogre has come your way. Do you remember how to fight it?")
        fightchoice = input ("Type in the name of the weapon if you remember what is best against it - or type 'help' to look at your parchment!\t")
        fightchoice = fightchoice.lower()

        if "help" in fightchoice:
            print("\n\nHere, have a look at your parchment paper:")
            print("\n\t", Parchment)

            weaponchoice = input ("Now are you ready? Please type in the weapon of your choice.\t")
            weaponchoice = weaponchoice.lower()

            if "sword" in weaponchoice:
                win()

            else:
                lose()

        elif fightchoice == "sword":
            win()

        else:
            lose()

    # Dragons
    def dragon_scenario():
        print ("An evil dragon has come your way. Do you remember how to fight it?")
        fightchoice = input ("Type in the name of the weapon if you remember what is best against it - or type 'help' to look at your parchment!\t")
        fightchoice = fightchoice.lower()


        if "help" in fightchoice:
            print("\n\nHere, have a look at your parchment paper:")
            print("\n\t", Parchment)

            weaponchoice = input ("Now are you ready? Please type in the weapon of your choice.\t")
            weaponchoice = weaponchoice.lower()

            if "lance" in weaponchoice:
                win()

            else:
                lose()

        elif fightchoice == "lance":
            win()

        else:
            lose()

    # Trolls
    def troll_scenario():
        print ("An evil troll has come your way. Do you remember how to fight it?")
        fightchoice = input ("Type in the name of the weapon if you remember what is best against it - or type 'help' to look at your parchment!\t")
        fightchoice = fightchoice.lower()

        if "help" in fightchoice:
            print("\n\nHere, have a look at your parchment paper:")
            print("\n\t", Parchment)

            weaponchoice = input ("Now are you ready? Please type in the weapon of your choice.\t")
            weaponchoice = weaponchoice.lower()

            if "knife" in weaponchoice:
                win()

            else:
                lose()

        elif fightchoice == "knife":
            win()

        else:
            lose()
			
### KB: You could have made one function for all the scenarios because the fightchoice pattern is always the same, only with changing parameters for the different scenario options. 
			

    # FUNCTIONS - game plays for the different field types

    # KNOWLEDGE FIELDS: linguistics trivia quiz
    def KNOWLEDGE():
        global points
        print ("You have arrived at a KNOWLEDGE field. You must answer my question to proceed.")
        print ("Press enter to see the question.\n")
        input()

        # A random question appears from the dictionary
        question = random.choice(list(questions))
        print (question)

        # Correct answer: the value from the key of the given entry
        correct = (questions.get(question))

        input()

        print ("You have three guesses! Go!")

        guesses = 0

        for n in range(0,3): # 3 guesses maximum
            guesses += 1
            print ("\nTake your guess nr.", guesses, end=" ")
            guess = input("! ")
            guess = guess.lower()

            if guess == correct:
                points += 1 # 1 point for each correct answer
                print ("\nYes, you win! You have", points, "points now!")
                questions.pop(question) # question cannot be repeated
                break

            else:
                print ("\nNo, that's not it.")

        if guess != correct:
            print ("You did not manage to guess it. You still have", points, "points. Better luck next time.") # nothing happens; no points added

    # RISK FIELD: dice challenge
    def RISK():
        global points
        print ("You have arrived at a RISK field. You must have a duel with a monster if you want to go further.")
        print ("It is a simple dice game. The higher number wins.")
        input()

        print ("You can choose to ignore it or you can go into the fight.")
        print ("But here's the catch:")
        input()

        print ("If you win, you get a health potion. You're gonna need it later.")
        print ("But if you lose, you also lose one point, which is going to make it harder to get the phials for the next game!")

        challenge = None

        while challenge != "0":
            # ask the user to accept or ignore the dice challenge
            challenge = input("\nDo you accept the challenge? Please type Yes or No.\n")
            challenge = challenge.lower()

            if challenge == "yes":
                print ("\nYou have accepted the challenge. Please press enter to roll the die.")
                input()
                # one random number for the player and one for the opponent
                dice_player = random.randint(1, 6)
                dice_monster = random.randint(1, 6)

                # winning situation
                if dice_player > dice_monster:
                    print ("You win with", dice_player, "against", dice_monster, "!")
                    print ("Here's a health potion as your prize.")
                    pot_inventory.append("potion")
                    pots = len(pot_inventory)		
                    print ("You now have", len(pot_inventory), "health potions in your bag.")
                    break

                # losing situation
                elif dice_player < dice_monster:
                    print ("You lose with", dice_player, "against", dice_monster, "!")

                    points -= 1
                    if points < 0:
                        points = 0 # no negative allowed

                    print ("You lost one point, and now you have", points, "points.")
                    break

                # tie: they can choose to go again
                elif dice_player == dice_monster:
                    print ("It's a tie. You can decide whether you want to roll again.")
                    input()

            # challenge not accepted
            elif challenge == "no":
                print ("You have chosen not to fight me. Please proceed on the board.")
                break

            # input is not "Yes" or "No"
            else:
                print ("\n", challenge, "is not a valid choice. Please indicate whether you accept the challenge by typing Yes or No.")

    # STRENGTH FIELD
    def STRENGTH():
        global points
        chosen_monster = random.choice(monsters) # monster randomly chosen
        print ("You have arrived at a STRENGTH field.")

        if chosen_monster == "witch":
            witch_scenario()

        elif chosen_monster == "ogre":
            ogre_scenario()

        elif chosen_monster == "dragon":
            dragon_scenario()

        elif chosen_monster == "troll":
            troll_scenario()

    # TYPES OF FIELDS OF THE BOARD
    knowledge_field = [1, 4, 6, 7, 8, 13, 14, 16, 19, 20, 22]
    strength_field = [2, 5, 10, 11, 17, 23, 26]
    risk_field = [3, 9, 12, 15, 18, 21, 24, 25]

    # INTRODUCTION
    print ("Welcome to the maze of the sphynx!")
    input()
    print ("Our hero finds herself on a path. It seems strange, because it has all these numbers all over it. She then realises it is a giant game board. She is confused as to what to do.\n")

    input ("Press enter in order to see the field from above.")

    board()

    input()

    print ("At the end of the maze, a giant sphynx awaits. She says:")
    input()
    print ("Welcome, stranger.\n\nYou have entered my maze, and you need to prove yourself in three kinds of tasks.")
    input()

    # Game description
    print ("There are some fields where you can prove your linguistic knowledge. Each answer is worth one point, and you have to collect at least 3 points if you want to win this game.\n")
    input()
    print ("There are also fields where you can play a game of risk: you have a die, and your enemy has a die. The higher number wins. Simple. If you win, you get health potions. But if you lose, you lose points that you have collected on knowledge fields. The choice whether you risk this is yours.\n")
    input()
    print ("And finally, on some fields you have to prove that you're worthy of being called a hero. You're gonna go into battle with a magical creature. You either remember what I say to you now or you lose precious health points.")
    input()
    print ("Here it goes: first of all, let me give you four weapons: a magic sword, a knife, a lance, and a gun. Each one is effective against one type of monster.")

    # Gifts from the sphynx: the weapons
    if "knife" and "lance" and "gun" and "sword" not in hero.inventory:
        hero.inventory = hero.inventory + sphynx_gifts

    else:
        hero.inventory # if the player fails the game one time, inventory is not doubled the next time

    hero.show_inventory() 

    input ()
    print ("The sword is going to help you against the ogres, the lance will be best against dragons. It is best to use the knife against trolls. And finally, the gun will be the most useful when you encounter a witch.\n")
    input()
    print ("Do you want to take a note?")

    # Add this info to parchment
    parchment()
    print(Parchment, "has been added to the parchment.")

    print ("Good luck, brave hero! Let the game begin!")
	
#### DELETE 
    hero.status() 

    # GAME STARTS
    while field < 27 and hero.health > 0:
        round += 1
        steps_taken = random.randint(1,4) # 1 to 4 steps randomly
        field += int(steps_taken)
        if field > 27:
            field = 27 # the final field is nr. 27
        else:
            field = field 
### KB: It doesn't hurt, but in theory you don't need else-statements like this one. 

	
        print ("\n\n********* ROUND", round, "*********")
        input()

        print ("You took", steps_taken, "steps, which brings you to field nr.", field, ".\n")
        print ("The sphynx says: ")

        if field in knowledge_field:
            KNOWLEDGE()

        elif field in strength_field:
            STRENGTH()
            if hero.health < 1:
                points = 0 # once the player loses, they lose all points as well
                lost == True # added by Oguz

            else:
                input()

        elif field  in risk_field:
            RISK()

    if lost == False: # addded by Oguz to fix my while loop (Zsofia)

        print ("This is the end of the game. Let's see the results:")
        input()

        # at least 3 points: they get the phials
        if points > 2:
            print ("First of all, let me give you the phials to use in your next challenge.")
            print ("Here's a red, a yellow and a blue one.")

            itinerary.extend(["red", "yellow", "blue"])
            print ("Your new itinerary is:")
            input()
            print (itinerary)

            points -= 3 # calculate the remaining points

            # For each point you get one more health potion, too
            if points > 0:
                print ("But you know what? Since you collected more than just 3 points, you also get some extra health potions to use later!")
                for i in range(points):
                    pot_inventory.append("potion")
                    pots = len(pot_inventory)
                print ("You now have", pots, "health potions altogether in your bag.")
                input()

            # If you only had 3 points, that's it, no extra health potions
            else:
                print ("Unfortunately you only collected three points, which means I have nothing else for you!")
                print ("But during the risk games, you were able to collect", len(pot_inventory), "health potions, so those are yours, too!")
                input()
                pots = len(pot_inventory)

        # If the user did not collect 3 points, they get questions in order to acquire the phials at the end
        else:
            if hero.health < 1:
                print ("You've lost all your health points. You were defeated by the enemy.")
                print("You wake up with the Sphynx looking over you.")
            else:

                while points < 3:
                    print ("You did not collect enough points for me to give you the phials needed for the next game. There are", 3-points, "points missing.\n")
                    print ("Here's your chance to collect those missing points:")
                    input()

                    KNOWLEDGE()

                print ("Let me give you the phials to use in your next challenge.")
                print ("Here's a red, a yellow and a blue one.")

                itinerary.extend(["red", "yellow", "blue"])
                print ("Your new itinerary is:")
                input()
                print (itinerary)

                # They still get the health potions from the dice games:
                print ("During the risk games, you were able to collect", len(pot_inventory), "health potions, so those are yours, too!")
                input()
                pots = len(pot_inventory)

    # If the player loses, everything is back to 0
    field = 0
    round = 0
	
	### KB: Health restored by half 
    hero.health += 50

    ######### END OF ZSOFIA LELNER'S SECTION #########

##########################################################

def Mini_game2():
       ###########  Oguzhan Kuyrukcu
    global pots, pot_inventory
	
    #STRUCTURE
        #THE HERO FOUND SOME ELIXIRS IN THE MINIGAMES (color-dependent. I am thinking just red, blue and yellow now but we can expand this "puzzle" later.)
        #HE USES THESE TO SATISFY THE DRAGONS AND IN THE END HE GETS THE SECRET PHRASE TO GET OUR (ALONG WITH THE IMPERATIVE FORM) TO GET OUT OF THE CAVE.

    #health = 100 #the dragons might attack the hero, even tho this won't be a combat quest.
    #also, this quest's health is regenerated everytime the hero goes back to the main cave. so if he has no potions he can just go back to the main cave and rest and come back #commented out because we use global health
    #Parchment="" #to make sure my code doesn't clash with Poppie's, will comment out once we merge them.


    def roll_dmg(): #when the dragons aggressively attack the hero, this will take place
        roll = random.randint(1,20) #not 0,20 because we don't want divison by zero, obviously
        damage = 60//roll + 20  #this means that the dragon attack could almost kill you, or you can almost mostly dodge the damage, but there'll always be a serious enough scar that you can't take this damage without drinking a potion more than a few times.
        print("... and burns you for", damage, "health points.\n")
        hero.health -= damage
        hero.status() 

    def roll_dmg_2():#when the dragons attack the hero as a side-effect of their actions, this will take place
        roll = random.randint(1,20) #not 0,20 because we don't want divison by zero, obviously
        damage = 20//roll #this means that the dragon attack does minimal damage at worst, and is unimportant with almost every roll
        print("You take", damage, "points of damage.\n")
        hero.health -= damage
        hero.status() 

    def potion(): #the hero can drink potions each time he takes damage
        global pots #brings something out of the function inside it
        if pots > 0:
            print("\nYou have", pots, "potions to heal your wounds.\n")
            potchoice = True
            while potchoice == True: #for loop incase of invalid input
                pot = input("""Do you drink a potion?
                1 - Yes
                2 - No
                """)
                if pot == "1":
                    hero.health += 50
                    if hero.health > 100:
                        hero.health = 100 #so health never goes above 100

                    print("\nYou drink a potion. It restores your health to", hero.health, "\n")
                    pots -= 1
                    print("\nYou have", pots, "potions left. \n")
                    potchoice = False

                elif pot == "2":
                    print("\nYou continue without drinking a potion. \n")
                    potchoice = False

                else:
                    print("\nThat's not a valid input. Please press 1 or 2.")

        else:
            print("You have no potions left. You must be careful about the damage you take.\n")

    def death(): #if the hero dies this takes effect
        print("You can no longer endure your suffering. Your consciousness fades, and everything darkens.\n")
        print("After a time that could be just hours or weeks, you open your eyes again.")
        hero.health += 50 ### KB: restoration by half


    print("With the colorful phials (red, blue, yellow) you have found at the other ends of the cave, you enter the larger one.\n")
    #which means this quest can't begin without them, so the hero has to do the other quest first.

    print("You enter a dark room and hear faint echoes of beastly sounds. As you walk deeper into the room, the sounds become more and more like words, but they remain beastly.\n")

    toplayornot = 0 #to enable the loop if the input is invalid

    while toplayornot == 0:

        choice = input("""Do you follow the voices, or go back like a wimp?

        1 - Follow the voices
        2 - Who are you calling a wimp!

        """) #the hero can go back to main hall and wait, or go to the other room (maybe?)

        if choice == "2":
            ##to be edited in accordance with the rest of the game
            toplayornot = 1
            print("That's the spirit!")
            print("\nYou walk to the end of the cave, where you see three shadows. They seem to be talking to each other in a tongue you don't understand, and in between their utterances the room is lit with fire, which seems to be coming from their mouths.\n")

        elif choice == "1":
            print("\nYou walk to the end of the cave, where you see three shadows. They seem to be talking to each other in a tongue you don't understand, and in between their utterances the room is lit with fire, which seems to be coming from their mouths.\n")
            toplayornot = 1

        else:
            print("That's not a valid choice. Press 1 or 2.")
            toplayornot == 0


    print("The creatures notice you and stop talking. As you approach, you notice that they resemble tiny dragons. One of them has white skin, one purple, and one green. You see now that they are chained, on their wings and their necks.\n")

    print("The dragons seem quite excited for some reason. They beckon you closer with their claws and they keep saying \"Jadati jinne!\". You are certain this isn't the dragon tongue, because you know it a little yourself. They must be speaking the local language, Dothraki. Perhaps it's the same language as the inscription?\n") #dragon tongue was vallyrian or something in GOT. we can revise it later #jadati is come: (jadat) + i (imperative), jinne is "here"

    whitedrag = False
    greendrag = False
    purpledrag = False
    #"dragon-satisfaction-value" once the dragons are satisfied, these values will change and the game will go on

    optdragons = {
    "1" : "Leave the dragon cave.",

    "2" : "Approach the green dragon.",

    "3" : "Approach the purple dragon.",

    "4" : "Approach the white dragon."
    } #instead of giving these as the input, we shall modify the list, so that if a dragon is once satisfied, he won't be approached again. #I'm using a dictionary because as a list deleting the option in the middle is problematic, since referring them by number isn't as sure as referring to them by their "tag".

    while whitedrag != True or greendrag != True or purpledrag != True: #when all of the dragons have been "satisfied", the game moves on.
        print("\nWhat do you do?\n")
        choice = input(optdragons) #input doesn't accept 2 arguments, apparently

        optactions = [
        " 1 - Attack the dragon. "
        " 2 - Throw food at the dragon. "
        " 3 - Show the dragon the phials. "
        " 4 - Step back from the dragon. "
        ] #this looks ugly in the console. How to make it appear better?

        interaction = True #to determine if the interaction with the selected dragon will go on or not.

        if choice == "1":
            print("You return to the main hall.") ##to be edited in accordance with the rest of the game #poppie will do this
            whitedrag = True
            greendrag = True
            purpledrag = True
            #the hero just might not want to play the quest at that point, or he actually has finished the quest already and thought it'd be different, (but it isn't, so he can go back.) however, if he wants, he can play the game as many times, since the dragons would always want to interact with the hero after they "sober up", because of the phials.
            #instead of return_main() function we just break the loop so we go back to the main selection menu

        else:
            if choice == "4":
                print("\nYou approach the white dragon.\n")
                print("As you move closer, you realize that the dragon is not looking at you, but the phials you are carrying.\n")
                print("The dragon shouts in the foreign tongue: \"Attihi anna haz shishei!\"\n") #my idea is to use dothraki so that the hero has to think what he has to do. I'm trying to translate them as best as possible but I can't find some words. For example, this phrase is supposed to be "Show me those phials" but I can't find any word similar to a phial, so I just used a made up word for this (borrowed from Turkish, infact)

                while interaction == True:

                    print("What do you do?")
                    choice = input(optactions)

                    if choice == "1":
                        print("\nYou attack the dragon, but your weapon can't even scratch the dragon scales. Annoyed and angry, the dragon breathes fire onto you..\n") #dragon attacks back, hurts the hero seriously.
                        roll_dmg()
                        print("Wounded, you retreat.\n")
                        potion()
                        break #go back to dragon choice

                    elif choice == "2":
                        print("The dragon doesn't seem interested in the food at all, and repeats, with a little dragonfire this time, \"Attihi anna haz shishei!\" \n")
                        roll_dmg_2()
                        potion()
                        #in which he hurts the hero slightly with fire-breath #the interaction goes on

                    elif choice == "3":
                        print("\nAs you take the phials out, the dragon almost starts smiling. He points at the phials, and then to the lamb carcass in front of him, while saying: \"Fitchi rek rakhaan.\" ") ##"bring them to the lamb", I hope. #This is the line that'll satisfy the dragon

                        loopwhite = True #invalid selection
                        while loopwhite == 1:
                            actionwhite = input("""What do you do?

                            1 - Throw a phial to the dragon
                            2 - Go near the lamb.

                            """)

                            if actionwhite == "1":
                                print("The phial hits the dragon, and rolls back to you. Luckily it's not broken, because the dragon looked quite angry and anxious after your action. He repeats, a little upset this time: \"Fitchas rek rakh.. \" \n ") #bring them to the lamb, I hope
                                roll_dmg_2() #minor damage, the dragon doesn't want to hurt us
                                potion()

                            elif actionwhite == "2":
                                print("As you go near the lamb, the dragon smacks his lips. He can barely contain his excitement. He keeps pointing at the phials and then to the lamb.\n")

                                loopwhite = False #to get out of the first question
                                blue = False #once each correct phial for each dragon is used, they'll turn True, and that'll be the satisfaction of the dragon.
                                yellow = False
                                red = False

                                while yellow != True or blue != True or red != True:

                                    actionwhite2 = input(""" What do you do?

                                    1 - Mix some of the yellow elixir with the lamb meat.
                                    2 - Mix some of the blue elixir with the lamb meat.
                                    3 - Mix some of the red elixir with the lamb meat.

                                    """
                                    )

                                    if actionwhite2 == "1":

                                        if yellow == False:
                                            print("The yellow liquid drips onto the meat, and it starts taking a yellow-ish color. The dragon looks happy, and points at the other phials, and again to the lamb.")
                                            yellow = True

                                        elif yellow == True: #the idea is the player, if careless, might think the dragon wants the same elixir. So this time I am not deleting the options even after they are satisfied, putting the hero at some (minor) risk
                                            print("The dragon sighs, burning you a little, and points at the other phials.")
                                            roll_dmg_2()
                                            potion()

                                    elif actionwhite2 == "2":

                                        if blue == False:
                                            print("The blue liquid drips onto the meat, and it starts taking a skylike color. The dragon looks happy, and points at the other phials, and again to the lamb.")
                                            blue = True

                                        elif blue == True:
                                            print("The dragon sighs, burning you a little, and points at the other phials.")
                                            roll_dmg_2()
                                            potion()

                                    elif actionwhite2 == "3":

                                        if red == False:
                                            print("The red liquid drips onto the meat, and it starts taking a bloody color. The dragon looks happy, and points at the other phials, and again to the lamb.")
                                            red = True

                                        elif red == True:
                                            print("The dragon sighs, burning you a little, and points at the other phials.")
                                            roll_dmg_2()
                                            potion()

                                    else:
                                        print("That's not a valid choice. Please try again.")

                            else:
                                print("That's not a valid choice. Please try again.")

                        if blue == True and yellow == True and red == True:
                            print("Once every elixir is mixed with the lamb, magically it assumes a bright white color. The dragon rushes in to eat it, and no longer looks interested in you. He seems happy. Perhaps you should now see what the other dragons want.")
                            whitedrag = True #satisfied
                            del optdragons["4"] #removes the option to approach this dragon again #this will be under this choice only.
                            break   #once he is satisfied, the interaction is over

                    elif choice == "4":
                        print("\# NOTE: You are facing all the dragons once again.\n")
                        #here, the hero can approach another dragons
                        break #go back to dragon choice

            elif choice == "2":
                    print("\nYou approach the green dragon.\n")
                    print("As you move closer, you realize that the dragon is not looking at you, but the phials you are carrying.\n")
                    print("The dragon shouts, in the foreign tongue: \"Attihi anna haz shishei!\"")

                    while interaction == True:

                        print("What do you do?")
                        choice = input(optactions)

                        if choice == "1":
                            print("You attack the dragon, but your weapon can't even scratch the dragon scales. Annoyed and angry, the dragon breathes fire onto you..") #dragon attacks back, hurts the hero seriouslyself.
                            roll_dmg()
                            print("Wounded, you retreat.\n")
                            potion()
                            break #go back to dragon choice

                        elif choice == "2":
                            print("The dragon doesn't seem interested in the food at all, and repeats, with a little dragonfire this time, \"Attihi anna haz shishei!\" \n")
                            roll_dmg_2()
                            potion()

                            #in which he hurts the hero slightly with fire-breath #the interaction goes on

                        elif choice == "3":
                                print("As you show the phials, the dragon's excitement becomes more and more visible. He beckons you closer.\n")
                                print("When you get closer, the dragon lifts one of his wings up, and shows a scar. He points at the phials, and then to his scar with his chin, saying \"Kolas ma shishe..\"") #"heal with the elixir"

                                blue = False #once each correct phial for each dragon is used, they'll turn True, and that'll be the satisfaction of the dragon.
                                yellow = False
                                red = False

                                while yellow != True or blue != True: #meaning, this dragon only wants blue and yellow elixirs.

                                    actiongreen = input("""What do you do?

                                    1 - Use the yellow elixir as an ointment on his scar.
                                    2 - Use the blue elixir as an ointment on his scar.
                                    3 - Use the red elixir as an ointment on his scar.

                                    """
                                    )

                                    if actiongreen == "1":

                                        if yellow == False:
                                            print("As you apply the yellow elixir on the scar, the tissue turns yellow-ish. The dragon looks relieved.")
                                            yellow = True

                                        elif yellow == True: #the idea is the player, if careless, might think the dragon wants to same elixir. So this time I am not deleting the options even after the are satisfied, putting the hero at some (minor) risk
                                            print("The dragon sighs, burning you a little, and points at the other phials.")
                                            roll_dmg_2()
                                            potion()

                                    elif actiongreen == "2":

                                        if blue == False:
                                            print("As you apply the blue elixir on the scar, the tissue turns blue-ish. The dragon looks relieved.")
                                            blue = True

                                        elif blue == True:
                                            print("The dragon sighs, burning you a little, and points at the other phials.")
                                            roll_dmg_2()
                                            potion()

                                    elif actiongreen == "3":

                                        print("As you touch the dragon's scar with the red elixir, the dragon screams and jumps in agony.. ")
                                        roll_dmg()
                                        potion()

                                    else:
                                        print("That's not a valid choice. Please try again.")

                                if blue == True and yellow == True:
                                    print("When the blue and yellow elixirs mix on the scar, they turn green. Within seconds, this green liquid heals the scar, and where the scar was grows a green scale in a minute. The dragon looks happy, but drowsy. It looks like he no longer needs your help.\n")
                                    greendrag = True #satisfied
                                    del optdragons["2"] #removes the option to approach this dragon again #this will be under this choice only.
                                    break                  #once he is satisfied, the interaction is over

                        elif choice == "4":
                            print("You are facing all the dragons once again.")
                            #here, the hero can approach another dragons
                            break #go back to dragon choice

            elif choice == "3":
                    print("\nYou approach the purple dragon.\n")
                    print("As you move closer, you realize that the dragon is not looking at you, but the phials you are carrying.\n")
                    print("The dragon shouts, in the foreign tongue: \"Attihi anna haz shishei!\"")

                    while interaction == True:

                        print("What do you do?")
                        choice = input(optactions)

                        if choice == "1":
                            print("You attack the dragon, but your weapon can't even scratch the dragon scales. Annoyed and angry, the dragon breathes fire onto you..\n") #dragon attacks back, hurts the hero seriously
                            roll_dmg()
                            print("Wounded, you retreat.\n")
                            potion()
                            break #go back to dragon choice

                        elif choice == "2":
                            print("The dragon doesn't seem interested in the food at all, and repeats, with a little dragonfire this time, \"Attihi anna haz shishei!\" \n")
                            roll_dmg_2()
                            potion()

                        elif choice == "3":
                                print("As you show the phials, the dragon starts smiling excitedly. He calls you near him.")
                                print("When you are in front of him, the dragon points at the phials, then his mouth. He says: \"Iddelas anna!\", and opens his mouth.") #"make me drink"

                                blue = False #once each correct phial for each dragon is used, they'll turn True, and that'll be the satisfaction of the dragon.
                                yellow = False
                                red = False

                                while red != True or blue != True: #meaning, this dragon only wants blue and yellow elixirs.

                                    actionpurple = input("""What do you do?

                                    1 - Open the yellow phial and drip some into his mouth.
                                    2 - Open the blue phial and drip some into his mouth.
                                    3 - Open the red phial and drip some into his mouth.

                                    """
                                    )

                                    if actionpurple == "1":
                                        print("When the yellow elixir touches the dragon's mouth, his face turns evermore purple with disgust. He screams \"Tokikof!\"..")
                                        roll_dmg()
                                        potion()

                                    elif actionpurple == "2":

                                        if blue == False:
                                            print("When the blue liquid reaches his mouth, the dragon starts laughing uncontrollably. You notice that one of his eyes turn blue as he is laughing.")
                                            blue = True

                                        elif blue == True:
                                            print("The dragon sighs, burning you a little, and points at the other phials.")
                                            roll_dmg_2()
                                            potion()

                                    elif actionpurple == "3":

                                        if red == False:
                                            print("When the red liquid reaches his mouth, the dragon starts laughing uncontrollably. You notice that one of his eyes turn red as he is laughing.")
                                            red = True

                                        elif red == True: #the idea is the player, if careless, might think the dragon wants to same elixir. So this time I am not deleting the options even after the are satisfied, putting the hero at some (minor) risk
                                            print("The dragon sighs, burning you a little, and points at the other phials.")
                                            roll_dmg_2()
                                            potion()

                                    else:
                                        print("That's not a valid choice. Please try again.")

                                if blue == True and red == True:
                                    print("After he drinks both the red and blue elixirs, the dragon looks euphoric. You notice that both of his eyes turn purple now. He is no longer interested in you. Indeed, it is as if you don't exist in his reality now. It's time to leave him alone. \n")
                                    purpledrag = True #satisfied
                                    del optdragons["3"] #removes the option to approach this dragon again #this will be under this choice only.
                                    break                  #once he is satisfied, the interaction is over

                        elif choice == "4":
                            print("You are facing all the dragons once again.")
                            #here, the hero can approach another dragons
                            break #go back to dragon choice

            else:
                    print("That's not a valid choice. Try again.")

            if hero.health < 1: #how can we make it so that this applies at any point? it works like a turn-based game like this, and actually works 1 turn late. do we just repeat it with every dragon? we should have potions too, so this should be more dynamic.
                death()
                #return_to_cave() #instead of return_main() function we just break the loop so we go back to the main selection menu
                whitedrag = True
                greendrag = True
                purpledrag = True

            else:

                if whitedrag == True and greendrag == True and purpledrag == True:

                    print("\nAll of the dragons seem.. drunk, or otherwise drowsy. And talkative. They keep blabbering something in that foreign tongue.. but then you realize they also blabber in Valyrian. It is as if they are arguing about something.")
                    input()

                    print("\nAfter a few minutes of drunk dragon debating, the white one lifts his head up and says in Valyrian: \"You have us made hap-happy. We will give you the right to make use of our wise.. ness, but only if you ask the right ques.. tschn. Axe care.. fully.\" \n ")

                    q = 0 #for the loop, incase of "wrong question"
                    def answer(): #just to have it easier with the multiple "right questions"
                        print("""
                        The dragons start talking to each other in that foreign tongue. After half a minute,
                        the Green Dragon says: "So, you want to leave the cave? Al-alright..
                        First, you need to know the Oooogre's name: He is called.. What was it again? Mud something.."
                        Purple Dragon: "Muddy."
                        Green Dragon: "Right, right. So you call his name.."
                        Purple Dragon: "T-t-three times."
                        White Dragon: "And then you have to command him to let's.. let you out in Dothraki.
                        You say.. uh.. "azh", which means "to let", "anna", which means "me", and uh.. "esem.. -esemrasalat", which means "leave"."
                        Purple Dragon: "He needs the request suffix /-as/, though, so he needs to say "azhas"."
                        Green Dragon: "No. the ogre wants the formal command. He has to use the formal imperative. For that he needs to attach /-i/ to the verb, since azh ends with a consonant."
                        """) #here the hero can figure out the imperative form. I'm not sure if I should include the other forms (negative, encouragents etc.) since they are not necessary in context of this story
                        print("\nThe dragons go on debating for a while to decide on the correct form of the secret phrase.")
                        print("\nFinally they return to you.")
                        print("""\nThe white dragon takes word and says: "The secret phrase is this: Muddy, azhi anna esemrasalat."
                        \nThe purple dragon interrupts and says: "That means "Muddy, let me out", incase you couldn't figure it out.
                        """)


                    while q == 0:
                        question = input("What do you ask? ")

                        if "secret" in question.lower(): #so, the player will type in the question, not choose among options this time. the idea is that any question related to the ogre's puzzle or anything that asks how to get out/leave will trigger a proper response from the dragons. problem: only one string works. if i write "code" or "secret" it takes every answer as valid
                            answer()
                            q = 1

                        elif "enchanted" in question.lower():
                            answer()
                            q = 1

                        elif "magic" in question.lower():
                            answer()
                            q = 1

                        elif "code" in question.lower():
                            answer()
                            q = 1

                        elif "leave" in question.lower():
                            answer()
                            q = 1

                        elif "get out" in question.lower():
                            answer()
                            q = 1

                        else:
                            print("The dragons mumble something, as if they did not hear what you said. Or they simply ignore you.") #so the player can ask questions again and again until he asks the "right question"

                    print("Now that you know the secret phrase, you can note it down in your parchment paper.")
                    note = True
                    while note == True:
                        parch = input("""
                        Do you want to take a note?
                        1 - Yes.
                        2 - No.
                        """)
                        if parch == "1":
                            parchment() #dictionary notepad
                            print(Parchment)
                            note = False
                        elif parch == "2":
                            print("You continue without taking a note.")
                            note = False
                        else:
                            print("That's not a valid input. Please press 1 or 2.")

    ################ END OF Oguzhan Kuyrukcu section






##########################################################
###### POPPIE DRYER'S SECTION: CENTRAL PROGRAM ###########

#Tasks: Creating the central progam, functions for the game, putting the mini games into the central program, writing the story line of the game


#Functions

#Write into parchment: global means it refers to something outside of function, the parchment acts as a note book for the character
def parchment():
    print("Write into the parchment:\t")
    write=input("")
    global Parchment
    Parchment.append(write)
    return Parchment
#I chose to use a list as it ordered the writing better

#Return to main cave function it brings you different options (Poppie Dryer)
#Options for game op1, op2, op3, op4

#op 1: it plays the mini games,
def op1():
    repeat=1
    global GAME, itinerary, pot_inventory
	
    print("\n\tOur hero walks further into the cave. It is much darker, and there are many terrifying sounds echoing around.")
    print("\n\tAfter walking for a long time, the cave path splits in two directions: Left and Right....\n in order to preceed, the hero must choose a path.")
    while repeat==1:
        if repeat==1:
            path=input("\n\tShould the Hero walk left or right?:\t").upper()
        if path=="LEFT":
            repeat=0
            print("\n\n**********************************************************")
            if "red" and "blue" and "yellow"  in itinerary:
                print ("You've already been there! Go right next time!") # added by Zsofia - the first mini game should not be played again if the hero has the phials
                input()
            else:
                Mini_game1 ()
        elif path=="RIGHT":
            repeat=0
            print("\n\n**********************************************************")
            if "red" and "blue" and "yellow"  in itinerary:
                Mini_game2()
            else:
                print('IT IS NOT SAFE TO ENTER THIS PART OF THE CAVE UNTIL YOU HAVE THE NECESSARY REQUIREMENTS!!! GO BACK!!!!!') #mini game 2 cannot be played unless you have played mini  game 1
                input()
        else:
            repeat=1

#op 2 repeat statement
def op2():
    print("Muddy: '\nNo problem; I can repeat the information:"
          "\n\nThe cave is protected by a magical force. There are two things you need to do in order to leave the cave:"
            "\n\tSay my name three times!\n\tSpeak the enchanted words."
            "\n\nONLY THEN! will the boulder be lifted, and will you be able to leave the cave freely!\n\t\t\t********"
           "\nI recommend that you venture deeper into the cave to search for any language clues.\nUse your parchment paper at given moments in order to record any information.")
    input()
#op 3 print statement
def op3 ():
    print("Muddy: 'You want a bit of help, ok... hmmm... I can only think of one thing"
          ":\n\tWell, in order to partake in the 'right' cave challenge, you need to have received soemthing in your itinerary from the 'left' cave challenge."
          "\n\tWithout this, you cannot carry on.\tI hope that helps?'")
    input()
#op 4 is the ending which allows you to finish the game
def op4():
    global GAME
    i=1
    while i==1:
        print("Muddy: So you are finally ready to leave the cave...?")
        print("\nHave another look at your parchment paper in case you need to remember anything:\n\n\t", Parchment)
        input("")
        print("\nOk, so now you're ready, let's begin!")
        print("\nFirst, you must call my name a given number of times...")
        name=input("What is the Ogre's name?\t").capitalize()
        if name=="Muddy":
            print("Correct!")
            break
        else:
            print("\nWRONG!!! That's not my name at all!\n")
            j=1
            while j==1:
                name_back=input("Would you like to:\nA: answer the question again or B: go back to the main cave?\t").upper()
                if name_back=="A":
                    j=0
                    continue
                elif name_back=="B":
                    j=0
                    i=0
                else:
                    continue

    while i==1:
        num=input("How many times does it need to be called?\t")
        if num=="3":
            print("'Muddy' "*3)
            break

        elif num == "three":
            print("'Muddy' "*3)
            break

        else:
            if num.isdigit():
                num = int(num)
                print("'Muddy' " *num)
                print("Incorrect, you're never going to leave the cave at this rate. Try again")
                j=1
                while j==1:
                    name_back=input("Would you like to:\nA: answer the question again or B: go back to the main cave?\t").upper()
                    if name_back=="A":
                        j=0
                        continue
                    elif name_back=="B":
                        j=0
                        i=0
                    else:
                        continue

            else:
                print("That's not even a number! Try again.")
                j=1
                while j==1:
                    name_back=input("Would you like to:\nA: answer the question again or B: go back to the main cave?\t").upper()
                    if name_back=="A":
                        j=0
                        continue
                    elif name_back=="B":
                        j=0
                        i=0
                    else:
                        continue


    while i==1:
        print("\nAnd finally: you must ask to leave the cave in the new secret language:\t")
        print("\n\nHere, have a look at your parchment paper again for some help:")
        print("\n\t", Parchment)
        final_answer=input("\nWhat are the magic words?\t")
        if "azhi anna esemrasalat"  in final_answer.lower():
            print("\n\n***********************************************************************")
            print("\nThe cave wall starts to creak and groan. All of a sudden sparkling light appears everywhere, muddy vanishes, and the walls of the cave open ")
            print("up to reveal the outside world...")
            print("\n\n\t\tOur hero escapes and runs into the outisde world! She is free!")
            GAME="E"
            i=0

        else:
            print("That's not the right answer; try again or you'll never escape!")
            j=1
            while j==1:
                name_back=input("Would you like to:\nA: answer the question again or B: go back to the main cave?\t").upper()
                if name_back=="A":
                    j=0
                    continue
                elif name_back=="B":
                    j=0
                    i=0
                else:
                    continue




#Introduction telling the story and introduction of parchment paper/notebook: (Poppie Dryer)
input("\nOur beloved Adventurer/Hero has been doing well on her quest so far!\n")
print("\nAfter a couple of hours she finds herself wandering around a deep dark forest!!!"
      "\nIt is so dark and dense that she can't see where she's going...")
input("")
print("Oh wait, WHAT IS THAT NOISE???!")
print("\n\t\t*CRASH* *BANG* *ROOOOOAAAAARRRR*")
input("")
print("Our Hero finds herself trapped inside a..... deep DARK CAVE!"
      "\nThe walls are made of thick rock, far too deep to dig through, and the door of the cave has been blocked off by a massive boulder."
      "\nJust when you think all hope is lost, at that moment you hear a loud booming voice...")
input("")
print("\n\t'ROOOOAAARRRR!!! I have trapped you!!!!\n\nMy name is Muddy, and I am an ogre who guards this magical cave!!'")
print("\nThe cave is protected by a magical force. There are two things you need to do in order to leave the cave:"
            "\n\n\t1: Say my name three times!\n\t2: Ask to get out the cave using the enchanted words."
            "\n\nONLY THEN! will the boulder be lifted and will you be able to leave the cave freely!")
input("")
GAME="Z"
while GAME=="Z":
    print("\nChoose a reply to the ogre:\n\tEnter A: I really want to leave this cave, what should I do?"
          "\n\tEnter B: Please Muddy, is there anything you can do to help me with this?"
          "\n\tEnter C: What should my next step be in order to learn the enchanted words?")
    reply=input("\nEnter your reply:\t").capitalize()

    if reply=="A":
        print("\n\tHero: 'I really want to leave this cave!'")
        break
    elif reply=="B":
        print("\n\tHero: 'Please Muddy, is there anything you can do to help me with this?'")
        break
    elif reply=="C":
        print("\n\tHero: 'What should my next step be in order to learn the enchanted words?'")
        break
    else:
        GAME=="Z"
print("\nOgre: 'OK, I suppose if you reeeeaaallllly want to leave the cave that desperately..., then there may be a bit of advice I can give you."
      "\n\tBut BE PREPARED, it won't be easy!")
input()
print("\tIf you are brave enough, I recommend that you venture deeper into the cave to search for any language clues."
      "\n\tBut you've got to be careful and have your wits about you! The deep cave is a lot darker and scarier than the main cave.\n\n")
input("")
print("\n\tOh, and before I forget, take this parchment paper with you:")

print("""                                                           ________________
                                                           /              /
                                                           /              /
                                                           /              /
                                                           /              /
                                                           /              /
                                                           /              /
                                                           /              /
                                                           /______________/  """)

print("\nIf you find any information, it will be helpful to write it down here, so you don't forget!")
print("\n\nWhy don't you have a practice now? You should write some infomation about how to escape the cave.\nMaybe write down my name so you don't forget it? (You'll need it later!)")
parchment() #practice for user to use the parchment
print(Parchment, "has been added to the parchment.")
print("\nOK, off you go!")
input()
print("\n\n************************************************************************")
print("\n************************************************************************")

#This brings the game forward to the two mini games and eventually the ending(Poppie Dryer)
GAME="A"
while GAME=="A":
    print("\n\n\t* walk * walk * walk *\n\t(You have returned to the main cave)")
    print("\n\nMuddy the Ogre: 'Welcome to the main cave, I hope your experiences in the deep cave don't scare you too much.")
    print("\n\t\t'I'm sure you're here for 4 reasons:\n\n\t\tEnter 1: You want to try again and proceed back into the deep cave.\n\t\tEnter 2: You want Muddy to repeat his information."
          "\n\t\tEnter 3: You want a bit of help.\n\t\tEnter 4: YOU HAVE FOUND THE ENCHANTED WORDS, AND YOU ARE READY TO LEAVE THE CAVE!!!'")
    MC_choice=input("\nEnter your choice:\t")
    if MC_choice=="1":
        op1()

    elif MC_choice=="2":
        op2()

    elif MC_choice=="3":
        op3()

    elif MC_choice=="4":
        op4()
    else:
        print("\nInvalid answer, please try again.")

print("\nThe hero has completed this part of her quest.")
print("\nThe imperative rule has been added to your scripts.") 

hero.scripts_append("Imperative suffix: /-i/") 
hero.show_scripts() 

if "knife" in hero.inventory: 
    hero.inventory_remove("knife") 
if "sword" in hero.inventory: 
    hero.inventory_remove("sword") 
if "gun" in hero.inventory: 
    hero.inventory_remove("gun") 
if "lance" in hero.inventory: 
    hero.inventory_remove("lance") 
hero.show_inventory()

input ("\n\nPress the enter key to exit.")

#####END OF POPPIE DRYER'S SECTION############

f.close() 