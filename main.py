import random, pickle, os, colorama
from Text_RPG_Food import *
from dictionaries import *
from Text_RPG_Enemy import *
from Text_RPG_Armour import *
from colorama import Back, Fore, Style
import generator
from math import sqrt

#create time.txt and inventory.dat and stats.dat
f = open('time.txt', 'a')
f.close()
del f
p = open('inventory.dat', 'ab')
p.close()
del p
p = open('stats.dat', 'ab')
p.close()
del p


def askYN(question):
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response


defaultItems = (TrustyDagger, Bread, Bread, Bread, Bread, Bread, Fists,
                ClothArmour)
cDict = {
    'green': Fore.GREEN,
    'cyan': Fore.CYAN,
    'red': Fore.RED,
    'blue': Fore.BLUE,
    'magenta': Fore.MAGENTA,
    'yellow': Fore.YELLOW,
    'reset': Style.RESET_ALL,
    'bright': Style.BRIGHT,
    'bRed': Back.RED,
    'black': Fore.BLACK,
    'bGreen': Back.GREEN
}
""" To do list
Items needed:
1: Health O
2: Inventory list O
3: Current weapon variable O
4: inventory altering functions O
5: saving the inventory with pickle O
6: name and name changer O
7: armor percent X implement l8r
8: skills (dodge, health regen, repairing, etc.) X implement l8r
9: attack function O
10: Weapon selection O
11: gold variable O
12: inventory displayer O
13: add __str__ function not needed currently
14: Save and load stats O
15: Create the GAME and GAMEPLAY O
16: bug: stackable item number is deleted between saves (fixed)
17: implement escape failed message (done)
"""


#player class
class Player(object):

    currentHealth = None
    maxHealth = 100

    currentWeapon = None

    currentArmour = None

    inventory = []
    stackInventory = {}  #data for storing stackable item amounts

    gold = 0

    playerName = ''

    currentFloor = 1
    floorList = []

    playerLocation = [0, 0]

    def displayInventory(self, inventoryList=inventory):  #function for displaying the inventory
        print(cDict['reset'], end='')
        print(self.playerName + '\'s inventory: ')
        i = 1
        for item in inventoryList:
            if item.quality == 0 or item.quality == 1:
                print(cDict['reset'], end='')
            elif item.quality == 2:
                print(cDict['cyan'], end='')
            elif item.quality == 3:
                print(cDict['magenta'], end='')
            elif item.quality == 4:
                print(cDict['yellow'], end='')
            print(str(i) + ': ', end='')
            if not item.isStackable:
                print(item)
                i += 1
            else:
                placeholder = item()
                print(repr(placeholder) + " - Amount: " + str(self.stackInventory[item]))
                i += 1
        print(cDict['reset'], end='')

    def inventoryAdd(self, item):  #Add an item to the player's inventory
        try:
            if item.isStackable:
                if item in self.inventory:
                    self.stackInventory[item] += 1
                else:
                    self.inventory.append(item)
                    self.stackInventory[item] += 1
            else:
                self.inventory.append(item())
        except:
            print('Something went wrong while adding to the inventory!')

    def inventoryRemove(self,
                        itemNum):  #delete an item from the player's inventory
        if self.inventory[itemNum].isStackable:
            self.stackInventory[self.inventory[itemNum]] -= 1
            if self.stackInventory[self.inventory[itemNum]] <= 0:
                self.inventory.remove(self.inventory[itemNum])
        else:
            self.inventory.remove(self.inventory[itemNum])

    def saveInventory(
            self,
            inventoryList):  #Save the inventory to the inventory.dat file
        print('Saving Inventory...')
        pfile = open('inventory.dat', 'wb')
        pickle.dump(inventoryList, pfile)
        pfile.close()
        del pfile
        sfile = open("stackables.dat", 'wb')
        pickle.dump(self.stackInventory, sfile)
        sfile.close()
        del sfile
        print('Inventory Saved\n')

    def loadInventory(self):  #Load the inventory from the inventory.dat file
        print(cDict['blue'] + 'Loading Inventory...')
        pfile = open('inventory.dat', 'rb')
        inv = pickle.load(pfile)
        pfile.close()
        sfile = open('stackables.dat', 'rb')
        self.stackInventory = pickle.load(sfile)
        sfile.close()
        print('Inventory Loaded\n' + cDict['reset'])
        del pfile
        del sfile
        return inv

    #check if its the first time playing
    def firstTimeManager(self):
        file = open('time.txt', 'r')
        line = file.readline()
        file.close()
        if line == '' or line == 'True':
            file = open('time.txt', 'w')
            file.write('False')
            file.close()
            return True
        elif line == 'False':
            file = open('time.txt', 'w')
            file.write('False')
            file.close()
            return False
        else:
            print('Hmm... Something\'s wrong with the file time.txt')
        del file

    def setInventory(self, invList, firstVar,
                     defaultItems):  #load in player inventory
        if firstVar == True:
            print('Loading inventory with default starting items')
            for item in defaultItems:
                self.inventoryAdd(item)
            self.saveInventory(invList)
        if firstVar == False:
            self.inventory = self.loadInventory()
            None

    def loadStats(self):  #Load player stats from stats.dat
        print(cDict['blue'] + 'Loading Stats...')
        pfile = open('stats.dat', 'rb')
        self.currentHealth = pickle.load(pfile)
        self.gold = pickle.load(pfile)
        self.playerName = pickle.load(pfile)
        self.currentWeapon = self.inventory[pickle.load(pfile)]
        self.currentFloor = pickle.load(pfile)
        self.floorList = pickle.load(pfile)
        self.currentArmour = self.inventory[pickle.load(pfile)]
        pfile.close()
        print('Stats Loaded\n' + cDict['reset'])
        del pfile
        #return currentHealth, gold, playerName, currentWeapon

    def saveStats(self):  #Save player stats to stats.dat
        print('Saving Stats')
        pfile = open('stats.dat', 'wb')
        pickle.dump(self.currentHealth, pfile)
        pickle.dump(self.gold, pfile)
        pickle.dump(self.playerName, pfile)
        pickle.dump(self.inventory.index(self.currentWeapon), pfile)
        pickle.dump(self.currentFloor, pfile)
        pickle.dump(self.floorList, pfile)
        pickle.dump(self.inventory.index(self.currentArmour), pfile)
        pfile.close()
        print('Stats Saved\n')
        del pfile

    def setStats(self, firstVar):  #set the player stats
        if firstVar:
            print('Loading default starting stats')
            self.currentHealth = self.maxHealth
            self.gold = 75
            self.selectWeapon()
            self.selectArmour()
            self.floorList.append(dungeon.createFloor(self.currentFloor))
            self.saveStats()
        else:
            self.loadStats()

    def setName(self):  #set the player name
        name = ''
        while name == '':
            name = input('What do you want to call yourself? ')
        self.playerName = name

    def displayStats(self):  #Display player stats
        print(cDict['yellow'], end='')
        print(self.playerName + '\'s stats: ')
        print(f'Health: {str(self.currentHealth)}/{str(self.maxHealth)}')
        print('Gold: ' + str(self.gold))
        print('Weapon in use is ' + self.currentWeapon.name)
        print('Armour in use is ' + self.currentArmour.name)
        print()
        print('Current Floor is: ' + str(self.currentFloor))
        print()
        self.displayInventory(self.inventory)
        print('\n')

    def eat(self):  #allow the player to eat and heal
        if self.currentHealth >= self.maxHealth:
            print("Your health is full! You can't eat anything!")
            return 0
        print("Your current health is: " + str(self.currentHealth) + '/' +
              str(self.maxHealth))
        print('What to eat?')
        self.displayInventory(self.inventory)
        while True:
            print('Use 0 to cancel')

            try:
                choiceNum = int(input('Choice  ['))
                if choiceNum == 0:
                    return 0
                choiceNum -= 1
                choice = self.inventory[choiceNum]
                break
            except:
                print("Invalid number!")
        selected = False
        for i in foodDictionary:
            if choice.name == i.name:
                print('The item you chose exists as a food item!')
                print('Your choice exists in your inventory!')
                print('Eating ' + choice.name + '\n')
                self.currentHealth += choice.healthRegen
                if self.currentHealth > self.maxHealth:
                    self.currentHealth = self.maxHealth
                self.inventoryRemove(choiceNum)
                if self.currentHealth < 1:
                    self.death()
                #self.saveInventory(self.inventory)
                #self.saveStats()
                selected = True
                break
        if not selected:
            print('The item you chose does not exist, or is not a food item')
        input(cDict['bGreen'] + cDict['black'] + cDict['bright'] +
              'Press Enter To Continue' + cDict['reset'])
        os.system('cls||clear')

    def selectWeapon(self):  #select player weapon for fighting
        selected = False
        print('What weapon to use?')
        self.displayInventory(self.inventory)
        while True:
            try:
                choice = int(input('Choice  ['))
                choice = self.inventory[choice - 1]
                break
            except:
                print("Invalid number!")
        for i in weaponDictionary:
            if choice.name == i.name:
                print('The item you chose exists as a weapon!')
                print(choice)
                print('Your choice exists in your inventory!')
                print('Equipping ' + choice.name + '\n')
                self.currentWeapon = choice
                #self.saveStats()
                selected = True
                break
        if not selected:
            print('The item you chose does not exist, or is not a weapon')
            print('Defaulting to fists')
            for i in self.inventory:
                if i.name == "Fists":
                    self.currentWeapon = i
                    break
            #self.saveStats()
        input(cDict['bGreen'] + cDict['black'] + cDict['bright'] +
              'Press Enter To Continue' + cDict['reset'])
        os.system('cls||clear')

    def selectArmour(self):  #select player armour for defense
        selected = False
        print('What armour to use?')
        self.displayInventory(self.inventory)
        while True:
            try:
                choice = int(input('Choice  ['))
                choice = self.inventory[choice - 1]
                break
            except:
                print("Invalid number!")
        for i in armourDictionary:
            if choice.name == i.name:
                print('The item you chose exists as a weapon!')
                print(choice)
                print('Your choice exists in your inventory!')
                print('Equipping ' + choice.name + '\n')
                self.currentArmour = choice
                #self.saveStats()
                selected = True
                break
        if not selected:
            print('The item you chose does not exist, or is not a weapon')
            print('Defaulting to cloth clothes')
            for i in self.inventory:
                if i.name == "Cloth Clothes":
                    self.currentArmour = i
                    break
            #self.saveStats()
        input(cDict['bGreen'] + cDict['black'] + cDict['bright'] +
              'Press Enter To Continue' + cDict['reset'])
        os.system('cls||clear')

    def weaponDurabilityDecrease(self):  #cause damage to the weapon durability
        self.currentWeapon.durability -= self.currentWeapon.durabilityDecrease
        if self.currentWeapon.durability <= 0:
            print('Your ' + self.currentWeapon.name + ' broke!')
            print('You must now select a new weapon')
            self.inventoryRemove(self.inventory.index(self.currentWeapon))
            self.currentWeapon.durability = 100
            self.selectWeapon()
            #self.saveInventory(self.inventory)
    def armourDurabilityDecrease(self):
        self.currentArmour.durability -= self.currentArmour.durabilityDecrease
        if self.currentArmour.durability <= 0:
            print('Your ' + self.currentArmour.name + ' broke!')
            print('You must now equip some new armour')
            self.inventoryRemove(self.inventory.index(self.currentArmour))
            self.currentArmour.durability = 100
            self.selectArmour()

    def attack(self, enemy):
        damage = random.randint(self.currentWeapon.damage[0],
                                self.currentWeapon.damage[1])
        enemy.currentHealth -= damage
        self.weaponDurabilityDecrease()
        print(cDict['magenta'], end='')
        print(f"You dealt {str(damage)} to {enemy.name}!")
        print(f"{enemy.name} has {str(enemy.currentHealth)} health left." +
              cDict['reset'])

    def damage(self, damage, checkForDeath=True):
        if damage > self.currentArmour.maxProtection:
            self.currentHealth -= damage
        else:
            self.currentHealth -= round(damage * 1 -
                                        (self.currentArmour.defense / 10))
            self.armourDurabilityDecrease()
        print(cDict['red'], end='')
        print("\nYou took " + str(damage) + " damage!")
        print("You now have " + str(self.currentHealth) + " Health\n")
        print(cDict['reset'], end='')
        if checkForDeath and self.currentHealth <= 0:
            self.death()

    def death(self):
        #goes back to last save
        os.system('clear||cls')
        print(cDict['red'], end='')
        print(r'''
_____.___.              ________  .__           .___
\__  |   | ____  __ __  \______ \ |__| ____   __| _/
 /   |   |/  _ \|  |  \  |    |  \|  |/ __ \ / __ | 
 \____   (  <_> )  |  /  |    `   \  \  ___// /_/ | 
 / ______|\____/|____/  /_______  /__|\___  >____ | 
 \/                             \/        \/     \/ ''')
        print("Going back to last save point...\n")
        print(cDict['reset'], end='')
        self.inventory = self.loadInventory()
        self.loadStats()
        self.playerLocation = [0, 0]
        self.gold = self.gold // 2

    def sortInventory(self, choice):
        if choice == 1:  #default sorting

            def myFunc(e):
                return e.quality

            self.inventory.sort(
                key=myFunc, reverse=True)  #sorts by quality descending

            def myFunc(e):
                return e.type

            self.inventory.sort(
                key=myFunc, reverse=True)  #sorts by type descending

    def __init__(self, newGame):
        firstTime = self.firstTimeManager()
        if newGame:
            firstTime = True
        if firstTime == True:
            #select name
            self.setName()
        for item in foodDictionary:
            self.stackInventory[item] = 0
        self.setInventory(self.inventory, firstTime, defaultItems)
        self.setStats(firstTime)
        self.displayStats()


class Game(object):
    def mainMenu(self):
        colorama.init()
        print('Welcome to:' + cDict['red'], end='')
        print(r'''
___________              __ ____________________  ________ 
\__    ___/___ ___  ____/  |\______   \______   \/  _____/ 
  |    |_/ __ \\  \/  /\   __\       _/|     ___/   \  ___ 
  |    |\  ___/ >    <  |  | |    |   \|    |   \    \_\  \
  |____| \___  >__/\_ \ |__| |____|_  /|____|    \______  /
             \/      \/             \/                  \/  A Game By Slim Squad'''
              )
        print(cDict['green'], end='')
        print('''
        1-Create new game
        2-Continue game
        ''')
        print(cDict['reset'], end='')
        choice_status = False
        choices = (1, 2)
        choice = 0
        while not choice_status and choice not in choices:
            try:
                choice = int(input('Choice: '))
            except:
                print('Invalid choice')
        if choice == 1:
            os.system('cls||clear')
            player = Player(True)
            self.intro(player)
            input(cDict['bGreen'] + cDict['black'] + cDict['bright'] +
                  'Press Enter To Continue' + cDict['reset'])
            os.system('cls||clear')
        elif choice == 2:
            #try:
            #os.system('clear||cls')
            player = Player(False)
            self.pause(player)
            #except:
            #    print('There was an error! Maybe there isn\'t a saved game?')

    def intro(self, player):
        print(
            "You are exploring a dark dungeon that contains many wild and unknown species of animals.\nApparently there are also some dangerous mutants..."
        )
        print("How many floors can you explore before you die...")
        print("GOOD LUCK!")
        print()
        self.pause(player)

    def pause(self, player):
        print("Hey, have a break!")
        while True:
            floor = player.floorList[player.currentFloor - 1]
            room = floor[player.playerLocation[1]][player.playerLocation[0]]
            print("What do you want to do?")
            print(cDict['green'], end='')
            #eat, select weapon, save game, continue, and trade if available
            choices = ['1', '2', '3', '4', '5', '6', '7']
            print("""
        1 - Eat
        2 - Select Weapon
        3 - View Stats and Inventory
        4 - Save Game
        5 - Continue
        6 - Sort Inventory
        7 - Equip Armour""")
            if room.content == 'T':
                print("        8 - Talk to the Trader\n")
                choices.append('8')
            else:
                print()
            print(cDict['reset'], end='')
            choice = input("Choice: ")
            os.system('cls||clear')
            if choice in choices:
                if choice == '1':
                    player.eat()
                elif choice == '2':
                    player.selectWeapon()
                elif choice == '3':
                    player.displayStats()
                elif choice == '4':
                    player.saveInventory(player.inventory)
                    player.saveStats()
                elif choice == '5':
                    self.floorMovement(player)
                elif choice == '6':
                    print("Sorting Inventory")
                    player.sortInventory(1)
                    print("Inventory Sorted")
                elif choice == '7':
                    player.selectArmour()
                elif choice == '8':
                    room.trader.traderInteraction(player)
            else:
                print("Invalid number!")

    def floorMovement(self, player):
        choice = []
        floor = player.floorList[player.currentFloor - 1]
        generator.generator.displayMap(floor, player.playerLocation)
        directions = ['n', 'e', 's', 'w', 'u', 'd']
        DIRECTIONS = ['n', 'e', 's', 'w', 'u', 'd']
        print(f'Current Player Location: {player.playerLocation}')
        print(
            f'Content of Current Location is {floor[player.playerLocation[1]][player.playerLocation[0]].content}'
        )
        for i in range(4):
            if floor[player.playerLocation[1]][
                    player.playerLocation[0]].connections[
                        i] == False:  #since floor coords are (y,x) and player coords are (x,y), we flip them around
                directions.remove(DIRECTIONS[i])
        if floor[player.playerLocation[1]][player.
                                           playerLocation[0]].content != 'D':
            directions.remove('d')
        if floor[player.playerLocation[1]][player.playerLocation[
                0]].content != 'U' or player.currentFloor == 1:
            directions.remove('u')
        while choice not in directions:
            print("Which way would you like to go?")
            if 'n' in directions:
                print("N - Go to the room to the North")
            if 'e' in directions:
                print("E - Go to the room to the East")
            if 's' in directions:
                print("S - Go to the room to the South")
            if 'w' in directions:
                print("W - Go to the room to the West")
            if 'u' in directions:
                print("U - Go up the staircase")
            if 'd' in directions:
                print("D - Go down the staircase")
            choice = input("Which direction to go? ").lower()
        if choice == 'n':
            player.playerLocation[1] -= 1  #decrease y coord
        elif choice == 'e':
            player.playerLocation[0] += 1  #increase x coord
        elif choice == 's':
            player.playerLocation[1] += 1  #increase y coord
        elif choice == 'w':
            player.playerLocation[0] -= 1  #decrease x coord
        elif choice == 'u':
            player.playerLocation = [0, 0]
            player.currentFloor -= 1
            print("You went back one floor")
            print("Your current floor is now " + str(player.currentFloor))
        elif choice == 'd':
            player.playerLocation = [0, 0]
            if player.currentFloor == len(player.floorList):
                player.currentFloor += 1
                player.floorList.append(
                    dungeon.createFloor(player.currentFloor))
            else:
                player.currentFloor += 1
            print("You went down one floor")
            print("Your current floor is now " + str(player.currentFloor))
            player.saveStats()
            player.saveInventory(player.inventory)
        print(f'New Player Location: {player.playerLocation}')
        print(
            f'Content of New Location is {floor[player.playerLocation[1]][player.playerLocation[0]].content}'
        )
        input(cDict['bGreen'] + cDict['black'] + cDict['bright'] +
              'Press Enter To Continue' + cDict['reset'])
        os.system('cls||clear')
        self.floorInteraction(
            floor[player.playerLocation[1]][player.playerLocation[0]], player)

    def floorInteraction(self, room, player):
        print("You enter the room...")
        floor = player.floorList[player.currentFloor - 1]
        room = floor[player.playerLocation[1]][player.playerLocation[0]]
        if not room.explored:
            if room.content == 'F':
                escape = self.battle(
                    player,
                    room.enemy)  #make it if escaped, room is still unexplored
                if escape != 1:
                    room.explored = True
            elif room.content == 'L':
                print("You found a loot chest!")
                print("You open the loot chest...")
                for item in room.loot:
                    print(f"You received {item.name} from the chest")
                    player.inventoryAdd(item)
                room.explored = True
            elif room.content == 'T':
                print("You meet a trader!")
                print(f"They are a {room.trader.type.capitalize()}")
                room.explored = True
            elif room.content == 'U' and player.currentFloor != 1:
                print("You find a staircase going upwards.")
                room.explored = True
            elif room.content == 'D':
                print("You find a staircase going downwards.")
                room.explored = True
        else:
            if room.content == 'F':
                print('A defeated enemy lays on the ground.')
            elif room.content == 'L':
                print('There is an empty chest.')
            elif room.content == 'T':
                print('You meet a trader')
            elif room.content == 'U' and player.currentFloor != 1:
                print("You find a staircase going upwards.")
            elif room.content == 'D':
                print("You find a staircase going downwards.")
            else:
                print("It's just an empty room.")

    def encounter(self, player, enemy):
        eatCount = 0
        hasAttacked = False
        choice = ""
        choices = ['1', '2', '3', '4', '5', '6', '7']
        while not hasAttacked:
            print(enemy)
            print("What do you do?")
            print(cDict['green'] + """
        1 - Attack the Enemy
        2 - Attempt to Escape
        3 - Eat
        4 - Select Weapon
        5 - View Stats and Inventory
        6 - Sort Inventory
        7 - Equip armour
            """ + cDict['reset'])
            choice = ""
            while choice not in choices:
                choice = input("Choice: ")
                if choice in choices:
                    os.system('cls||clear')
                    if choice == '1':
                        player.attack(enemy)
                        hasAttacked = True
                    elif choice == '2':
                        return random.randint(1, 3)
                        hasAttacked = True
                    elif choice == '3':
                        if eatCount <= 5:
                            player.eat()
                            eatCount += 1
                        else:
                            print("You are full! You can't eat!")
                    elif choice == '4':
                        player.selectWeapon()
                    elif choice == '5':
                        player.displayStats()
                    elif choice == '6':
                        print("Sorting Inventory")
                        player.sortInventory(1)
                        print("Inventory Sorted")
                    elif choice == '7':
                        player.selectArmour()
                else:
                    print("Invalid number!")

    def battle(self, player, enemy):
        localEnemy = enemy()
        print("You face a:")
        while localEnemy.currentHealth > 0 and player.currentHealth > 0:
            escape = self.encounter(player, localEnemy)
            if escape == 1:
                print("You escaped!")
                break
            elif escape in [2, 3]:
                print("You failed to escape!")
            if localEnemy.currentHealth > 0:
                player.damage(
                    random.randint(enemy.damage[0], enemy.damage[1]), False)
        if player.currentHealth <= 0:
            player.death()
            del localEnemy
        elif localEnemy.currentHealth <= 0:
            print(f"You defeated the {localEnemy.name}\n")
            gold = random.randint(localEnemy.gold[0], localEnemy.gold[1])
            print("You received " + str(gold) + " Gold")
            player.gold += gold
            del localEnemy
            player.displayStats()
        return escape

    def __init__(self):
        self.mainMenu()


class DungeonCreator(object):
    TYPES = {
        'U': 1,  #stairs up
        'D': 1,  #stairs down
        'F': 6,  #fight
        'L': 3,  #loot
        'T': 1
    }  #trader

    def createFloor(self, floor=1):
        difficulty = floor // 10 + 1
        baseRooms = 10
        extraRooms = 2
        currentRooms = baseRooms * difficulty + extraRooms
        ratio = (4, 3)
        currentRatio = self.findFloorSize(currentRooms * 2, ratio[0], ratio[1])
        #print(currentRatio)

        floorArray = generator.generator.generate(currentRatio, currentRooms)
        floorArray = generator.generator.createConnections(floorArray)
        floorArray = self.populateFloor(floorArray, floor)
        return floorArray

    def populateFloor(self, array, floor=1):
        difficulty = floor // 10 + 1
        types = dict(self.TYPES)
        for key in types.keys():
            if key != 'U' and key != 'D':
                types[key] = types[key] * difficulty
        for i in array:
            for j in i:
                if array.index(i) == 0 and i.index(j) == 0:
                    j.content = 'U'
                    del types['U']
                else:
                    if j.content != 'n':
                        content = random.choice([*types.keys()])
                        j.content = content
                        types[content] -= 1
                        for key in [*types.keys()]:
                            if types[key] == 0:
                                del types[key]
                        if content == 'F':
                            eligibleEnemies = []
                            for enemy in enemyDictionary:
                                if floor >= enemy.level[
                                        0] and floor <= enemy.level[1]:
                                    eligibleEnemies.append(enemy)
                            if eligibleEnemies == []:
                                eligibleEnemies = enemyDictionary
                            j.enemy = random.choice(eligibleEnemies)
                        elif content == 'L':
                            eligibleFood = []
                            eligibleWeapon = []
                            foodQuality = random.choices([1, 2, 3, 4],
                                                         weights=(60, 25, 10,
                                                                  5),
                                                         k=1)
                            for item in foodDictionary:
                                if difficulty == item.level and foodQuality[
                                        0] == item.quality and item not in foodBlacklist:
                                    eligibleFood.append(item)
                            if eligibleFood == []:
                                eligibleFood = foodDictionary

                            weaponQuality = random.choices([1, 2, 3, 4],
                                                           weights=(60, 25, 10,
                                                                    5),
                                                           k=1)
                            if random.randint(1, 3) == 1:
                                for item in weaponDictionary + armourDictionary:
                                    if difficulty == item.level and weaponQuality[
                                            0] == item.quality:
                                        eligibleWeapon.append(item)
                                if eligibleWeapon == []:
                                    eligibleWeapon = weaponDictionary[
                                        1:] + armourDictionary[
                                            1:]  #do not include fists or cloth clothes

                            if eligibleWeapon != []:
                                j.loot = [
                                    random.choice(eligibleFood),
                                    random.choice(eligibleWeapon)
                                ]
                            else:
                                j.loot = [random.choice(eligibleFood)]

                        elif content == 'T':
                            j.trader = Trader(
                                random.choice(['grocer', 'blacksmith']), floor)
        return array

    def findFloorSize(
            self, a, d,
            e):  #find the factors, b and c, of a, in the ratio d and e
        b = round(d * sqrt(a / (d * e)))
        c = round(e * sqrt(a / (d * e)))
        return (b, c)


class Trader(object):
    type = ''
    sales = []
    floor = 0
    baseItem = None
    difficulty = 0

    def createSales(self):
        if self.type == 'grocer':
            #add the base item that the trader will sell
            if self.difficulty <= len(grocerBaseItems):
                self.baseItem = grocerBaseItems[self.difficulty - 1]
                self.sales.append(self.baseItem)
            else:
                self.baseItem = random.choice(grocerBaseItems)
                self.sales.append(self.baseItem)

            eligibleFood = []
            for item in foodDictionary:  #add common items to list choice
                if self.difficulty == item.level and item.quality == 1 and item != self.baseItem:
                    eligibleFood.append(item)
            for i in range(2):  #add 3 common items to sales
                if eligibleFood != []:
                    choice = random.choice(eligibleFood)
                    self.sales.append(choice)
                    eligibleFood.remove(choice)
                else:
                    break

            eligibleFood = []
            for item in foodDictionary:  #add rare items to list choice
                if self.difficulty == item.level and item.quality == 2 and item != self.baseItem:
                    eligibleFood.append(item)
            for i in range(random.randint(1, 2)):  #add 1 or 2 rare items
                if eligibleFood != []:
                    choice = random.choice(eligibleFood)
                    self.sales.append(choice)
                    eligibleFood.remove(choice)
                else:
                    break

            if random.randint(
                    1,
                    3) == 1:  #1/3 chance for trader to sell an epic food item
                eligibleFood = []
                for item in foodDictionary:  #add epic items to list choice
                    if self.difficulty == item.level and item.quality == 3 and item != self.baseItem:
                        eligibleFood.append(item)
                if eligibleFood != []:
                    choice = random.choice(eligibleFood)
                    self.sales.append(choice)
                    eligibleFood.remove(choice)

            if random.randint(
                    1, 4
            ) == 1:  #1/4 chance for trader to sell an legendary food item
                eligibleFood = []
                for item in foodDictionary:  #add legendary items to list choice
                    if self.difficulty == item.level and item.quality == 4 and item != self.baseItem:
                        eligibleFood.append(item)
                if eligibleFood != []:
                    choice = random.choice(eligibleFood)
                    self.sales.append(choice)
                    eligibleFood.remove(choice)
        if self.type == 'blacksmith':
            #add the base item that the trader will sell
            if self.difficulty <= len(blacksmithBaseItems):
                self.baseItem = blacksmithBaseItems[self.difficulty - 1]
                self.sales.append(self.baseItem)
            else:
                self.baseItem = random.choice(blacksmithBaseItems)
                self.sales.append(self.baseItem)

            eligibleWeapons = []
            for item in weaponDictionary:  #add common items to list choice
                if self.difficulty == item.level and item.quality == 1 and item != self.baseItem:
                    eligibleWeapons.append(item)
            for i in range(2):  #add 2 common items to sales
                if eligibleWeapons != []:
                    choice = random.choice(eligibleWeapons)
                    self.sales.append(choice)
                    eligibleWeapons.remove(choice)
                else:
                    break

            eligibleWeapons = []
            for item in weaponDictionary:  #add rare items to list choice
                if self.difficulty == item.level and item.quality == 2 and item != self.baseItem:
                    eligibleWeapons.append(item)
            for i in range(random.randint(1, 2)):  #add 1 or 2 rare items
                if eligibleWeapons != []:
                    choice = random.choice(eligibleWeapons)
                    self.sales.append(choice)
                    eligibleWeapons.remove(choice)
                else:
                    break

            if random.randint(
                    1,
                    3) == 1:  #1/3 chance for trader to sell an epic food item
                eligibleWeapons = []
                for item in weaponDictionary:  #add epic items to list choice
                    if self.difficulty == item.level and item.quality == 3 and item != self.baseItem:
                        eligibleWeapons.append(item)
                if eligibleWeapons != []:
                    choice = random.choice(eligibleWeapons)
                    self.sales.append(choice)
                    eligibleWeapons.remove(choice)

            if random.randint(
                    1, 4
            ) == 1:  #1/4 chance for trader to sell an legendary food item
                eligibleWeapons = []
                for item in weaponDictionary:  #add legendary items to list choice
                    if self.difficulty == item.level and item.quality == 4 and item != self.baseItem:
                        eligibleWeapons.append(item)
                if eligibleWeapons != []:
                    choice = random.choice(eligibleWeapons)
                    self.sales.append(choice)
                    eligibleWeapons.remove(choice)

    def displaySales(self):
        print(cDict['reset'], end='')
        print(f"{self.type.capitalize()}'s Stock:")
        i = 1
        for item in self.sales:
            if item.quality == 0 or item.quality == 1:
                print(cDict['reset'], end='')
            elif item.quality == 2:
                print(cDict['cyan'], end='')
            elif item.quality == 3:
                print(cDict['magenta'], end='')
            elif item.quality == 4:
                print(cDict['yellow'], end='')
            print(str(i) + ': ', end='')
            if item.type == 'food':
                print(item.name + ': Regenerates ' + str(item.healthRegen) +
                      ' Health | Cost: ' + str(item.cost) + ' Gold')
            elif item.type == 'weapon':
                print(item.name + ': Deals ' + str(item.damage) +
                      ' Damage | Cost: ' + str(item.cost) + ' Gold')
            i += 1
        print(cDict['reset'], end='')
    def displayPlayerSales(self, player):
        print(cDict['reset'], end='')
        i = 1
        for item in player.inventory:
            if item.quality == 0 or item.quality == 1:
                print(cDict['reset'], end='')
            elif item.quality == 2:
                print(cDict['cyan'], end='')
            elif item.quality == 3:
                print(cDict['magenta'], end='')
            elif item.quality == 4:
                print(cDict['yellow'], end='')
            print(str(i) + ': ', end='')
            if item.type == 'food':
                print(item.name + ': Regenerates ' + str(item.healthRegen) + ' Health | Sells for: ' + str(item.cost//2) + ' Gold' + ' | Amount: ' + str(player.stackInventory[item]))
            elif item.type == 'weapon':
                print(item.name + ': Deals ' + str(item.damage) + ' Damage | Sells for: ' + str(item.cost//2) + ' Gold')
            i += 1
        print(cDict['reset'], end='')

    def traderInteraction(self, player):
        while True:
            print("What do you want to do?")
            print(cDict['green'], end='')
            choices = ['0', '1', '2']
            print("\n        1 - Buy From the Trader's Stock")
            print("        2 - Sell your items to the Trader (not quite yet)")
            if self.type == 'blacksmith':
                choices.append('3')
                choices.append('4')
                print(
                    "        3 - Repair Your Weapon at the Blacksmith's Forge")
                print(
                    "        4 - Repair Your Armour at the Blacksmith's Forge")
            print()
            print(cDict['reset'], end='')
            choice = input("Choice (0 to exit): ")
            os.system('cls||clear')
            if choice in choices:
                if choice == '1':
                    print(f"You have {str(player.gold)} Gold")
                    self.displaySales()
                    try:
                        print('0 to cancel')
                        choice = int(input("What to buy? "))
                        if not choice == 0:
                            if not choice > len(self.sales):
                                item = self.sales[choice - 1]
                                if not item.cost > player.gold:
                                    player.gold -= item.cost
                                    player.inventoryAdd(item)
                                    print('You bought: ' + item.name)
                                else:
                                    print("You don't have enough gold!")
                            else:
                                print("Invalid Input!")
                    except:
                        print("Invalid Input!")
                elif choice == '2':
                    print(f"You have {str(player.gold)} Gold")
                    if self.type == "grocer":
                        print("You can sell food items to the grocer")
                        self.displayPlayerSales(player)
                        try:
                            print('0 to cancel')
                            choice = int(input("What to sell? "))
                            if not choice == 0:
                                if not choice > len(player.inventory):
                                    item = player.inventory[choice - 1]
                                    if item.type == 'food' and not item.quality == 0:
                                        player.gold += item.cost//2
                                        player.inventoryRemove(player.inventory.index(item))
                                        print('You sold: ' + item.name + ' for ' + str(item.cost//2) + ' Gold')
                                    else:
                                        print("You can't sell that!")
                                else:
                                    print("Invalid Input!")
                        except:
                            print("Invalid Input!")
                    elif self.type == "blacksmith":
                        print("You can sell weapons and armour to the blacksmith")
                        self.displayPlayerSales(player)
                        try:
                            print('0 to cancel')
                            choice = int(input("What to sell? "))
                            if not choice == 0:
                                if not choice > len(player.inventory):
                                    item = player.inventory[choice - 1]
                                    if (item.type == 'weapon' or item.type == 'armour') and not item.quality == 0:
                                        player.gold += item.cost//2
                                        player.inventoryRemove(player.inventory.index(item))
                                        print('You sold: ' + item.name + ' for ' + str(item.cost//2) + ' Gold')
                                    else:
                                        print("You can't sell that!")
                                else:
                                    print("Invalid Input!")
                        except:
                            print("Invalid Input!")
                elif choice == '3':
                    if player.currentWeapon.durability == 100:
                        print("Your weapon is not damaged! You cannot repair it!")
                    else:
                        print("Your currently equipped weapon is: ")
                        print(player.currentWeapon)
                        cost = 100 - player.currentWeapon.durability
                        print("It will cost " + str(cost) + " Gold to repair your weapon fully")
                        choice = askYN("Continue? [Y/N]: ")
                        if choice == 'y':
                            if not cost > player.gold:
                                print('"Very well", says the Blacksmith. "Hand it over so I can freshen it up"')
                                print("You give your weapon to the Blacksmith")
                                print("He sharpens it up on the stone and cleans it up with a cloth.")
                                player.gold -= cost
                                player.currentWeapon.durability = 100
                                print("Your weapon is now fully repaired!")
                            else:
                                print("You don't have enough gold!")
                elif choice == '4':
                    if player.currentArmour.durability == 100:
                        print("Your armour is not damaged! You cannot repair it!")
                    else:
                        print("Your currently equipped armour is: ")
                        print(player.currentArmour)
                        cost = 100 - player.currentArmour.durability
                        print("It will cost " + str(cost) +
                              " Gold to repair your armour fully")
                        choice = askYN("Continue? [Y/N]: ")
                        if choice == 'y':
                            if not cost > player.gold:
                                print('"Very well", says the Blacksmith. "Hand it over so I can fix it up"')
                                print("You take off your armour and hand it to the Blacksmith")
                                print("He whacks if a few times with a mallet to straighten out those annoying dents and adds reinforcements where needed. \nIt's not ideal, but it'll do.")
                                player.gold -= cost
                                player.currentArmour.durability = 100
                                print("Your armour is now fully repaired!")
                            else:
                                print("You don't have enough gold!")
                elif choice == '0':
                    break
            else:
                print("Invalid number!")

    def __init__(self, type, floor):
        self.sales = []
        self.type = type
        self.floor = floor
        self.difficulty = floor // 10 + 1
        self.createSales()


dungeon = DungeonCreator()
game = Game()
