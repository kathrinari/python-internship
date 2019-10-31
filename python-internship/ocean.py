#Ocean - Hanna-Negin Roshankar

print("Your hero has come a long journey and travelled all continents and faced a lot of dangerous situations.")
input("[Enter]")
print("\nShe had to enter the ocean since a group of crazy gone orcs was behind her. Your hero is now drowning in the big wide ocean because she cannot swim.")
input("[Enter]")
print("\nShe is far away from the island she wants to reach and from where she needs to travel.")
input("[Enter]")
print("\nWill you help the hero to get there?")
print("\nOh, look! The orcs were able to get a banana boat and are now chasing her!")


input("[Enter]")
print("\nThey are coming closer and closer. Damn they are so close that they are about to catch and eat her!")
print("Her only chance of survival is if she is able to deflate the banana boat!\n")

import random

weapon_list=["cannonball", "sword", "knife", "old shoe", "taser", "gun", "bow", "arrow", "stone"]
meters=(10, 20, 30)
orcmeters= (10,20,30,40)
orcstrength=(random.choice(orcmeters))

while True: 

    print("What kind of weapon should she choose to fight the banana boat? She can choose between:") 
    for item in weapon_list: 
	    print (weapon_list.index(item), " - ", item) 
   
    try: 
	    weapon = int(input("Type in the corresponding number: "))
    except (ValueError, IndexError): 
        print("\nPlease enter one of the displayed numbers!!\n\n") 
        continue 

    while True: 	
        try:  
            herostrength = int(input("How far should she throw her weapon: 10, 20 or 30 meters? "))
        except ValueError: 
            print("\nYou have to enter a valid number!\n")
            continue
		
        if herostrength not in meters: 
            print("\nPlease enter 10, 20 or 30!\n") 
            continue 
        else: 
            break
		
    if (weapon == 2 and herostrength == 10) or (weapon == 0 and herostrength == 20) or (weapon == 4 and herostrength == 30) or (weapon == 0 or weapon == 4 and herostrength < orcstrength):
        print ("\nVery good! She hit the banana boat and defeated the orcs. They are drowning!\n")
        break
    
    else:
        print("\nDamn! She did not strike the boat! Try again.\n")
        continue	
   

print("\nYour hero won the fight!")
input("[Enter]")
print ("\nOh no! But she is so weakened by the fight with the orcs that she blacks out! Again she is drowning...")
input("[Enter]")
print("\nAll that effort seems to have been in vain!")
input("[Enter]")
print("\nWait! What is that? A giant fish is coming up to her!")
input("[Enter]")
print("\nIs it a giant fish? No! It's the most beautiful thing she has ever seen! A gorgeous mermaid!")
input("[Enter]")


print("\nShe seems to give her signs. What is that? She seems to flirt. Does your hero know how to flirt with a mermaid appropriately?")
print("Hurry up! You do not have much energy left!")
input("[Enter]")
print("\n She is winking at her! What should she do (a, b or c)?")
print("a) She winks back.")
print("b) She says: Hey sweetie!")
print("c) She says: Damn! Never seen anything hot like you!")

a1=input("Please type in your answer.")
while a1:
    if a1=="a":
        print("Your hero did well! She liked it!")
        break
    elif a1== "b":
        print("No way! She didn't like it. Try again.")
        a1=input("Please type in your answer.")
    elif a1=="c":
        print("Sorry! A mermaid does not appreciate rude behaviour. Try again.")
        a1=input("Please type in your answer.")
    else: 
        print("Sorry! Your answer is not correct. Try again.")
        a1=input("Please type in your answer.")

input("[Enter]")
print("\nNow she seems to reach for her hand. What should she do (a, b or c)?")
print("a) She tries to touch her face.")
print("b) She flexes and shows off all her muscles.")
print("c) She simply tries to grab her hand in a shy way too.")


a2=input("Please type in your answer.")
while a2:
    if a2 == "a": 
        print("Sorry! She didn't like it. Try again.")
        a2=input("Please type in your answer.")
    elif a2 == "b":
        print("What a bad way to impress a majestic creature like this! Try again.")
        a2=input("Please type in your answer.")
    elif a2 == "c":
        print("Very good! She is smiling at you!")
        break 
    else: 
        print("Sorry! Your answer is not correct. Try again.")
        a2=input("Please type in your answer.")

input("[Enter]")
print("\nHer face is coming closer and closer. Your hero can hear her breathe. She feels her heartbeat through the water. Her face is now close to hers. What should she do (a, b or c)?")
print("a) She looks her deep in the eye.")
print("b) She just kisses her.")
print("c) She tries to give her signs with her head to indicate that she should bring her to the water surface to let her breathe.")

a3=input("Please type in your answer.")
while a3: 
    if a3== "a":
        print("You impressed her! She has fallen in love!")
        break
    elif a3 == "b":
        print("What a rude behaviour! She got angry. Try again!")
        a3=input("Please type in your answer.")
    elif a3== "c":
        print("Sorry! She did not understand at all. Try again!")
        a3=input("Please type in your answer.")
    else:
        print("Sorry! Your answer is not correct. Try again.")
        a3=input("Please type in your answer.")


input("[Enter]")
print("\nYou won the mermaid's heart! Congratulations!")
input("[Enter]")
print("\nMermaid: You absolutely stole my heart! I cannot let you drown!")
print("The mermaid brings you now to the water surface! Finally, you can breathe!!")       
input("[Enter]")
print("\nMermaid: I will now bring you to the island where you belong. But take care, every step you take could be dangerous and your last one! But don't forget that I will always love you :* ")
input("[Enter]")
print("\nAnd remember my name. I am Kiki. You will be in need of the syllables one day!")
print ("\nFinally! Your hero has reached the island! Now she can travel on in to a mysterious forest where she has to survive more adventures!")

input("[Enter]")