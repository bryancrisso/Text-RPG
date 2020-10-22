class Food(object):
    name = ''
    healthRegen = 0
    type = 'food'
    cost = 0
    isStackable = True
    amount = 0
    level = 0
    quality = 0
    def __str__(self):
        rep = self.name + ': Regenerates ' + str(self.healthRegen) + ' Health'
        return rep
    def __repr__(self):
        rep = self.name + ': Regenerates ' + str(self.healthRegen) + ' Health'
        return rep

###############
#LEVEL 1 ITEMS#
###############

class Bread(Food):
    name = 'Bread'
    healthRegen = 15
    cost = 20
    level = 1 # example of "tiers" (loot spawns based on current difficulty)
    quality = 2

class Apple(Food):
    name = 'Apple'
    healthRegen = 5
    cost = 10
    level = 1
    quality = 1

class CornishPasty(Food):
    name = 'Cornish Pasty'
    healthRegen = 40
    cost = 35
    level = 1
    quality = 3

class SteamedHam(Food):
    name = 'Steamed Ham'
    healthRegen = 60
    cost = 50
    level = 1
    quality = 4

class Beans(Food):
    name = 'Beans'
    healthRegen = 1
    cost = 5
    level = 1
    quality = 1

#class BatStew(Food):
    #name = 'Bat Stew'
    #healthRegen = 20 ! CHANCE OF DAMAGING PLAYER?
    #cost = 10        ! dk how to impliment

class Cherries(Food):
    name = 'Cherries'
    healthRegen = 2
    cost = 7
    level = 1
    quality = 1

###############
#LEVEL 2 ITEMS#
###############

class Steak(Food):
    name = 'Steak'
    healthRegen = 70
    cost = 75
    level = 2
    quality = 4

class TinOfBiscuits(Food):
    name = 'Tin of Biscuits'
    healthRegen = 9
    cost = 15
    level = 2
    quality = 1

class BleachBottle(Food):
    name = 'Bleach Bottle'
    healthRegen = -10
    cost = 15
    level = 2
    quality = 2
    #Put effect of removing posion and whatnot

#make food better value if you pay more
if __name__ == "__main__":
    print("This is a module that contains food data for the game.")
    input("\n\nPress the enter key to exit.")