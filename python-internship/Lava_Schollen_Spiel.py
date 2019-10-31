#lava schollen spiel
#by Friederike Hohl
import random, pickle 

f=open("hero.dat", "rb+")
hero=pickle.load(f)  

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

### KB: I added the text for context, since I changed the game to play the Lava_Schollen_Spiel automatically after either winning, losing or quitting. 
input("...") 
input("...") 
input("...") 
input("Finally!\n")

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
        print("\nThere was no space left, so you fell into the lava. -5 health")
        print("\nYou have to try again.")
	### KB: added health subtraction 
        hero.health-=5
        hero.status()
        hero.check()
        #set variables back
        wrongGuesses = 0
        lettersUsed = []
        soFar = "-" * len(WORD)
        hints = 0
        y = True
    else:
        print("\nYou guessed the word and land safely on solid grounds.")
        print("\nThe word is", WORD)
        hero.scripts_append("dorvof = ibex") 
        hero.show_scripts()
        y = False

input("\n\nPress the enter key to exit.")

f.close() 