# Linguistic Gaming with Python 
# Final Projects 

import tkinter as tk
import random, pygame, sys, time, pickle
from pygame.locals import *

FPS = 10
pygame.init()
pygame.display.init()
pygame.mixer.init()
pygame.font.init()

input("Please Press Enter Key to start the game!")

import OpeningDescription

class Hero(object):
    instruction1 = "\nYou need to set your hero's name" 
    name = ""
    health = 100
    inventory = []	
    scripts = []
	
    def __init__(self): 
        self.setting()

    def setting(self):
        self.set_name()
        print('\nHi', self.name, '\n')
        self.status()
        self.show_inventory() 
        self.show_scripts() 

    def set_name(self):
        print(self.instruction1)
        self.name = input('')

    def status(self):
        print('Your health stat is: ', self.health) 
		
### KB: prevents from losing too soon or creating an error in minigames
    def check(self): 
        if self.health <= 0: 
            print("\n\nOh no!!! You lost all of your health!\n Luckily, ", self.name, "drank some potions before sailing off to her adventures...\n") 
            self.health=100 
            print("Your health got restored!\n") 
            self.status() 
		
### KB: functions for showing, adding and removing items to inventory/scripts
    def show_inventory(self): 
        print("Your current inventory contains: ", self.inventory)
		
    def show_scripts(self): 
        print("You have the following scripts: ", self.scripts) 

    def inventory_append(self, item): 
        self.inventory.append(item) 

    def inventory_remove(self, item): 
        self.inventory.remove(item) 

    def scripts_append(self, script): 
        self.scripts.append(script) 

    def scripts_remove(self, script): 
        self.scripts.remove(script) 
		

### KB: creates one instance of the class Hero
hero=Hero()	

### KB: pickle the hero in a file, so other programs can use it and make changes
f = open("hero.dat", "wb")
pickle.dump(hero, f) 
f.close() 
		
import Accusative 

import InfinitiveMorpheme

import daki_davveya 

import addakhat_azhat

import Rosemary 

import Pomegranate

import akat 

import dorvof

import cheyao 

import Allative 

import Imperative 

### KB: after playing all the games, we have to load the current hero again 
f=open("hero.dat", "rb+")
hero=pickle.load(f) 


# 	LAST LEVEL

# Haocheng Ma and Joobin Youn(Scenario Part)
class Scenario(object): 
    check_list = []
    inventory = []

    def __init__(self, health):
        self.health = hero.health
        self.inventory = hero.inventory 
		
    def status(self):
        print('Your health stat is: ', self.health) 
		

    def north(self): 
        print('You have come to the Northern region!')
        self.status()
        choice = input('What would you like to do?\n\n'
                       '1. Interact with the hidden door 2. Leave ')
					   
        if choice == '1':
            if len(self.check_list) != 0:
                print("Your help:") 
                for item in self.check_list:
                    print('** '+ item + ' **')
            else:
                print('You are too weak to open the door right now.')
				
            if ('The Ibex' in self.check_list) and ('Dark Bay Horse' in self.check_list):
                print('')
                print('\nWith the help of the Ibex and the Dark Bay Horse, '
                '\nyou have opened the Hidden Door! '
                '\nTherein you obtain the Object of Power and Value. '
                '\nVictory and Glory to you!')
                return 'Happy'
				
            else:
                print('\nMaybe you should go out there and look for some help!')
                return 'Back'
				
        elif choice == '2':
            print('You returned to the hidden door.')
            return 'Back'
        else:
            print('You returned to the hidden door.')
            return 'Back'

    def south(self):
        self.status()
        print('The Southern region is filled with poisonous air, \nyour hero had taken damage '
              'but managed to flee back to the former region. - 5 health')
        self.health -= 5
        self.status()
        return 'Back'

    def west(self):
	### KB: Dictionary to make choice and printing easier
        horses = {"1":'Brown Bay Horse', "2":'Dark Bay Horse', "3":'White Bay Horse'}  
        self.status()
        print('You have encountered three horses in the western region')
		
        while True:
            do = input('What would you like to do?\n\n1. Feed 2. Leave ')
			
            if do == '1':
                for key in horses: 
                    print(key, " - ", horses[key]) 
                horse_num = input('Which horse would you like to feed?\n\n')
				
                if horse_num == "1": 
                    print('\nYou have angered the horse, the horse attacked you and you have lost 5 health')
                    self.health -= 5
                    self.status()
                    return 'Back'
					
                elif horse_num == "2":
			### KB: Check if there is something in the inventory
                    if self.inventory: 
                        print("You find this in your bag:") 
                        print(self.inventory)
                        feed = input('What would you like to feed?\n') 
                    
                        if feed.lower() == "pomegranate": 
						
				### KB: Check if player has TWO pomegranates
                            if self.inventory.count("pomegranate") == 2: 
                                many = input('How many would you like to feed? 1 or 2 ')
						
                                if many == '1':
                                    print('Wrong! The horse does not just eat one! -3 health')
                                    self.health -= 3
                                    self.status()
                                    return 'Back'
							
                                elif many == '2':
                                    print('\nThe Dark Bay Horse is satisfied and now it is on your side!')
                                    self.check_list.append('Dark Bay Horse')
                                    self.inventory.remove("pomegranate")
                                    self.inventory.remove("pomegranate") 					
                                    return 'Back', self.check_list
							
                                else: 
                                    print("Sorry, that's not a valid choice!\n") 
                            else: 
                                print("You don't have enough pomegranates for the Dark Bay Horse! Oh no!! It is getting angry and attacks you! \n Maybe you should try to play the game again?\n") 
                                for i in range(0, 5):
                                    time.sleep(0.5)
                                    print('. ', end='')
                                return "Bad" 
							
                        elif feed.lower() == "rosemary":
                            print('You chose the wrong answer. -3 health')
                            self.health -= 3
                            self.status()
                            return 'Back'
                        else: 
                            print("Sorry, that's not a valid choice!\n") 
							
			### KB: If hero has nothing in his inventory return bad ending 
                    else: 
                        print("You look in your bag and realize... You don't have anything to feed! Oh no!! Maybe you should try to play the game again?\n") 
                        print("Suddenly, you just faint...\n") 
                        for i in range(0, 5):
                            time.sleep(0.5)
                            print('. ', end='')
                        return "Bad" 
						
                elif horse_num == "3":
                    print('\nYou have angered a unicorn! The horse attacks you and you lose 5 health\n')
                    print('Critical! 5 more damage by the unicorn.')
                    self.health -= 10
                    self.status()
                    return 'Back'
		### KB: Added else-statements to catch invalid input	
                else: 
                    print("That's not a valid choice, please try again!\n")
				
            elif do == '2':
                print('You returned to the hidden door.')
                return 'Back'
				
            else:
                print('Only choose between 1(Feed) or 2(Leave)')
                continue


    def east(self):
	### KB: Basically the same as in west scenario here 
        goats = {"1":'The Goat', "2":'The Ibex', "3":"The Sheep"}
        self.status()
        print('You have encountered three animals in the eastern region')
		
        while True:
            do = input('What would you like to do?\n\n1. Feed 2. Leave ')
			
            if do == '1':
                for key in goats: 
                    print(key, " - ", goats[key]) 
                goat_num = input('Which animal do you like to feed?\n\n')
				
                if goat_num == '1':
                    print('\nYou have angered the goat, the goat attacked you and you have lost 5 health')
                    self.health -= 5
                    self.status()
                    return 'Back'
					
                elif goat_num == '2':
                    if self.inventory: 
                        print("You find this in your bag:") 
                        print(self.inventory)
                        feed = input('What would you like to feed?\n') 

                        if feed.lower() == "rosemary":
                            many = input('How many would you like to feed? 1 or 2 ')
						
                            if many == '2':
                                print('Wrong! -3 health')
                                self.health -= 3
                                self.status()
                                return 'Back'
							
                            elif many == '1':
                                print('The ibex is satisfied, and now it is on your side!')
                                self.check_list.append('The Ibex')
                                self.inventory.remove("rosemary")
                                return 'Back', self.check_list

                            else: 
                                print("Sorry, that's not a valid choice!\n") 
							
                        elif feed == '1':
                            print('You chose the wrong answer. -3 health')
                            self.health -= 3
                            self.status()
                            return 'Back'

                        else: 
                            print("Sorry, that's not a valid choice!\n") 
								
                    else: 
                        print("You look in your bag and realize... You don't have anything to feed! Oh no!! Maybe you should try to play the game again?\n") 
                        print("Suddenly, you just faint...\n") 
                        for i in range(0, 5):
                            time.sleep(0.5)
                            print('. ', end='')
                        return "Bad" 
						
                elif goat_num == '3':
                    print('\nYou have angered the sheep, the sheep attacked you and you have lost 5 health\n')
                    self.health -= 5
                    self.status()
                    return 'Back'

                else: 
                    print("Sorry, that's not a valid choice!\n") 
					
            elif do == '2':
                print('You returned to the hidden door.')
                return 'Back'
				
            else:
                print('Only choose between 1(Feed) or 2(Leave)')
                continue


# Joobin for Game Structure Part
class Game(object):
	intro_msgs = """
Our hero is looking to pass through a hidden door way to retrieve an
an old object of great value and power.  She has found a sort of
Rosetta stone at the side of a mountain which has the following
message inscribed on it in three languages."""
	beginning_msgs = "Now your hero starts her final adventure. Press Enter to proceed."
	hints = []
	correct_hints = [""]
	scenario = Scenario(hero.health)
	ending = ''

	# Haocheng Ma for Maps

	map = ["""
        N
      
        O
     W OXO E
        O
        
        S
    """, """
        N
      
        X
     W OOO E
        O
        
        S
    """, """
        N
      
        O
     W OOO E
        X
        
        S
    """, """
        N
      
        O
     W XOO E
        O
        
        S
    """, """
        N
      
        O
     W OOX E
        O
        
        S
	"""
	]

	# Joobin Youn

	def __init__(self):
		self.intro()
		proceed = input(self.beginning_msgs)
		if proceed == '' or proceed != '':
			self.gathering()
			self.gathering_ceremony()
			self.get_health_point(hero.health) # This needs an actual "health" variable to collect it from the last mini game, not 100
			self.scenario.health = self.health
			self.get_inventory(hero.inventory)
			self.moving_place('Mountain', 'Hidden Door')
			self.map_explanation()
			while self.health > 0:
				region = self.show_map()
				self.scenario.health = self.health
				if region == ('N' or 'n'):
					result = self.scenario.north()
					if result == 'Back':
						self.health = self.scenario.health
						continue
					elif result == 'Happy':
						self.ending = 'happy'
						break
				elif region == ('S' or 's'):
					result = self.scenario.south()
					if result == 'Back':
						self.health = self.scenario.health
						continue
				elif region == ('W' or 'w'):
					result = self.scenario.west()
					if result == 'Back':
						self.health = self.scenario.health
						continue
			### KB: Added this to terminate the game if hero has nothing in his inventory	
					elif result == "Bad": 
						self.ending = "bad" 
						break 
				elif region == ('E' or 'e'):
					result = self.scenario.east()
					if result == 'Back':
						self.health = self.scenario.health
						continue
			### KB: Added this to terminate the game if hero has nothing in his inventory
					elif result == "Bad": 
						self.ending = "bad" 
						break
			if self.health <= 0:
				self.ending = 'bad'

			if self.ending == 'happy':
				self.happy_ending()
			elif self.ending == 'bad':
				self.bad_ending()
		else:
			exit()

	def intro(self):
		print(self.intro_msgs)

	def gathering(self):
		self.hints.append("Feed the ibex rosemary.")
		self.hints.append("Give the dark bay horse two pomegranates.")

	def gathering_ceremony(self):
		print('')
		print('\n******* The Last Journey begins! *******')
	
    # Haocheng Ma

	def get_health_point(self, health):
		# This function is for importing health points from other team
		self.health = health

	def get_inventory(self, inventory):
		# This function is for importing health points from other team
		self.inventory = inventory

	def map_explanation(self):
		print("\nSo here is the map, there are four unknown regions you could explore. \nThe X is the place "
			"you are currently at, and the O marks the other regions you could go.")

    # Joobin Youn

	def moving_place(self, depart, dest):
		print('\nCame out of the', depart, 'to the region of the', dest)
		for i in range(0, 5):
			time.sleep(0.5)
			print('. ', end='')

	def show_map(self):
		print(self.map[0])
		while True:
			choice = input('Which way do you wanna go? press N, S, W, E. Quit for \'q\'.\n')
			if choice.capitalize() == ('N' or 'n'):
				print(self.map[1])
			elif choice.capitalize() == ('S' or 's'):
				print(self.map[2])
			elif choice.capitalize() == ('W' or 'w'):
				print(self.map[3])
			elif choice.capitalize() == ('E' or 'e'):
				print(self.map[4])
			elif choice.capitalize() == ('Q'):
				print('You gave up')
				print('--- The end of Game ---')
				exit(1)
			else:
				print('\nYou took the wrong path. Just enter n, s, w, e.\n')
				continue
			return choice.capitalize()

	def happy_ending(self):
		print('Door opened! You found the crown, the ancient object of powers!')
		print("""
         *
       *-|-*
       ..*.. 
     *"*****"*
    \" \"\"\"\"\"\"\" \"
    \*********/            
    (((((0)))))""")
		print('\nNow with the crown, the powers come, and invisible treasures could be seen all \naround! Brave hero, now roam around. Claim thy riches thou deserve!')
		input('You venture inside to collect the riches...')
		
		import CaveRoomBonus
		input("\nPress the enter key to exit.")

	def bad_ending(self):
		print('OMG. Your health is below 0. Grim Reaper appeared!')
		print("""
            *********
           *************
          *****     *****
         ***           ***
        ***             ***
        **    0     0    **
        **               **                  ____
        ***             ***             //////////
        ****           ****        ///////////////  
        *****         *****    ///////////////////
        ******       ******/////////         |  |
      *********     ****//////               |  |
   *************   **/////*****              |  |
  *************** **///***********          *|  |*
 ************************************    ****| <=>*
*********************************************|<===>* 
*********************************************| <==>*
***************************** ***************| <=>*
******************************* *************|  |*
********************************** **********|  |*  
*********************************** *********|  |""")
		print("\nHis sharp sickle cut you. You're bleeding.")
		self.health -= 70
		print("\nYou died.")
		print('\n--- The End of the Game ---')
		input("\n\nPress the enter key to exit.")

if __name__ == '__main__':

	game = Game()
	
f.close()