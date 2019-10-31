
#VOLCANO : KIMBERLEY GICQUEL

import random

#the hero finds himself on rocky ladscape --> heat, smell --> volcano --> setting the scene

print ("The hero's eyes need to adjust to the sudden sunlight...")
input ("[Enter]")

print ("\nShe finds herself in the middle of a rocky landscape.")
print ("The first thing she notices is the sulfuric smell surrounding her.")
input ("[Enter]")

print ("\nThe hero gets up, hoping to finally find a way away from this island.")
print ("She tries to see if she can find a pathway.")
input ("[Enter]")

print ("\nThe hero turns around and finds herself in front of a mountain...but the mountain is growling.")
input ("[Enter]")

print ("\nSuddenly it strikes her. This must be a volcano!")
print ("The hero realizes that on top of the volcano she would have an overview of the island and might find a way away from here.""")
input ("[Enter]")

print ("\nHope emerges in the hero. She walks towards the volcano, and although her body aches from exhaustion, she gets ready to climb up.")
input ("[Enter]")

print ("\n\nGET READY FOR THE MINI GAME: LIAR LIAR, PANTS ON FIRE")
input ("Press [Enter] to start the Minigame")

#starting the minigame

#explain the rules to the player
print ("\nTo climb the volcano you need to throw a dice and win against the strength of the volcano.")
print ("The goal is to get a higher number of eyes than the volcano to climb higher.")
print ("But be careful! The volcano is an evil oponent and might lie.")
print ("Reveal his lie and climb higher.")
print ("If the volcano wins over you, you will lose your grip and fall.")
print ("The hero looks strong. Three wins should be enough to reach the top")
print ("Lets get started...")
input ("Press [Enter] to start")


win = 0 #set the numbers of wins to zero, later on the number of wins will be changed
rounds = 0 #set the number of played rounds to zero, with every round one round will be added
volcanolie = 1 #sets the lie of the volcano to 1 (-->is changed during the game)

while rounds < 7 or win < 3: #the player can play a maximum of 6 rounds
    herodice = random.randint(1,6) #the hero rolls the dice
    print ("\nThe hero rolled a", herodice, ".")  #tells player the number of eyes on the rolled dice
   
    if rounds >= 6:     #if the player played 6 or more rounds.
        rounds = 0     #the rounds are set back to 0 so the while loop starts again
        win = 0        #also the wins are set to 0 so the game is reset
        print ("\nThis was exhausting! The hero is out of energy and faints. She falls off the volcano....right back onto the ground.")
        input ("\n\n\nTO RESTART THE GAME \"LIAR LIAR, PANTS ON FIRE\" PRESS [ENTER]")

    elif win == 3:  #the player wins the game if he won three times
        print ("\nWELL DONE! YOU WON THREE TIMES! The hero reaches the top of the volcano")
        print ("She looks around and notices the beauty of this island.")
        print ("Just when she spots the beach that she landed on, she hears a dark growling from inside the volcano.")
        print ("The volcano erupts.\n\n\n") #setting the scene for the next minigame
        print ("""        
      ,*-'. 
      .'+* 
    '   #   ' 
       /v\  
     .'   `.  
__.-"       "-.__             """)

        input ("\n\n\n[Enter]")
        print ("\nA cloud of lava dust surrounds you.")
        print ("Another eruption blows her up in the air and away from the volcano.")
        print ("The hero faints from the heat and when she falls onto the hot, but soft ground all she remembers is the sound of the volcano: \"DA\"...")
        print ("Before loosing consciousness completely, the feeling strikes her that this sound \"da\" is something she should remember.")
        print ("Then everything turns black and the hero loses consciousness....")
        break       #escape the loop and end the game when the player won three times
    
    # if herodice == 6:       #if he rolls a 6 the hero wins, since there is no higher number
        # print ("Great! She wins and climbs up some meters towards the top of the volcano.")
        # win += 1
        # rounds += 1 #both win and rounds are added 1
        # input ("Press [Enter] to keep on climbing")
        
  #  else:   #every situation other than the dice is 6
    volcanodice = random.randint(1,6)  #the volcano rolls the dice
    if volcanodice == herodice:
        print ("\nThe volcano is just as strong as the hero and rolled a", volcanodice, ",too. The hero trembles, but does not fall.")
        input ("Press [Enter] to keep on climbing")

    if volcanodice < herodice:  #the volcano rolled a number lower than the hero
        lie = random.randint(1,2)   # decide whether to lie or not
        if lie == 1:
            volcanolie = herodice + 1 #the volcano decides to lie and tells the hero he rolled a 5
            
			### KB: Added while-loop 
            while True: 
                print ("\nThe volcano tells the hero that he rolled a", volcanolie, ".")
                lier = input ("Should the hero believe the volcano? Or did the volcano lie? (bel/lie): ") #ask player if he believes or if it is a lie		

                if lier == "lie": #the player correctly decides it is a lie and therefore wins
                    print ("\nThe hero yells out: \"LIAR, LIAR, PANTS ON FIRE.")
                    input ("Press [Enter] to see whether the hero is right")
                    print ("\nYou are right! The volcano lied, he only rolled a", volcanodice,". The hero climbs higher, hoping to soon reach the top of the volcano.")
                    win += 1
                    rounds += 1
                    input ("Press [Enter] to keep on climbing")
                    break 

                elif lier == "bel": #the player decides to believe the volcano and plays another round
                    volcanodice == volcanolie #the lie becomes the new volcanodice
                    print ("\nThe hero chooses to believe the volcano. It is now her chance to win over it.")
                    input ("Press [Enter] to keep on climbing")
                    herodice = random.randint(1,6) #the hero rolls the dice again
                   
                    if herodice == volcanodice: #the hero rolls the same number as the volcano --> nothing happens
                        print ("\nYou rolled a",herodice,", too. The hero trembles, but does not fall.")
                        rounds += 1
                        input ("Press [Enter] to keep on climbing")
                        break 
                        
                    elif herodice < volcanodice: #the hero rolls a number lower than the volcano --> he loses and falls off --> win - 1
                        print ("\nThe hero rolled a",herodice,". The volcano is stronger than the hero.")
                        print ("The hero trembles, hears a crack and the stone under his foot breaks off.")
                        print ("She falls back to a lower position.")
                        rounds += 1
                        input ("Press [Enter] to keep on climbing")
                        break 
                        
                    elif herodice > volcanodice: #the hero rolls higher than the volcano --> he wins
                        print  ("\nYeah! You rolled a",herodice,". You are stronger than the volcano and climb higher.")
                        rounds += 1
                        win += 1
                        input ("Press [Enter] to keep on climbing")
                        break 
						
				### KB: catches invalid input		
                else: 
                    print("\nPlease enter 'bel' if you believe the volcano or 'lie' if you think it lied!\n") 
                    continue
                        
        elif lie == 2: #the hero unmasks the lie and wins
            print ("\nYou won! The volcano rolled a", volcanodice, ".")
            win += 1
            rounds += 1
            input ("Press [Enter] to keep on climbing")
                
    if volcanodice > herodice:  #the volcano rolled a number higher than the hero
        print ("\nThe volcano tells the hero that he rolled a", volcanodice, ".")
		
		### KB: Added while-loop 
        while True: 
            lier = input ("Should the hero believe the volcano? Or did the volcano lie? (bel/lie): ") #ask player if he believes or if it is a lie
            
            if lier == "lie":   #if the player falsely choses it to be a lie a round is added
                print ("\nThe hero yells: \"LIAR, LIAR, PANTS ON FIRE\"")
                input ("Press [Enter] to see whether the hero is right")
                print ("\nBut she was wrong. This was not a lie.")
                print ("The hero trembles, hears a crack and the stone under her left hand breaks off.")
                print ("She falls back to a lower position.")
                rounds += 1
                input ("Press [Enter] to keep on climbing")
                break 
                
            elif lier == "bel":   #if the player correctly guessed that it was not a lie the game continues
                print ("\nThe hero chooses to believe the volcano. It is now her chance to win over it.")
                herodice = random.randint(1,6) #the hero rolls the dice again
               
                if herodice == volcanodice: #the hero rolls the same number as the volcano --> nothing happens
                    print ("You rolled a",herodice,", too. The hero trembles, but does not fall.")
                    rounds += 1
                    input ("Press [Enter] to keep on climbing")
                    break 
                    
                elif herodice < volcanodice: #the hero rolls a number lower than the volcano --> he loses and falls off --> win - 1
                    print ("\nThe hero rolled a",herodice,". The volcano is stronger than the hero.")
                    print ("The hero trembles, hears a crack and the stone she reached for breaks off.")
                    print ("She falls back to a lower position.")
                    rounds += 1
                    input ("Press [Enter] to keep on climbing")
                    break 
                    
                elif herodice > volcanodice: #the hero rolls higher than the volcano --> he wins
                    print  ("\nYeah! You rolled a",herodice,". You are stronger than the volcano and climb higher.")
                    rounds += 1
                    win += 1
                    input ("Press [Enter] to keep on climbing")
                    break 	
			
			### KB: catches invalid input
            else: 
                 print("\nPlease enter 'bel' if you believe the volcano or 'lie' if you think it lied!\n") 
                 continue 

input ("Press [Enter] to wake up from your unconsciousness.") #to get to the next Minigame (DESERT - SHANELLE) the player is advised to press the enter button
