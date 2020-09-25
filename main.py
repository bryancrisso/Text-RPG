import random, pickle, time
from Text_RPG_Food import *
from dictionaries import *




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

defaultItems = (TrustyDagger, Bread, Bread, Bread, Bread, Bread, Fists)


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
9: attack function X
10: Weapon selection O
11: gold variable O
12: inventory displayer O
13: add __str__ function not needed currently
14: Save and load stats O
15: Create the GAME and GAMEPLAY X
"""

#player class
class Player(object):

    currentHealth = None
    maxHealth = 100

    currentWeapon = None

    inventory = []

    gold = None

    playerName = ''

    def displayInventory(self, inventoryList = inventory): #function for displaying the inventory
        print(self.playerName + '\'s inventory: ')
        i = 1
        for item in inventoryList:
            print(str(i) + ': ', end = '')
            if not item.isStackable:
                print(item)
                i += 1
            else:
                placeholder = item()
                print(repr(placeholder) + " - Amount: " + str(item.amount))
                i += 1

    def inventoryAdd(self, item): #Add an item to the player's inventory
        try:
            if item.isStackable:
                if item in self.inventory:
                    self.inventory[self.inventory.index(item)].amount += 1
                else:
                    self.inventory.append(item)
                    self.inventory[self.inventory.index(item)].amount += 1
            else:
                self.inventory.append(item())
        except:
            print('Something went wrong while adding to the inventory!')

    def inventoryRemove(self, itemNum): #delete an item from the player's inventory
        if self.inventory[itemNum].isStackable:
            self.inventory[itemNum].amount -=1
            if self.inventory[itemNum].amount == 0:
                self.inventory.remove(self.inventory[itemNum])
        else:
            self.inventory.remove(self.inventory[itemNum])

    def saveInventory(self, inventoryList): #Save the inventory to the inventory.dat file
        print('Saving Inventory...')
        pfile = open('inventory.dat', 'wb')
        pickle.dump(inventoryList, pfile)
        pfile.close()
        print('Inventory Saved\n')
        del pfile

    def loadInventory(self): #Load the inventory from the inventory.dat file
        print('Loading Inventory...')
        pfile = open('inventory.dat', 'rb')
        inv = pickle.load(pfile)
        pfile.close()
        print('Inventory Loaded\n')
        del pfile
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

    def setInventory(self, invList, firstVar, defaultItems): #load in player inventory
        if firstVar == True:
            print('Loading inventory with default starting items')
            for item in defaultItems:
                self.inventoryAdd(item)
            self.saveInventory(invList)
        if firstVar == False:
            self.inventory = self.loadInventory()
            None

    def loadStats(self): #Load player stats from stats.dat
        print('Loading Stats...')
        pfile = open('stats.dat', 'rb')
        currentHealth = pickle.load(pfile)
        gold = pickle.load(pfile)
        playerName = pickle.load(pfile)
        currentWeapon = pickle.load(pfile)
        pfile.close()
        print('Stats Loaded\n')
        del pfile
        return currentHealth, gold, playerName, currentWeapon

    def saveStats(self): #Save player stats to stats.dat
        print('Saving Stats')
        pfile = open('stats.dat', 'wb')
        pickle.dump(self.currentHealth, pfile)
        pickle.dump(self.gold, pfile)
        pickle.dump(self.playerName, pfile)
        pickle.dump(self.currentWeapon, pfile)
        pfile.close()
        print('Stats Saved\n')
        del pfile

    def setStats(self, firstVar): #set the player stats
        if firstVar == True:
            print('Loading default starting stats')
            self.currentHealth = self.maxHealth
            self.gold = 75
            self.selectWeapon()
            self.saveStats()
        if firstVar == False:
           self.currentHealth, self.gold, self.playerName, self.currentWeapon = self.loadStats()
    
    def setName(self): #set the player name
        name = ''
        while name == '':
            name = input('What do you want to call yourself?  [')
        self.playerName = name

    def displayStats(self): #Display player stats
        print(self.playerName + '\'s stats: ')
        print('Health: ' + str(self.currentHealth))
        print('Gold: ' + str(self.gold))
        print('Weapon in use is ', end = '')
        print(self.currentWeapon.name)
        print('')
        self.displayInventory(self.inventory)
        print('\n')

    def eat(self): #allow the player to eat and heal
        if self.currentHealth >= self.maxHealth:
            print("Your health is full! You can't eat anything!")
            return 0
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
        for i in foodDictionary:
            if choice.name == i.name:
                print('The item you chose exists as a food item!')
                print('Your choice exists in your inventory!')
                print('Eating ' + choice.name + '\n')
                self.currentHealth += choice.healthRegen
                if self.currentHealth > self.maxHealth:
                    self.currentHealth = self.maxHealth
                self.inventoryRemove(choiceNum)
                self.saveInventory(self.inventory)
                self.saveStats()
                break
            else:
                print('The item you chose does not exist, or is not a food item')

    def selectWeapon(self): #select player weapon for fighting
        selected = False
        print('What weapon to use?')
        self.displayInventory(self.inventory)
        while True:
            try:
                choice = int(input('Choice  ['))
                choice = self.inventory[choice-1]
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
                self.saveStats()
                selected = True
                break
        if not selected:
                print('The item you chose does not exist, or is not a weapon')
                print('Defaulting to fists')
                self.currentWeapon = Fists()
                self.saveStats()


    def weaponDurabilityDecrease(self): #cause damage to the weapon durability
        self.currentWeapon.durability -= self.currentWeapon.durabilityDecrease
        if self.currentWeapon.durability <= 0:
            print('Your ' + self.currentWeapon.name + ' broke!')
            print('You must now select a new weapon')
            self.inventoryRemove(self.inventory[self.inventory.index(self.currentWeapon)])
            self.currentWeapon.durability = 100
            self.selectWeapon()
            self.saveInventory(self.inventory)

    def attack(self, enemy):
        enemy.currentHealth -= random.randint(self.currentWeapon.damage[0],self.currentWeapon.damage[1])
        self.weaponDurabilityDecrease()

    def damage(self, damage):
        self.currentHealth -= damage
        print("You took " + str(damage) + " damage!")

    def __init__(self, newGame):
        firstTime = self.firstTimeManager()
        if newGame:
            firstTime = True
        if firstTime == True:
            #select name
            self.setName()
        else:
            None
        self.setInventory(self.inventory, firstTime, defaultItems)
        self.setStats(firstTime)
        self.displayStats()

class Game(object):

    def mainMenu(self):
        print('Welcome to the Text RPG')
        print('''
        1-Create new game
        2-Continue game
        ''')
        choice_status = False
        choices = (1,2)
        choice = 0
        while not choice_status and choice not in choices:
            try:
                choice = int(input('Choice: '))
            except:
                print('Invalid choice')
        if choice == 1:
            player = Player(True)
            self.intro(player)
        elif choice == 2:
            try:
                player = Player(False)
                self.pause(player)
            except:
                print('There was an error! Maybe there isn\'t a saved game?')
    def intro(self, player):
        print("You are exploring a dark dungeon that contains many wild and unknown species of animals.\nApparently there are also some dangerous mutants...")
        print("How many floors can you explore before you die...")
        print("MUHAHAHAHAHAHAAAAAAAAAAAAAAAAAAAAAAAA!")
        print("GOOD LUCK!")
        print()
        self.pause(player)
    def pause(self, player):
        print("Hey, have a break!")
        while True:
            print("What do you want to do?")
            #eat, select weapon, save game, and continue
            choices = ['1','2','3','4', '5']
            print("""
            1 - Eat
            2 - Select Weapon
            3 - View Stats and Inventory
            4 - Save Game
            5 - Continue""")
            choice = input("Choice: ")
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
                    print("Sorry! feature not implemented yet")
                    player.damage(10)
            else:
                print("Invalid number!")
        

    def __init__(self):
        self.mainMenu()
game = Game()
