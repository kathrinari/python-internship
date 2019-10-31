
# 	LAST LEVEL

# Haocheng Ma and Joobin Youn(Scenario Part)
class Scenario(object):
    def __init__(self, health):
        self.health = health

    horses = ['Dark Bay Horse', 'Brown Bay Horse', 'White Bay Horse']    goats = ['goat', 'ibex']
    feed = ['pomegranate', 'apple', 'rosemary']
    check_list = []

    def north(self):
        print('You have come to the Northern region!')
        print('Health: ', str(self.health))
        choice = input('What would you like to do?\n\n'
                       '1. Interact with the hidden door 2. Leave')
        if choice == '1':
            print('My Inventory List')
            if len(self.check_list) != 0:
                for item in self.check_list:
                    print('** '+ item + ' **')
            else:
                print('Your Inventory is Empty! Find something!')
            if ('The Ibex' in self.check_list) and ('Dark Bay Horse' in self.check_list):
                print('')
                print('\nWith the help of the Ibex and the Dark Bay Horse, '
                '\nyou have opened the Hidden Door! '
                '\nTherein you obtain the Object of Power and Value. '
                '\nVictory and Glory to you!')
                return 'Happy'
            else:
                print('\nNothing happened, maybe you should go out there and look for some help!')
                return 'Back'
        elif choice == '2':
            print('You are returned to the hidden door.')
            return 'Back'
        else:
            print('You are returned to the hidden door.')
            return 'Back'

    def south(self):
        print('Health: ', str(self.health))
        print('The Southern region is filled with poisonous air, \nyour hero had taken damage '
              'but managed to flee back to the former region. - 5 health')
        self.health -= 5
        return 'Back'

    def west(self):
        print('Health: ', str(self.health))
        print('You have encountered three horses in the western region')
        while True:
            do = input('What would you like to do?\n\n1. Feed 2. Leave')
            if do == '1':
                horse_num = input('Which horse do you like to feed?\n\n'
                                  '1. White Horse 2. Dark Bay Horse 3. The Unicorn\n')
                if horse_num == '1':
                    print('\nYou have angered the horse, the horse attacked you and you have lost 5 health')
                    self.health -= 5
                    return 'Back'
                elif horse_num == '2':
                    feed = input('What would you like to feed?\n'
                                 '1. Pomegranate 2. Rosemary\n')
                    if feed == '1':
                        many = input('How many would you like to feed? 1 or 2')
                        if many == '1':
                            print('Wrong! -3 health')
                            self.health -= 3
                            return 'Back'
                        elif many == '2':
                            print('\nThe Dark Bay Horse is satisfied and now it is on your side!')
                            self.check_list.append('Dark Bay Horse')
                            return 'Back', self.check_list
                    elif feed == '2':
                        print('You chose the wrong answer. -3 health')
                        self.health -= 3
                        return 'Back'
                elif horse_num == '3':
                    print('\nYou have angered the holy unicorn, the horse attacked you and you have lost 5 health\n')
                    print('Critical! 5 more damage by Unicorn.')
                    self.health -= 10
                    return 'Back'
            elif do == '2':
                print('You are returned to the hidden door.')
                return 'Back'
            else:
                print('Only choose between 1(Feed) or 2(Leave)')
                continue

    def east(self):
        print('Health: ', str(self.health))
        print('You have encountered three animals in the eastern region')
        while True:
            do = input('What would you like to do?\n\n1. Feed 2. Leave')
            if do == '1':
                horse_num = input('Which animal do you like to feed?\n\n'
                                  '1. The Goat 2. The Ibex 3. The Sheep\n')
                if horse_num == '1':
                    print('\nYou have angered the goat, the goat attacked you and you have lost 5 health')
                    self.health -= 5
                    return 'Back'
                elif horse_num == '2':
                    feed = input('What would you like to feed?\n'
                                 '1. Pomegranate 2. Rosemary\n')
                    if feed == '2':
                        many = input('How many would you like to feed? 1 or 2')
                        if many == '2':
                            print('Wrong! -3 health')
                            self.health -= 3
                            return 'Back'
                        elif many == '1':
                            print('The ibex is satisfied, and now it is on your side!')
                            self.check_list.append('The Ibex')
                            return 'Back', self.check_list
                    elif feed == '1':
                        print('You chose the wrong answer. -3 health')
                        self.health -= 3
                        return 'Back'
                elif horse_num == '3':
                    print('\nYou have angered the sheep, the sheep attacked you and you have lost 5 health\n')
                    self.health -= 5
                    return 'Back'
            elif do == '2':
                print('You are returned to the hidden door.')
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
	beginning_msgs = "Now your hero starts adventure. Press the enter to proceed."
	hero = Hero()
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

	def start(self):
		self.intro()
		self.hero.setting()
		proceed = input(self.beginning_msgs)
		if proceed == '' or proceed != '':
			self.gathering()
			self.gathering_ceremony()
			self.get_health_point(100) # This needs an actual "health" variable to collect it from the last mini game, not 100
			self.scenario.health = self.hero.health
			self.get_inventory(['rosemary', 'pomegranate'])
			self.moving_place('Mountain', 'Hidden Door')
			self.map_explanation()
			while self.hero.health > 0:
				region = self.show_map()
				self.scenario.health = self.hero.health
				if region == ('N' or 'n'):
					result = self.scenario.north()
					if result == 'Back':
						self.hero.health = self.scenario.health
						continue
					elif result == 'Happy':
						self.ending = 'happy'
						break
				elif region == ('S' or 's'):
					result = self.scenario.south()
					if result == 'Back':
						self.hero.health = self.scenario.health
						continue
				elif region == ('W' or 'w'):
					result = self.scenario.west()
					if result == 'Back':
						self.hero.health = self.scenario.health
						continue
				elif region == ('E' or 'e'):
					result = self.scenario.east()
					if result == 'Back':
						self.hero.health = self.scenario.health
						continue
			if self.hero.health <= 0:
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
		self.hero.health = health;

	def get_inventory(self, inventory):
		# This function is for importing health points from other team
		self.hero.inventory = inventory


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
			choice = input('Which way wanna go? press N, S, W, E. Quit for \'q\'.\n')
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
		print('Door Opened! You found the Crown, the ancient object of powers!')
		print("""
         *
       *-|-*
       ..*.. 
     *"*****"*
    \" \"\"\"\"\"\"\" \"
    \*********/            
    (((((0)))))""")
		print('Now with the crown, the powers come, and invisible treasures could be seen all \naround! Brave hero, now roam around. Claim thy riches thou deserve!')
		print('You venture inside to collect the riches...')
		
		caveRoom()
		input("\nPress the enter key to exit.")

	def bad_ending(self):
		print('OMG. Your health is below 0. Grim Reaper Appeared!')
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
		self.hero.health -= 70
		print("\nYou died.")
		print('\n--- The end of Game ---')
		input("\n\nPress the enter key to exit.")