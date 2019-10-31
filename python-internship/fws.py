stems = {"men":"at", "dog":"at", "ger":"at", "ild":"at", "khezh":"at", "nith":"at", "an":"at", "chetir":"at", "orkarlin":"at","feve":"lat", "garvo":"lat", "drivo":"lat", "zigere":"lat", "dothra":"lat", "e":"lat"}
q = {"The name of the univerity's director is Kerstin Krieglstein.":"a", "Language is not arbitrary":"d", "A implicature is a logical conclusion":"d", "The words 'Ship' and 'Sheep' are a minimal-pair":"a", "A phoneme is the smallest unit of language that can change a meaning":"a", "There are just lexical morphemes":"d", "'DOG' is a verbal phrase":"d", "Butt, Braun and Eckard are professors of modern literature":"d"}

import random, pickle

ex = 0 #no of exercises/stems
corr = 0 #no of correct suffixes

f=open("hero.dat", "rb+")
hero=pickle.load(f) 

#implement a while loop to make the player see the explanation
print("""

                           WELCOME TO THE MINIGAME

                          F U N  W I T H  S T E M S

        princess:  'Here comes the explanation:

- You managed the previous game 'Mix and Match' and you got a first impression of verb forms in Dothraki. Now you have to make your knowledge explicit.

- You will find different Dothraki verb-stems. Your only exercise is to fullfill the stems with the corresponding infitive-suffix.

- There will be 10 stems. You have to fullfill at least 8 of them correctly. For each wrong form you lose 7 health points.

- You can choose not to play, but remember: if you exit you can't come back here! Don't disappoint me! 

- Have FUN!'

""")

input("Press the enter key to go on! ")

#now we have to tell the program to print ten random stems of the lists above, and the player has to give us at least 8 correct forms

choice = None
while choice != 0:
        print(
        """
        Your choice: Please choose what you want to do now:
        0 - Exit 
        1 - Return the list of stems
        2 - I need help!!!
        """
            )

        try: 		### KB: added this try-statement to deal with invalid input
            choice = int(input("Your choice: "))
        except ValueError: 
            print("\nPlease enter 1 or 2!\n") 
            continue 
			
        if choice == 0: 
            print("Bye")

        elif choice == 1:
            while ex < 10:
                w = random.choice(list(stems.keys())) #word out of -at-stems
                y = stems[w] #value of the word
                print("This is your word:", w)
                t = input("Give me the correct suffix: ")
                if t == y:
                    print("Right!")
                    ex += 1
                    corr += 1
                    hero.health+=7
                    hero.status()
                    hero.check()
                    print("You have to solve", 10-ex, "more exercises! And you answered", corr, "of the minimum of 8 exercises correctly!")
                    stems.pop(w)
                else:
                    print("Oh no! It's not true. Please look at it again.")
                    ex += 1
                    hero.health-=7
                    hero.status()
                    hero.check()
                    print("You have to solve", 10-ex, "more exercises! And you answered", corr, "of the minimum of 8 exercises correctly!")

            if corr < 8:
                print("You are a loser! You have given less than 8 correct answers...Now you will have to try again. This is your new health", hero.health,". Good-bye, my almost-lover <|3")	
            ### KB: Resetting sentry variables 
                ex = 0 #no of exercises/stems
                corr = 0 #no of correct suffixes
				
                input("Press the enter key to try again!")
			
            else:
                print("\nHEY! I AM SO PROUD OF YOU!!!!!! Now you know the infitive morpheme of dothraki: It's -at if the last letter of the stem is an consonant or -lat if the last letter of the stem is a vowel!")
                input("Press the enter key to go on!")
                break


        elif choice == 2: #help: question game
                quest = 0
                false = 0
                print("So, you say, you need help? Hmmmm...In that case, I think you have to answer a few questions. ALL of them have to be correct. I present you a couple of sentences. You will have to agree or disagree. If you agree, you type 'a'. If you disagree, you type 'd'.")
                input("Alright? Then press the enter key. ")
                while false == 0 and quest < 5:
                        qu = random.choice(list(q.keys()))
                        que = q[qu]
                        print("This is the question:", qu)
                        ans = input("Please answer: " )
                        
                        while ans != "a" and ans != "d": 
                            ans = input("Please enter 'a' for agree or 'd' for disagree: " )
							
                        if ans == que:
                            print("YOU ARE RIGHT")
                            quest += 1
                            q.pop(qu)
                        else:
                            print("YOU ARE WRONG! I am sorry but you have to try again...")
                            quest += 1
                            false += 1
                            input("Press the enter key to choose again.")
							
                while false == 0 and quest == 5:
                        print("Congratulation. You managed the help game! This is your hint: 'Dothralat' and 'Kezhat' are infinitives. The first stem ends with a vowel and the second stem ends with a consonant.")
                        false = None
                        quest = None
                        input("Great. Press the enter key to go on. ")

        else: 		### KB: added the else statement to deal with invalid input 
            print("\nPlease enter a valid choice!\n") 
            continue 			

f.close() 