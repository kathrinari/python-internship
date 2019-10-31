#Project work Ayfer Uygun(AU) and Leonie Beckert(LB)
#Allative form

import random	#für die zufällige Auswahl der Fragen+Antworten, LB
import pickle 

f=open("hero.dat", "rb+")
hero=pickle.load(f)  

#Erklärungs- /Einführungstext, AU
input("\n\nYou walked through a door and suddenly...")
print("\n\nKLONK!")
print("\n\nAlas! There is a cage around you!")
print("In a dark corner of the room you see a silhouette appears.")
print("It's George R. R. Martin with a smile on his face.")


import tkinter as tk	#AU
import time				#AU
import os				#AU

#function, welche GIF öffnet, AU
def gifoeffnen(name,gifnr):		#function 'gifoeffnen', welche Name des GIFs und dessen Frame-Anzahl inbegriffen hat, AU
	giffenster = tk.Tk()	#neues TK-Fenster öffnen, in dem GIF gezeigt wird, AU
	label = tk.Label()
	label.pack()
	counter = 0				#zählt Frames im GIF, AU
	
	while counter < gifnr :		#während noch nich alle Frames im GIF gezeigt wurden, AU
		photo = tk.PhotoImage(file=name, format="gif -index " + str(counter))
		label.config(image = photo)
		time.sleep(0.05)		#Zeit, wie lange jedes Frame angezeigt wird, AU
		giffenster.update()		#GIF-Fenster muss upgedated werden, nach jedem Frame, AU
		counter += 1			#Counter geht ein Frame weiter, AU
		
	if counter > gifnr :		#schließt GIF-Fenster, wenn alle Frames angezeigt wurden, AU
		giffenster.destroy()
		
      
gifoeffnen("george.gif",20)		#öffnet George R. R. Martin "Haters gonna hate"-GIF mit 20 Frames, AU

#Erklärung, was im Spiel passiert, LB
print("He says 'If you're clever and answer my questions correctly you will get some coins.\nFive of them will be enough to save your life... at least for the moment'")
print("'But if you get the answer wrong you will feel the wrath of my whip!'")

#Eingabe des Namens. LB
name = input("\n\n'What's your name?' ")

#Ankündigung des Rätsels, LB
print("\n\n'So,", name, "If your memory is not the best, it might be wise to take some notes. \nYou'll only be hearing this once!'")

#Initialisierung der Variablen: Inventar(AU) und Variable, die Münzen zählt (LB)
inventory = []
coin_counter = 0

#Liste mit den Fragen, welche George stellen wird, LB, AU
questions = [
			"If you give a carrot to a dark bay horse (cheyao), what do you say?", 
			"If you give straw to an ibex (dorvof), would you say 'dorvofaan'? (yes/no)", 
			"When you put something in  a basket (qeso), what do you call it?",
			"You give the mothers (mother = mai) of your best friends some flowers, would you call them maissea? (yes/no)",
			"When you finallly clean yourself and you go into the water (eveth), what do you say?",
			"You eat some olives (olive = ewe), do you eat eweaan? (yes/no)",
			"You give each of your caterpillars (filki) a teddybear, so they sleep well. What do you call them?",
			"You plant some beautiful flowers, so the bees (bee = giz) have something to eat. Is gizea correct? (yes/no)",
			"You shoot an arrow towards Cersei, because everybody hates her. What's the correct form of her name?"
			]

			
#Liste mit den richtigen Antworten, LB, AU			
answers = ["cheyaosaan", "yes", "qesaan", "no", "evethaan", "yes", "filkisea", "yes", "Cerseisaan"]

### KB: Could have used dictionary! 

### KB: Stating allative rules 
all1="Allative inanimante: /-aan/"
all2= "Allative animate: /-(s)aan/" 
all3="Allative animate plural: /-(s)ea/"

#Initialisierung des "Menüs", LB
choice = None

#"Menü" mit der Wahl spielen oder aufhören, 0 = aufhören, 1 = spielen, LB
while choice != "0":		#Wenn die Auswahl nicht "0" ist, immer "Menü" anzeigen, LB
	print(					#"Menü" anzeigen, LB
	"""
	You can choose between these options:
	
	0 - Quit
	1 - Face the challenge
	
	"""
	)
	
	#Erfragen der Auswahl, LB
	choice = input("Choice: ")
	
	#Start des Spiels mit Rätsel über Allativ, LB
	if choice == "1":
		#Rätsel anzeigen, AU
		print(
		"""
		
		'Can you solve this linguistic mystery?

        The theory of the allative Form in Dothraki says
        if you want to denote a movement towards a noun 
        you have to solve the riddle in the following rhyme:
                
		To know if your word is alive or death
		You need to know if it takes a breath.

		Unless it's not taking a breath
		and no matter the stem
		it ends with  -aan.

		Can you hear a single heartbeat which is absonant
		and it ends with a consonant, 
		-aan is its only consequent.

		Do not ogle,
		when your single heartbeat follows now a vowel
		you have to focus on the end, 
		with -saan the stem is condemned!

		Winter is coming
		A plural number of white walkers along the continent,
		and stems with consonants
		show an -ea at the end.

		Can you imagine flying dragons?
        They hatch out of eggs
        Daenerys Targaryen had plural eyes of them like a jewel
        when your word stem ends with a, e, i, o, u,
        -sea adding at the end is what you need to do. 
		
		""")
		
		#Während Hero noch lebt und nicht genug Münzen hat, LB
		while (hero.health > 0) and (coin_counter < 5):
		
			#wählt Zahl zufällig aus der Länge der Liste mit Fragen, LB
			number = random.randrange(len(questions))
			
			#zeigt die zufällig gewählte Frage an, LB
			print(questions[number])
			
			#erfragt die Antwort, LB
			answer = input("\nwhat is your answer? ")
			
			#Wenn die Antwort die richtige ist (selbe Position in der Liste, wie die gestellte Frage), LB
			if answer == answers[number]:
				#Glückwunsch-Nachricht anzeigen, LB
				print("\nCongratulations, that was right. You get one coin!\n\n\n")
				inventory += "coin"		#"Münze" dem Inventar hinzufügen, AU
				coin_counter += 1		#"Münzen"-Counter um 1 erweitern, LB			
			
			#wenn die Antwort falsch ist, LB
			else:
				print("\nNo, that was wrong!")	#Nachricht anzeigen, dass Antwort falsch war, LB
				hero.health -= 10		### KB: changed to minus ten

				#aktuelle Lebenspunkte anzeigen
				hero.status() 	

			#gestellte Frage + Antwort aus der jeweiligen Liste löschen
			del questions[number]
			del answers[number]

		#wenn die Lebenspunkte verbraucht sind, LB
		if hero.health <= 0:
			#Nachricht über den Tod anzeigen, LB
			print("Oh no! You got whipped to death by George R. R. Martin. \nTry again if you're brave enough.")	

			#Todes-GIF im seperaten Tkinter-Fenster anzeigen, AU
			gifoeffnen("death2.gif",10)
			
			### KB: restore some health 
			hero.health += 50
			#Münzen-Counter resetten, LB
			coin_counter = 0

			#Frage- und Antwortliste resetten,damit wieder alle vorhanden sind für die nächste Runde, LB
			questions = [
			"If you give a carrot to a dark bay horse (cheyao), what do you say?", 
			"If you give straw to an ibex (dorvof), would you say 'dorvofaan'? (yes/no)", 
			"When you put something in  a basket (qeso), what do you call it?",
			"You give the mothers (mother = mai) of your best friends some flowers, would you call them maissea? (yes/no)",
			"When you finallly clean yourself and you go into the water (eveth), what do you say?",
			"You eat some olives (olive = ewe), do you eat eweaan? (yes/no)",
			"You give each of your caterpillars (filki) a teddybear, so they sleep well. What do you call them?",
			"You plant some beautiful flowers, so the bees (bee = giz) have something to eat. Is gizea correct? (yes/no)",
			"You shoot an arrow towards Cersei, because everybody hates her. What's the correct form of her name?"
			]
		
			answers = ["cheyaosaan", "yes", "qesaan", "no", "evethaan", "yes", "filkisea", "yes", "Cerseisaan"]

		
		#Spiel gewinnen, wenn man fünf Münzen hat, LB
		elif coin_counter == 5:
			#Glückwunsch-Nachricht anzeigen, LB
			print("Very good! You may continue with your fight for the iron throne.")
			hero.scripts_append(all1) 
			hero.scripts_append(all2) 
			hero.scripts_append(all3) 
			hero.show_scripts() 
			
			#Anzeigen von Xena-GIF, AU
			gifoeffnen("xena.gif",25)
			break 


	#Beenden des Spiels bei Auswahl "0" im Menü, LB
	elif choice == "0":
		input("\n\nChicken! Press enter to exit.")
		
f.close() 
