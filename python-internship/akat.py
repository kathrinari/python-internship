#Project work
#Baumann/Gustedt


#Packages to import
import random, pickle 
from tkinter import*

#Fix hero values
bag= ["knife", "night vision goggles", "firestone", "healing potion"]
### KB: I fixed the syntax here. 
ups=0
pw= "nature"

f=open("hero.dat", "rb+")
hero=pickle.load(f) 

#Setting and main game loop (Stephanie Gustedt)
piepmatz = ("""

                        _.-.
                    .-.  `) |  .-.
                _.'`. .~./  \.~. .`'._
            .-'`.'-'.'.-:    ;-.'.'-'.`'-.
             `'`'`'`'`   \  /   `'`'`'`'`
                         /||\

                        / ^^ \

                        `'``'`

        """)
stake= ("""
                    \\\////
                    |.)(.|
                    | || |
                    \(__)/
                    |-..-|
                    |o\/o|
               .----\    /----.
              / / / |~~~~| \ \ \

             / / / /|::::|\ \ \ \

            '-'-'-'-|::::|-'-'-'-'
                   (((^^)))
                    >>><<<
                    ||||||
                    (o)(o)
                    | /\ |
                    (====)
                    |_/\_|
                    (_/\_)
                   _|_,__|_
                  (___\____) """)

fire='''    (                ,&&&.
            )                .,.&&
           (  (              \=__/
               )             ,'-'.
         (    (  ,,      _.__|/ /|
          ) /\ -((------((_|___/ |
        (  // | (`'      ((  `'--|
      _ -.;_/ \\--._      \\ \-._/.
     (_;-// | \ \-'.\    <_,\_\`--'|
     ( `.__ _  ___,')      <_,-'__,'
     `'(_ )_)(_)_)' '''

isle='''
          _
         /_'. _
       _   \ / '-.
      < ``-.;),--'`
       '--.</()`--.
         / |/-/`'._\
         |/ |=|
            |_|
       ~`   |-| ~~      ~
   ~~  ~~ __|=|__   ~~
 ~~   .-'`  |_|  ``""-._   ~~
  ~~.'      |=|    O    '-.  ~
    |      `"""`  <|\      \   ~
~   \              |\      | ~~
     '-.__.--._    |/   .-'
          ~~   `--...-'`    ~~
  ~~         ~          ~
         ~~         ~~     ~

'''

print(isle)


print("After this successful quest, your hero walks along the beach when she \
suddenly gets aware of something round in the sand.")

print("Your hero bends over and grabs the round, shiny object. She realizes \
this is the handle of a door on the ground.")

input("\nPress Enter key to continue.")

print("\nExcited about her next adventure, she pulls the door open and jumps \
fearlessly into the dark.")

input("\nPress Enter key to continue.")

print("\nYour hero lands on a hard stony ground. When she stands up, torches \
magically light up, so she can look around.")

print("She is standing in the middle of a moist, stony room. In front of her there are six doors, each of them with an 'X'.")

DOORS=(
"""
___________________________________________________________________________
`.______A___________B___________C___________D___________E___________F_____.'
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||   X   || ||   X   || ||   X   || ||   X   || ||   X   || ||   X   ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||o      || ||o      || ||o      || ||o      || ||o      || ||o      ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
  _||_______||_||_______||_||_______||_||_______||_||_______||_||_______||_
.'_________________________________________________________________________`.

""",


"""
___________________________________________________________________________
`.______A___________B___________C___________D___________E___________F_____.'
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||   A   || ||   X   || ||   X   || ||   X   || ||   X   || ||   X   ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||o      || ||o      || ||o      || ||o      || ||o      || ||o      ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
  _||_______||_||_______||_||_______||_||_______||_||_______||_||_______||_
.'_________________________________________________________________________`.

""",

"""
___________________________________________________________________________
`.______A___________B___________C___________D___________E___________F_____.'
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||   A   || ||   K   || ||   X   || ||   X   || ||   X   || ||   X   ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||o      || ||o      || ||o      || ||o      || ||o      || ||o      ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
  _||_______||_||_______||_||_______||_||_______||_||_______||_||_______||_
.'_________________________________________________________________________`.

""",

"""
___________________________________________________________________________
`.______A___________B___________C___________D___________E____________F____.'
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||   A   || ||   K   || ||   A   || ||   X   || ||   X   || ||   X   ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||o      || ||o      || ||o      || ||o      || ||o      || ||o      ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
  _||_______||_||_______||_||_______||_||_______||_||_______||_||_______||_
.'_________________________________________________________________________`.

""",

"""
___________________________________________________________________________
`.______A___________B___________C___________D___________E___________F_____.'
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||   A   || ||   K   || ||   A   || ||   T   || ||   X   || ||   X   ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||o      || ||o      || ||o      || ||o      || ||o      || ||o      ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
  _||_______||_||_______||_||_______||_||_______||_||_______||_||_______||_
.'_________________________________________________________________________`.

""",

"""
___________________________________________________________________________
`.______A___________B___________C___________D___________E___________F_____.'
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||   A   || ||   K   || ||   A   || ||   T   || ||   =   || ||   X   ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||o      || ||o      || ||o      || ||o      || ||o      || ||o      ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
  _||_______||_||_______||_||_______||_||_______||_||_______||_||_______||_
.'_________________________________________________________________________`.

""",

"""
___________________________________________________________________________
`.______A___________B___________C___________D___________E___________F_____.'
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||   A   || ||   K   || ||   A   || ||   T   || ||   =   || ||   2   ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||o      || ||o      || ||o      || ||o      || ||o      || ||o      ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
   ||       || ||       || ||       || ||       || ||       || ||       ||
  _||_______||_||_______||_||_______||_||_______||_||_______||_||_______||_
.'_________________________________________________________________________`.

""")

missioncompl=0

print(DOORS[missioncompl])

print("Your hero knows that if she wants to get outside, she has to find the \
right door. Maybe behind one or more of these doors she might find some hints for \
decoding the inscription.")

input("\nPress Enter key to continue.")


freak='''


   .o oOOOOOOOo                                            OOOo
   Ob.OOOOOOOo  OOOo.      oOOo.                      .adOOOOOOO
   OboO"""""""""""".OOo. .oOOOOOo.    OOOo.oOOOOOo.."""""""""'OO
   OOP.oOOOOOOOOOOO "POOOOOOOOOOOo.   `"OOOOOOOOOP,OOOOOOOOOOOB'
   `O'OOOO'     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO'    `OOOOo
   .OOOO'            `OOOOOOOOOOOOOOOOOOOOOOOOOO'            `OO
   OOOOO                 '"OOOOOOOOOOOOOOOO"`                oOO
  oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
 oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OOOOOOOOOOOOO.OOOOOOOOOOOOOO
"OOOO"       "YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     "OOO"
   Y           'OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?'         :`
   :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
   .            oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
                '%o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO':
                     `$"  `OOOO' `O"Y ' `OOOO'  o             .
   .                  .     OP"          : o     .
                             :
                             .

'''

spaceship= '''
        `. ___
                    __,' __`.                _..----....____
        __...--.'``;.   ,.   ;``--..__     .'    ,-._    _.-'
  _..-''-------'   `'   `'   `'     O ``-''._   (,;') _,'
,'________________                          \`-._`-','
 `._              ```````````------...___   '-.._'-:
    ```--.._      ,.                     ````--...__\-.
            `.--. `-`                       ____    |  |`
              `. `.                       ,'`````.  ;  ;`
                `._`.        __________   `.      \'__/`
                   `-:._____/______/___/____`.     \  `
                               |       `._    `.    \

                               `._________`-.   `.   `.___
                                             SSt  `------'`
'''



enemy_pictures = ("""

 ___    ___
( _<    >_ )
//        \\
 \\___..___//
 `-(    )-'
    |__|_
  /_|__|_\

  /_|__|_\
  /_\__/_\

   \ || /   _)
     ||    ( )
      \\___//
       `---'
                          """,


            """
             : `.--.' ;              _....,_
             .'      `.      _..--'"'       `-._
            :          :_.-'"                  .`.
            :  6    6  :                     :  '.;
            :          :                      `..';
            `: .----. :'                          ;
              `._Y _.'               '           ;
                'U'      .'          `.         ;
                   `:   ;`-..___       `.     .'`.
                   _:   :  :    ```"''"'``.    `.  `.
                 .'     ;..'            .'       `.'`
                `.......'              `........-'`""",


            """
                                _,,......_
                             ,-'          `'--.
                          ,-'  _              '-.
                 (`.    ,'   ,  `-.              `.
                  \ \  -    / )    \               \

                   `\`-^^^, )/      |     /         :
                     )^ ^ ^V/            /          '.
                     |      )            |           `.
                     9   9 /,--,\    |._:`         .._`.
                     |    /   /  `.  \    `.      (   `.`.
                     |   / \  \    \  \     `--\   )    `.`.___
            -hrr-   .;;./  '   )   '   )       ///'       `-"'
                    `--'
                    7//\    ///\
            """)


print("\nNow it´s her turn. Which door shall your hero enter?")


#Further variables for the main game loop (SG)

choice = None #none=zero in terms of a number

doorletter=[]

loopdoor=0



#while-loop, the game begins (SG)

while missioncompl < 6:


    print(DOORS[missioncompl])

    choice = input("Choose a door: ")
    choice = choice.upper()
    print()

    # wrong doors (SG)
    if choice == "A":
        print("\nDoor A opens.")
        input("\nPress enter key to continue. ")
        print(freak)
        print("\nThat was not a good decision. The freak of death appears \
and kills your hero immediately. Outch...")
        print("\nLuckily, your hero drank her magic potion at the beginning of the quest\
(yes, she did).")
        ups+=1

        if "A" not in doorletter:
            missioncompl += 1
            doorletter += "A"

        else:
            print("\n\nNice try. Maybe you should try the other doors, too. \
Here you are just gonna die.")
        input("\n\nPress enter key to continue.")


    elif choice == "F" and "F" not in doorletter:
        print("\nDoor F opens. Your hero enters it and finds herself...")
        input("\nPress enter key to continue.")
        print("\nIn the exact same room of doors she just came from.")
        loopdoor += 1
        if loopdoor == 3:
            missioncompl += 1
            doorletter += "F"


    ### correct doors

    #Minigame behind door 'B' (Stephanie Gustedt)

    elif choice == "B" and "B" not in doorletter:
        print("\nDoor B opens.")
        input("\nPress enter key to continue. ")
        print("\nInstructions:")
        print("\nIn the following you will see that an extra window opens.")
        print("In this window you will see some linguistic multiple choice questions.")
        print("In order to answer them, memorize the answers (or write them down), close the \
window and type in your answers here.")
        print("\nCaution! The questions are not very difficult but each wrong answer takes \
your hero one life.")

        input("\nIf you are mentally ready, press enter to continue. ")
        ## First task
        tk=Tk()
        canvas=Canvas(tk, width=400, height=600)
        canvas.pack()
        task1=PhotoImage(file=r'phonetictask.gif')
        canvas.create_image(0, 0, anchor=NW, image=task1)
        tk.mainloop()

        input("\nPress enter key to continue. ")
        print("\nNow you can type in your answers.")
        acceptedanswers= 'abc'
        answer=0
        print("\nFirst question:")

        #Answer for ballons
        while answer != "b":
            answer=input("\n\nWhat was the correct transcription of the word 'balloons'? ")
            answer=answer.lower()
            if answer not in acceptedanswers:
                print("\nSorry,", answer, "is not a valid choice.")

            else:
                if answer == "b":
                    print("\nThat is correct. Good job.")

                else:
                    print("\nNope, sorry. Your hero just lost one life.")
                    ups += 1


        #Answer for protection
        answer=0
        while answer != "a":
            answer=input("\n\nWhat was the correct transcription of the word 'protection'? ")
            answer=answer.lower()
            if answer not in acceptedanswers:
                print("\nSorry,", answer, "is not a valid choice.")

            else:
                if answer == "a":
                    print("\nThat is correct. Good job.")

                else:
                    print("\nNope, sorry. Your hero just lost one life.")
                    ups += 1


        #Answer for purring
        answer=0
        while answer != "c":
            answer=input("\n\nWhat was the correct transcription of the word 'purring'? ")
            answer=answer.lower()
            if answer not in acceptedanswers:
                print("\nSorry,", answer, "is not a valid choice.")

            else:
                if answer == "c":
                    print("\nThat is correct. Good job.")

                else:
                    print("\nNope, sorry. Your hero just lost one life.")
                    ups += 1

### KB: could have been done via function with parameters

        ## Second task

        input("\n\nPress enter key for your second task. ")

        tk=Tk()
        canvas=Canvas(tk, width=1000, height=600)
        canvas.pack()
        task2=PhotoImage(file=r'phonologytaskI.gif')
        canvas.create_image(0, 0, anchor=NW, image=task2)
        tk.mainloop()

        input("\nPress enter key to continue. ")
        print("\nNow you can type in your answers.")
	
		
        answer=0
        print("\nSecond question:")

        #Answer for first sound
        while answer != "c":
            answer=input("\n\nWhat were the correct features of the first sound? ")
            answer=answer.lower()
            if answer not in acceptedanswers:
                print("\nSorry,", answer, "is not a valid choice.")

            else:
                if answer == "c":
                    print("\nThat is correct. Good job.")

                else:
                    print("\nNope, sorry. Your hero just lost one life.")
                    ups += 1


        #Answer for second sound
        answer=0
        while answer != "a":
            answer=input("\n\nWhat were the correct features of the second sound? ")
            answer=answer.lower()
            if answer not in acceptedanswers:
                print("\nSorry,", answer, "is not a valid choice.")

            else:
                if answer == "a":
                    print("\nThat is correct. Good job.")

                else:
                    print("\nNope, sorry. Your hero just lost one life.")


        ## Third task

        input("\n\nPress enter key for your third task. ")

        tk=Tk()
        canvas=Canvas(tk, width=800, height=900)
        canvas.pack()
        task3=PhotoImage(file=r'phonologytaskII.gif')
        canvas.create_image(0, 0, anchor=NW, image=task3)
        tk.mainloop()

        input("\nPress enter key to continue. ")
        print("\nNow you can type in your answers.")

        answer=0
        print("\nThird question:")

        #Answer for first question
        while answer != "b":
            answer=input("\n\nWhich sound did the first features describe? ")
            answer=answer.lower()
            if answer not in acceptedanswers:
                print("\nSorry,", answer, "is not a valid choice.")

            else:
                if answer == "b":
                    print("\nThat is correct. Good job.")

                else:
                    print("\nNope, sorry. Your hero just lost one life.")
                    ups += 1


        #Answer for the second question
        answer=0
        while answer != "c":
            answer=input("\n\nWhich sound did the second features describe? ")
            answer=answer.lower()
            if answer not in acceptedanswers:
                print("\nSorry,", answer, "is not a valid choice.")

            else:
                if answer == "c":
                    print("\nThat is correct. Good job.")

                else:
                    print("\nNope, sorry. Your hero just lost one life.")
                    ups += 1


        #Answer for the third question
        answer=0
        while answer != "c":
            answer=input("\n\nWhich sound did the third features describe? ")
            answer=answer.lower()
            if answer not in acceptedanswers:
                print("\nSorry,", answer, "is not a valid choice.")

            else:
                if answer == "c":
                    print("\nThat is correct. Good job.")

                else:
                    print("\nNope, sorry. Your hero just lost one life.")
                    ups += 1


        ## Fourth task

        input("\n\nAlmost over. Press enter key for your last task. ")
        tk=Tk()
        canvas=Canvas(tk, width=900, height=400)
        canvas.pack()
        task4=PhotoImage(file=r'phonologytaskIII.gif')
        canvas.create_image(0, 0, anchor=NW, image=task4)
        tk.mainloop()

        input("\nPress enter key to continue. ")
        print("\nNow you can type in your answer.")

        answer=0
        print("\nFourth question:")

        while answer != "b":
            answer=input("\n\nWhich was the correct rule to describe the English Schwa deletion? ")
            answer=answer.lower()
            if answer not in acceptedanswers:
                print("\nSorry,", answer, "is not a valid choice.")

            else:
                if answer == "b":
                    print("\nThat is correct. Good job.")

                else:
                    print("\nNope, sorry. Your hero just lost one life.")
                    ups += 1


        print("\nGreat, your hero won! Automatically she is back in the room of doors.")
        missioncompl += 1
        doorletter += "B"


#Minigame behind door 'C' (Anne Baumann)
    elif choice == "C" and "C" not in doorletter:
        print("\nDoor C opens.")
        input("\nPress enter key to continue. ")

        WORDS = ("dangerous", "island", "death", "blood")

        pw = "bird"
        entered_word = " "

        print("\nYour hero enters the room behind door C and stands in front of a huge stake.\n\n")
        print(stake)

        input("\nPress enter key to continue.")

        print("\n\nShe summons up her courage and tiptoes around the stake. On each side of it, she can see some letters in forms a cube. \
Unfortunately, they do not make sense at all. But... they must have something to do with the four holes on the ground. \
The holes have the same size as the letters. Also, the cubes can be taken out and put in again.")

        input("\n\nYour hero wants to solve the riddle... and looks at the first combination of letters.\
        \n\nPress the enter key to continue.")

        for word in WORDS:

           #creation of a jumbled version of it
            word_list = list(word) 
            random.shuffle(word_list)
            jumble = ''.join(word_list)

            print("\nThe word she looks at is: ", jumble) 

           #Players guess
            guess = input("What could this mean? Please enter your guess:")
            while guess.lower() != word.lower():
                    print("\nNope, that's not it. Please try again.")
                    guess = input("Your guess:")

            print("\nSuddenly, the first cube of the word is highlighted. This must be the solution! Great!")

        print("\n\nYour hero now has solved all the four riddles. She is standing in front of the stake and looks at the \
highlighted letters. Then, she tries to take them out... and it works! But now, she needs to put the cubes \
into the holes at the bottom of the stake. She looks at her letters D -- I -- R -- B again...")

        while True:
            try:
                hint=" "
                hint = int(input("\n\nWhat do you want to do? Choose 1 to try to to fit in the cubes directly or look for one more hint by entering 2: "))
                break

            except:
                print("\nSorry, this is not a valid choice.")

        while entered_word.lower() != "bird":
            if hint == 1:
                entered_word = input("Please put the cubes into the right order: ")

            elif hint == 2:
                print("\n\nYour hero takes her time and investigates the room. \
Then, she hears a strange noise and looks around... somehow, some kind of animal got in here.")
                print(piepmatz)
                pw = "bird"
                entered_word = input("Please put the cubes into the right order: ")

            else:
                print("\nSorry, this is not a valid choice.")
                entered_word = input("Please put the cubes into the right order. You lost the chance to get a hint: ")

        input("\nSuper! All the stones lit up and the stake starts to sink into the ground. \
Then, she sees a short flash. Press enter to see the words lighted up by the flash!\n")
        print("""     _
          _ __   __ _| |_ _   _ _ __ ___         
         | '_ \ / _` | __| | | | '__/ _ \
         | | | | (_| | |_| |_| | | |  __/
         |_| |_|\__,_|\__|\__,_|_|  \___|


What could that mean...? She promises herself not to forget those letters... """)

### KB: Had to fix the ASCII. 

        print("\n\nYour hero jumps into the whole and gets back to the room with the doors.")

        input("\n\nPress the enter key to exit.")

        missioncompl += 1
        doorletter += "C"

#Minigame behind door 'D' (Anne Baumann)
    elif choice == "D" and "D" not in doorletter:

        print("Your hero rattles at the door, but cannot open it. She tries harder and harder, \
even jumps into it, but still, nothing happens. Your hero relentlessly pulls and pushes the door... but cannot open it. Suddenly, her \
strenghts are on the vain! \nAll she remembers is sinking down to the floor... After seemingly endless hours of darkness, \
she hears a strange noise, opens her eyes and sees a huge spaceship coming down.")
        print(spaceship)
        print("The spaceship drops a strange bag and disappears immediately.")
        response=" "
        response=input("Press the enter key to see what is inside the bag.")
 
		#for-loop to display all the items
        for item in bag: 
            print(bag.index(item), " - ", item) 
 
        get_item=None 
		
        while get_item != 3: 
		#ask the user which item to choose	
            try: 
	            get_item = int(input("\nWhat item do you want to use first? Please enter its number: "))
            except ValueError: 
                print("\nSorry, this is not a valid choice.\n") 
                continue 
           
            if get_item >= len(bag):
                print("\nSorry,", get_item, "is not a valid choice.")
                continue
            elif get_item != 3:
                print("\nYour hero is way too weak to use this item... Maybe you should try something else first!\n")
                continue  

        print("\nGreat, your hero is now strong enough to try to open the door again.\n")

        #Delete the healing potion from the list as it is already used
        del bag[3]
 	
	    #for-loop to display all the items
        for item in bag: 
             print (bag.index(item), " - ", item)

        while get_item != 1:
		#ask the user which item to choose	
            try: 
	            get_item = int(input("\nWhat item do you want to use now? Please enter its number: "))
            except ValueError: 
                print("\nSorry, this is not a valid choice.\n") 
                continue 
				
            if get_item >= len(bag):
                print("\nSorry,", get_item, "is not a valid choice.")
                continue
            elif get_item != 1:
                print("Your hero applies the", bag[get_item], "but nothing happens... Maybe you should try something else.")
                continue  

        input("\n\nYour hero puts the night vision goggles and sees a hidden button on the right side of the door. \
She presses the button and the door slowly opens. \nPress the enter key to continue.")

        #Create a list of enemies
        enemy_names = ("a scorpion", "a bear", "an aardvark")

        #Determine the number of monsters
        random.seed()
        nr_of_enemies = random.randint(1,3)

        #Create an empty list for enemies to be filled by the random number
        enemy = []
        for number in range(nr_of_enemies):
            ### KB: Randomly chooses number of enemy in the list that is going to appear
            chosen_number = random.randrange(3)
            enemy.append(chosen_number)
		
       #picks current enemy from enemy list 
        e = enemy[-1]

        print("\n\nYou are now inside a dark room. As you are still wearing your night vision goggles, you can see ", enemy_names[e], " running towards you!", enemy_pictures[e])

        #Ask the user for the weapon he wants to use
        print("\nNow, which weapon do you want to use for your first fight?")
       
        while True:
            try:
                weapon = int(input("\nPlease enter 0 for using the knife, 1 for throwing the night vision goggles, 2 for the laser sword \
and 3 for the fire stone to make a huge fire.\n"))
            except ValueError:
                print("\nSorry, this is not a valid choice.")
                continue 

            if weapon < 0 or weapon > 4:
                print("\nSorry,", weapon, "is not a valid choice. Please enter a valid number:")
                continue 
            else: 
                break 

        #Define the effectivity of the weapons against the monsters
        effectivity = (
            (1,0,2,5),
            (2,0,3,5),
            (2,0,3,5))

        while hero.health > 0 and nr_of_enemies > 0:
            power_hero = random.randrange(2) + effectivity[e][weapon]
            power_monster = random.randrange(3)

            if power_hero < power_monster:
                hero.health -= 10
                print("You lost against the monster! You hero loses ten points of his health.")

            elif power_hero > power_monster:
                nr_of_enemies -= 1
                #delete the last item of the list
                enemy.pop()
                print("You won against", enemy_names[e], ".") 

            else:
                print("Hey, it seems like the fight ended in a standoff. So, fight again!")
                continue
             
            try: 
                e = enemy[-1]
            except IndexError: 
                break 
				
            print("\nOh no, there is even more of them!!! Your next enemy is going to be " , enemy_names[e], ".", enemy_pictures[e])
            print("\nNow, which weapon do you want to use for your next fight?")
			
            while True:
                try:
                    weapon = int(input("\nPlease enter 0 for using the knife, 1 for throwing the night vision goggles, 2 for the laser sword \
and 3 for the fire stone to make a huge fire.\n"))
                except ValueError:
                    print("\nSorry, this is not a valid choice.")
                    continue 

                if weapon < 0 or weapon > 4:
                    print("\nSorry,", weapon, "is not a valid choice. Please enter a valid number:")
                    continue 
                else: 
                    break 
			
        if hero.health <= 0:
                print("Your hero is dead.")
                ups+=1
                print("Luckily, this is only a game.")
                hero.health+=50
                print(hero.name, " revives with ", hero.health, "health!") 
        else:
            print("\n\nGreat, you won the battle. You can exit this room now.")

        missioncompl +=1
        doorletter += "D"

#Minigame behind door 'E' (Anne Baumann)
    elif choice == "E" and "E" not in doorletter:
        if "C" not in doorletter:
            print("\nThis door is locked. It seems that you have to enter one of the other rooms first.")
        else:
            print("\nThis door seems to be locked, too! As your hero pulls the door, letters appear above it, \
asking your hero to enter the right password. She scratches her head and thinks desperately about an option \
to get into this room. The password must be somewhere in here... it has to do with one of the other rooms...?")

            password = input("Then suddenly she remembers! There was this word in room C. What was is again?: ")
            while password.lower() != "nature":
                    password=input("You shall not pass! Please try again:")

            print("\nMagnificient! Proud of having overcome this obstacle, makes some steps forward and searches for the next quest.\
After a little walk, she spots a fire with a man sitting next to it. She approaches carefully.")
            print(fire)
            print("\nYour hero and the stranger have a long conversation and he even shares his meal with you! Lucky you,\
for this your hero feels even more healthy!")
            input("Please press enter to continue.")
            hero.health+= 10
            hero.status()
            missioncompl += 1
            doorletter += "E"


    #Doors can only be opened once (except for the death door and door E)
    elif choice in doorletter:
        print("\nYou already entered that door. The door is locked now.")

    else:

        print("Sorry,", choice, "is not a valid choice. \nTry again.")

#At the end of the game (SG)

print(DOORS[missioncompl])

print("\nCongratulations! Your hero accomplished this mission!!!")

print("\nThe doors now show you the meaning of the word 'akat'.")

hero.scripts_append("akat = 2") 
hero.show_scripts()

input("\nPress enter key to continue. ")

print("\n\nSuddenly the doors disappear to make room for one portal - the way out.")

print("""

                                   ___---___
                             ___---___---___---___
                       ___---___---         ---___---___
                 ___---___---                     ---___---___
           ___---___---                                 ---___---___
     ___---___---                   E X I T                   ---___---___
__---___---_________________________________________________________---___---__
===============================================================================
 ||||                                                                     ||||
 |---------------------------------------------------------------------------|
 |___-----___-----___-----___-----___-----___-----___-----___-----___-----___|
 / _ \===/ _ \                                                   / _ \===/ _ \
( (.\ oOo /.) )                                                 ( (.\ oOo /.) )
 \__/=====\__/                                                   \__/=====\__/
    |||||||                                                         |||||||
    |||||||                                                         |||||||
    |||||||                                                         |||||||
    |||||||                                                         |||||||
    |||||||                                                         |||||||
    |||||||                                                         |||||||
    |||||||                                                         |||||||
    |||||||                                                         |||||||
    (oOoOo)                                                         (oOoOo)
    J%%%%%L                                                         J%%%%%L
   ZZZZZZZZZ                                                       ZZZZZZZZZ
  ===========================================================================__|_________________________________________________________________________|__
_|___________________________________________________________________________|_
|_____________________________________________________________________________|
_______________________________________________________________________________

""")

print("\Your hero enters the portal.")

input("\nPress enter key to continue. ")




print("\nThe total of lost lifes in this game:", ups)
if ups == 0:
    print("\nWow, you did not loose any life! That´s a new record!")

elif ups > 7:
    print("\nLucky for you, your are not a cat, otherwise you´ll definitely be \
dead by now.")

elif ups == 1:
    print("\nLost one life? Don´t worry, could have happened to everybody.")

else:
    print("\nHm, you lost", ups, "lifes? That´s a lot. Maybe you should be \
glad that this is only a game. We hope you are more careful in real life...")

print("\nGood luck with the following adventures. Bye, bye")

input("\n\nPress enter key to exit. ")

f.close()
