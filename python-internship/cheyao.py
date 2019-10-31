################################################################
############################ GROUP #############################
################################################################

import random, pickle 

f=open("hero.dat", "rb+")
hero=pickle.load(f)  

#Quiz Game, Storyline

print("""
\n\nHello hero, you have come a long way.
Congratulation.

Solve this game and you will gain a bit of information about 
the unknown language and the word "cheyao" that will enable 
you to decipher the inscription on the doorway.  
_____________________________________________________________

GAME RULES:

ANSWER 8/10 QUESTIONS TO WIN
YOU HAVE 3 LIVES
YOU HAVE ONE 50:50 JOKER
YOU HAVE ONE FAIRY JOKER
""")

print(
"""
===========================LET'S START========================

""")

# setting starting variables 
lives = 3
score = 0
remainingQ = 10
# Joker inventory
JOKER = ["50:50", "Fairy Joker"]


def questions(question, correct): 
    global lives, score, remainingQ, JOKER
    print(question) 
	
    while JOKER: 
	# choosing a joker yes/no
        wahl = input("Do you want to use a Joker?(yes/any other key for no): ")
        if wahl.lower() == "yes":
            print("Available Joker:", JOKER)
            joker = input("\nYou choose: ")
            if joker == "50:50":
			    ### KB: list with all possible answers
                answers=["a", "b", "c", "d"]
				### KB: remove the correct answer from the list
                answers.remove(correct)
				### KB: chose a random answer from the list to be the fake
                fake=random.choice(answers)
				### KB: put the fake and correct answer into another list
                possible=[correct, fake]
                ### KB: sort the list alphabetically
                possible.sort()
                print("\n One of these two is correct:", possible)
                JOKER.remove("50:50")	# deleting the joker from the list
                break 
            elif joker.lower() == "fairy joker":
                print("\nMy fairy instincs say that ", correct, " is the right answer!")
                JOKER.remove("Fairy Joker")	# deleting the joker from the list
                break 
            else:
                print("You didn't choose a Joker.")
						
        else: 
           break 
			
    answer = input("Type in your answer: ").lower()

   # scores if he get 8/10 questiones right
   # if/else statements for the answers
   #if wrong -1 lives and if right +1 score
    if answer == correct:
        print(" \nCORRECT!! ")
        score += 1
    else:
       print(" \nWRONG ")
       lives -= 1
					
    remainingQ -= 1
    input("\n\nPress Enter to answer the next question.")
		

	
question1 = '''
    Q1 - What is the study of language and languages?
    __________________________________________________
     a - Phonetics
     b - Syntax
     c - Linguistics
     d - Semantics
    '''

correct1="c" 

question2 = '''
    Q2 - What is the study of the meaning of languages?
    ____________________________________________________
     a - Phonetics
     b - Syntax
     c - Linguistics
     d - Semantics
    '''
	
correct2="d"
	
question3 = '''
    Q3 - Phonetics is the study of the sounds of language.
         What do we call to this sounds?
    ______________________________________________________
     a - Morphemes
     b - Phonemes
     c - Syntax
     d - Lexicology
    '''
	
correct3="b"

question4 = '''
    Q4 - What is the study of language as it pertains to social classes,
         ethnic groups and genders?
    ____________________________________________________________________     
     a - Psycholinguistics
     b - Comparative linguistics
     c - Sociolinguistics
     d - Linguistics
    '''
	
correct4="c"
	
question5 = '''
    Q5 - Shakespeare is born on 1564 and died on....?
    __________________________________________________     
     a - 1660
     b - 1664
     c - 1616
     d - 1620
    __________________________________________________
    '''
	
correct5="c"
	
question6 = '''
    Q6 - We can also use the upper teeth with the lower lip,
        for _________ sounds. This is how we make an f sound.
    _________________________________________________________     
     a - Uvular
     b - Labiodental
     c - Velar
     d - Nasal
    _________________________________________________________
    '''
	
correct6="b"
	
question7 = '''
    Q7 - Which of these is a daughter language?
    ___________________________________________     
     a - Spanish
     b - Germanic
     c - Latin
     d - Hellenic
    ___________________________________________ 
    '''
	
correct7="a"

question8 = '''
    Q8 - Which is a child's strategy of language acquisition?
         
     a - Bootstrapping
     b - Overextension
     c - Chunking
     d - All of the above
    '''
	
correct8="d"

question9 = '''
    Q9 - What is Ebonics?
    _________________________________________________________     
     a - Bosnian, Croatian, Serbian base languages.
     
     b - An alternative term used in 1997 for various
         dialects of the African-American English.
         
     c - Languages of Europe belong to the Indo-European
         language family.
         
     d - A language that is the recorded or hypothetical
         ancestor of another language or group of languages.
    '''
	
correct9="b"
	
question10 = '''
    Q10 - What is study of written symbols?
         
      a - Lexicology
      b - Phraseology
      c - Phonology
      d - Orthography
    '''

correct10="d"

while True: 
    while remainingQ > 0:  
        questions(question1, correct1) 

        questions(question2, correct2) 

        questions(question3, correct3) 

        questions(question4, correct4) 

        questions(question5, correct5) 

        questions(question6, correct6) 

        questions(question7, correct7) 

        questions(question8, correct8)

        questions(question9, correct9) 

        questions(question10, correct10) 

### KB: End of game begins here when remaining questions are set to zero
 
  ### KB: Hero answered 8 or more questions correctly
    # Showing the score and the information about the word
    if score >= 8:
        print("""
                Congratulations! You are a smart HERO.
                You have""",
                score, """ Questions out of 10 correct!

                Here is the Information about the Dothraki
                word 'CHEYAO':

                - It is a determiner phrase (DP).
                - 'CHEYAO' means 'dark bay horse'.

    ******************************************************************
    ***************Good luck with your next adventure.****************
    ******************************************************************

                """)
        hero.scripts_append("cheyao = dark bay horse") 
        hero.show_scripts()
        break
				
    #if the hero doesn't reach the score (8/10), he fails
    else:
       ### KB: If hero also lost all of his lives
        if lives <= 0: 
            print("""
		   
You lost all of your lives! 

                
      GAME OVER

    """)
	
            print("Your health is reduced by 10!")
            hero.health-=10 
            hero.status() 
            hero.check()

	   ### KB: If hero didn't lose all of his lives, but also didn't reach 8/10
        else: 
            print("""
                Nice try, Hero.
                But you failed.
                
              """, score)
			  
        #asking if the player wants to play again
        again = input("Do you want to try again? Press 'n' to end and 'Enter' to try again.")
		
        if again.lower() == "n":
            print("\n You have left the game.")
            break
        else: 
	   ### KB: variables/list are set to initial state again
            lives=3 
            score=0
            remainingQ=10
            JOKER=["50:50", "Fairy Joker"]
			
f.close() 