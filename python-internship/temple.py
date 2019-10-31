
# TEMPLE OF WISDOM : JAVIER LÓPEZ SIERRA

#introduction of setting and explanation of the game
print("\n\nAfter the encounter with the monkey, our hero finds her way to the end of the jungle. An enourmous wall of stone blocks the way. The wall has a gap, where a temple stands. Going through it might be the only possibility to get past that wall. ")
input("\nPress the enter key to approach the temple.")
print("\nAs our hero approaches the temple, she can see some letters on top of the entrance: 'THE TEMPLE OF WISDOM'. Our brave hero decides to enter.")
input("\nPress the enter key to enter the temple.")
print("\nThe temple is quite dark, but there is enough light to see the back door, very close to a statue of an erudite holding a crosier. The hero walks towards it, and when she is very close, all of a sudden, the statue of the erudite comes alive and obstructs the exit.")
input("\nPress the enter key to interact with the erudite.")
print("\nThe erudite, in a very calm tone, says: 'WELCOME TO THE TEMPLE OF WISDOM. I WAS EXPECTING YOU. ONLY WISE PEOPLE CAN USE THIS TEMPLE TO GO BEYOND THE WALL OF STONE. IF YOU WANT TO CONTINUE YOUR JOURNEY, YOU WILL HAVE TO FIND THE SOLUTION TO A RIDDLE. YOU WILL HAVE THREE OPPORTUNITIES. IF YOU DON'T FIND IT IN THE FIRST TRY, YOU MAY GET A HINT'.")
input("\nPress the enter key to accept challenge.")
print("\nOur hero, who went to a very expensive private school and considers herself very smart, accepts the challenge.")
print("\n\nGET READY FOR THE MINI GAME: THE RIDDLE CHALLENGE")

answer=""

while answer.capitalize() != "Silence": 
    input("\nPress the enter key to hear the riddle.")
   
    riddle1 = print("\n\nWhat is so delicate, that even mentioning it would break it?")
    answer = input("\nYour answer: ")
	
    if answer.capitalize() == "Silence": 
        break 
    else: 
        print("\nThat is not a very wise answer.")
   
    input("\nPress the enter key to obtain a hint from the erudite.") 
    riddle2 = print("\nIt is your lucky day. I will provide you with a hint. Pay attention:")
    input("\nPress the enter key to see hint.")
    print("\nYour answer is something I enjoy in this temple when I don't have visitors.")
    answer = input("\nYour answer: ")
	
    if answer.capitalize() == "Silence": 
        break 
    else: 
        print("\nAgain, that is not a very wise answer.")
		
    input("\nPress the enter key to obtain another hint from the erudite.")
    riddle3 = print("\nI am losing my patience. But I will be nice today, so I will provide you with a very last hint. Pay attention, I won't say it twice:")
    input("\nPress the enter key to see hint.")
    print("\nYour answer is what people demand when they say 'shhhhh.'")
    answer = input("\nYour answer: ")
	
    if answer.capitalize() == "Silence": 
        break 
    else: 
        print("\nOnce again, that is not a very wise answer. Your parents invested too much money in that school for nothing. Sorry, but I refuse to help you. If you want to continue your journey, you will have to start over. I will pretend this didn't happen and ask you again.")
		
    print("\nWow, it looks like the erudite is quite disappointed with your lack of knowledge. He won't let you through until you find the correct answer.")
    input("\nPress the Enter key to restart THE RIDDLE CHALLENGE.") #game will restart

print("\nYou truly are a wise person. You will always be welcome here. You may pass.")
input("\nPress the enter key to obtain help from the erudite.")
print("\nAs a sign of respect, I will provide you with a syllable that might be of great help later.")
input("\nPress the enter key to hear the syllable.")
print("\nThe syllable is:    YA")
input("\n\nPress the enter key to leave the temple.")
				
print("\n\nOur hero, with great satisfaction and the feeling that her parents made the right investment in that private school, leaves the temple.")

input("\n\nPress the enter key to continue.")