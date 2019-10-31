### accusative minigames ### 

import random, pickle
#from game import hero

f=open("hero.dat", "rb+")
hero=pickle.load(f)  


print("""
Our hero stands there clueless. Luckily, a smart fox appears!
The fox asks our hero if she needs help.
She thinks "What the heck? a speaking fox?!" but, desperately, decides to answer him.
She shows him the Rossetta Stone and asks him if he knows this language.
The fox says that he studied this language for a whole year in school. Sadly, he only remembers how accusative works.
The fox proposes to study by playing a game.
""")
input("Press enter to begin!")

table = ("""\nThese are the accusative endings:
\n
singular animate, stem -C \t /-es/
singular animate, stem -V \t /-es/
plural animate, stem -C \t /-is/
plural animate, stem -V \t /-es/
inanimate \t\t\t /-/ or /-e/
""")

print(table)

print("""
Now you know how to build the accusative forms and you saw that for the animate nouns you only have to add the right suffix depending on number and the stem type (consonant/vowel final). Therefore we are now going to practice the more complicated forms, those of the inanimate nouns.
""")

AccRules= ("""
There are three rules you have to consider to build the accusative forms of inanimate nouns.

1. one is the bare stem /-/.
So if the stem ends in a consonant nothing changes; the accusative form is equal to the nominative form.

2. in the second case the accusative form is derived by stripping off the final vowel from the nominative form 

3. after applying rule 2. you have to check if the form ends in:
\t - /g/, /w/ or /q/
\t - a vowel (meaning there were originally more than one final vowel)
\t - a complex coda (bigger than or as big as two consonants or a geminate)

If this is the case you have to add an /e/ to the end of the word.

The variance comes from phonotactics of the language.
""")

print(AccRules)

### KB: writing shorter rules for putting into scripts inventory 
Acc1="Accusative1: Nom ends in consonant: /-/"
Acc2="Accusative2: Nom ends in vowel: strip vowel"
Acc3="Accusative3: Nom ends in vowel: strip vowel, add /-e/"

### KB: a dictionary with the nominative as key and the accusative as value
nom_acc = {"qeso":"qes", "os":"os", "sondra":"sondre", "mawizzi":"mawizze", "khewo":"khewe", "alegra":"alegre", "kendra":"kendre", "zhalia":"zhalie", "achrakh":"achrakh", "ador":"ador", "hoggi":"hogge", "soqwi":"soqwe"}


isPlaying = False
usedWords=[]

def wordChoice():
	'''Chooses a random nominative from the dictionary'''
	global usedWords
	 
	word = random.choice(list(nom_acc))		### KB: randomly pick a key from a dictionary (which is the nominative form)
	if word in usedWords: 
		return wordChoice()
	else: 
		usedWords.append(word)			
		accusative = nom_acc[word]
		return word, accusative

def writeAcc():
	'''Minigame: User has to enter the correct accusative form, after three correct answers he passed''' 

	global isPlaying, usedWords
	isPlaying = True
	
# asking the user to enter the right accusative form of the word		
	print("Please enter the accusative form of the following words\n")
	
# player passed when he reached 3 correct answers
	right = 0
	while right < 4:
		word, accusative = wordChoice()

		print("Nominative ", word)
			
		print("Need help? Enter 'y' to see the menu again or press the enter-key to continue.")
		choice = input("\t\t\tChoice: ")
		if choice == 'y':
			continueGame = displayMenu()
			if not continueGame:
				return
			print("Nominative ", word)
		
		answer=input("Accusative ")
		if answer==accusative:
			right+=1
			
		print("Guessed right:", right)
		
		if right < 4 and (len(usedWords) == len(list(nom_acc))):
			print("Sorry you don't seem to have what it takes to learn the accusative.")
			break
	
	if right == 4:
		print("\n\nCongratulations! You passed the first step, you will now enter the next challenge.\n")
		chooseAcc()
		

def chooseAcc():

	global usedWords
	right = 0
	fake_acc = {}
	usedWords = []
	
	print("""Your task in this game is to choose the correct accusative form from 3 different options.""")
 
	while right < 4:
		word, accusative = wordChoice()
		
		print("\nThe nominative is",word)
		
		accusative1 = word[:-1] 	#accusative form by stripping last segment
		print("1", accusative1) 
		fake_acc["1"] = accusative1 
		accusative2 = word 			#accusative equivalent to nominative
		print("2", accusative2)
		fake_acc["2"] = accusative2
		accusative3 = word[:-1] + "e" 	#accusative by stripping last segment and adding e
		print("3", accusative3) 
		fake_acc["3"] = accusative3

		answer = input("Choose the correct accusative form of by entering the corresponding key number:\n\n")
			
		while answer not in fake_acc.keys(): 
			answer = input("Please use one of the key numbers. Choose the correct accusative form by entering the corresponding key number again:\n\n")		
			
		if fake_acc[answer] == accusative: 
			print("Hurra! You chose the correct accusative form!\n")
			right += 1 		#counts correct answers
		
		else:
			print("Sorry, this is not the correct accusative form.\n")
			
		if right < 4 and (len(usedWords) == len(list(nom_acc))):
			print("Sorry you don't seem to have what it takes to learn the accusative.")
			break
		
	if right == 4:
		print("Good job! You chose the correct accusative form 4 times.\n")
		
	scrambledAcc()

### The player is presented with scrambled letters and has to form the correct accusative form ###


def scrambledAcc():
	global usedWords
	
	print('''This is your next challenge:\nYou will be presented with scrambled words and your task is to bring the letters in the right order and find the correct word.
	The sracmbled word is in accusative form to give you a clue you will see the nominative form of the word.''')

	right = 0
	usedWords = []
	
	while right < 4:
		word, accusative = wordChoice() 
		### KB: creating a shuffled version of the accusative
		### KB: in order to do that I have to convert the string to a list
		acc_list = list(accusative)
		random.shuffle(acc_list)
		jumble = ''.join(acc_list)
		
		print("\nThe nominative form of your jumbled word is:", word)		# show the nominative form 
		print("The jumble is:", jumble)											# and the jumbled acc form

		guess = input("\nYour guess: ")											# ask for input
		while guess != accusative and guess != "": 							# if the player typed something in and it is not correct 
			print("\nSorry, that's not correct.")
			print("Do you want to see the rules again?")						# ask the user if he needs to see the rules again
			displayMenu()
			print("\nThe nominative form of your jumbled word is:", word)
			guess = input("What's your guess: ")								# and ask for a new input
	
		while guess == "":														# make sure that the user types something in 
			print("\nYou have to try it and type something in!")
			print("Do you want to see the rules again?")						# ask the user if he needs to see the rules again
			displayMenu()
			print("\nThe nominative form of your jumbled word is:", word)
			guess = input("What's your guess? ")	
			
		if guess == accusative:												# this is the case if the guess is correct
			print("\nThat's it! You built the correct accusative form!\n")
			right += 1			# counting the right answers
		
		else: 
			print("Sorry, that's not right!\n") 
													
		if right < 4 and (len(usedWords) == len(list(nom_acc))):
			print("Sorry you don't seem to have what it takes to learn the accusative.")
			break
			
	print("Perfect! You now know how the accusative works!")			# the player has finished our game
	print("The accusative rules are added to your scripts in case you have to look them up again.")
	print("Good luck with your further challenges!\n")
	
	# add the accusative rules to the scripts inventory
	hero.scripts_append(Acc1)									
	hero.scripts_append(Acc2)	
	hero.scripts_append(Acc3)
	hero.show_scripts()	
	

# function that displays the menu
def displayMenu():
	global isPlaying
	choice = None
	while not choice:

		if isPlaying:
			print("""
			0 - Quit
			1 - Show Accusative Endings
			2 - Inanimate Rules
			3 - Restart 
			4 - Continue Game
			""")
		else:
			print("""
			0 - Quit
			1 - Show Accusative Endings
			2 - Inanimate Rules
			3 - Play
			""")
		
		choice = input("Choice: ")
		print()

		if choice == "0":
			print("Goodbye.")
			exit()
		elif choice == '1':
			print(table)
		elif choice == '2':
			print(AccRules)
		elif choice == '3':
			writeAcc()
			return False
		elif choice == '4' and isPlaying:
			print("Game resumed\n")
			return True
		choice = None

displayMenu() 

f.close()