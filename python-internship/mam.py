# mix and match

#import modules
import random, pickle

f=open("hero.dat", "rb+")
hero=pickle.load(f) 

# game specific variables

### KB: This could have been done with a dictionary! 

# creates a list with dothraki forms
ls_dothraki = [
    
    "dothralat (inf.)",
    "vitihirat (inf.)",
    "verat (inf.)",
    "elat (inf.)",
    "dothrae (3.pl)",
    "adothrak (1.sg)",
    "acharoe (3.sg)",
    "tih (1.sg)",
    "dothraki (1.pl)",
    "tihi (3.pl)",
    "sajak (1.sg)",
    "zala (3.sg)"

]

# creates a dictionary with english forms and the corresponding number in list for dothraki translation

verbs_english = {
    
    "0 to ride":"0",
    "1 to travel":"1", 
    "2 to observe":"2",
    "3 to go":"3",
    "4 they ride":"4",
    "5 I will ride": "5",
    "6 it will listen":"6",
    "7 I have seen":"7",
    "8 we ride":"8",
    "9 they will see":"9",
    "10 I mount":"10",
    "11 she wants":"11"
 
}

# greet player
# game instructions

print("""
      
    Hello there! Welcome to the game 'Mix and Match'!
    In this game you are going to to get a list of 12 English Verbs and a random dothraki translation to one of the verbs.
    Your task is to give the correct English translation of the dothraki verb by entering the corresponding number of the English verb list given.
    If you give a false answer, you will lose 5 health points.
    When you have successfully completed half the game (match 6 forms correctly), there will be a little surprise for you ;)
    Have fun!!
    
        """)
input("Press the enter key to continue.\n")

# starting the game

correct_answers = 0

#creates a list with all the correctly guessed words
guessed_words =[] 

# while loop that gives out a new dothraki word until all words have been matched correctly
while correct_answers < 12:
    print("Here is the list of possible English translations:")
    for key in 	verbs_english: 
        print(key)
    print()

    print("Here is another dothraki verb:")
    dothraki = random.choice(ls_dothraki)
    
    # while loop that checks if the given dothraki word has already been correctly guessed
    # if so, it gives out a new one
    while dothraki in guessed_words:
        dothraki = random.choice(ls_dothraki)
   
    num_list = ls_dothraki.index(dothraki)
    # print (num_list) # uncomment to see the correct answer
    print(dothraki)
    answer = input("What could this dothraki word mean? Type in the correct number:")
    print()
    
    # making sure that the player gave a valid choice
    if answer in verbs_english.values():
        
        # answer is correct
            if answer == str(num_list):
                    print("This is correct!")
                    correct_answers += 1
                    
                    #creates a list with correctly guessed words
                    guessed_words.append(dothraki)
                    print("So far you gave", correct_answers, "correct answer/s. Good job!")
                    
                    input("Press the enter key to go on.")
                    print()
         
         # answer is false       
            else:
                print("Unfortunately, this is not the correct answer.")
                print("You lose 5 health points.")
                hero.health-=5
                hero.status()
                hero.check()
                input("Press the enter key to try again!")
                print()
                
    # player gave an unknown choice            
    else:
        print("\nSorry, there is no translation for this choice. You have to choose a number between 0 and 11.")
        input("Press the enter key to try again!")
        print()


    if correct_answers == 6:
        print("princess: 'Congratulations, you matched half of all the words correctly already!! You are doing really well so far!'")
        print("'Here is a little game as a reward.'")
        input("Press the enter key to get to your reward!")
        print()
        
        import hangman_ling
        print()
    
        
# player matched all words correctly

print("princess: 'Awesome! You matched all the verbs correctly!'")
print("'You got a first impression of dothraki verb forms.'")
print("'In the next game you are going to learn more about dothraki infinitive forms.'")
input("\nPress the enter key to get to the next game!")
print()

f.close() 