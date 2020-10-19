class Food(object):
    name = ''
    healthRegen = 0
    type = 'food'
    cost = 0
    isStackable = True
    amount = 0
    level = (0,0)
    def __str__(self):
        rep = self.name + ': Regenerates ' + str(self.healthRegen) + ' Health'
        return rep
    def __repr__(self):
        rep = self.name + ': Regenerates ' + str(self.healthRegen) + ' Health'
        return rep

class Bread(Food):
    name = 'Bread'
    healthRegen = 15
    cost = 16
    level = (1,10) # example of "tiers" (loot spawns based on current floor number)

class Apple(Food):
    name = 'Apple'
    healthRegen = 5
    cost = 6
    level = (1,5)
class CornishPasty(Food):
    name = 'Cornish Pasty'
    healthRegen = 40
    cost = 35
    level = (5,15)
class SteamedHam(Food):
    name = 'Steamed Ham'
    healthRegen = 60
    cost = 45
    level = (10,20)
class Beans(Food):
    name = 'Beans'
    healthRegen = 1
    cost = 2
    level = (1,3)
#class BatStew(Food):
    #name = 'Bat Stew'
    #healthRegen = 20 ! CHANCE OF DAMAGING PLAYER?
    #cost = 10        ! dk how to impliment

class Cherries(Food):
    name = 'Cherries'
    healthRegen = 2
    cost = 3
    level = (1,4)
class Steak(Food):
    name = 'Steak'
    healthRegen = 70
    cost = 50
  level = (10,30)
class TinOfBiscuits(Food):
    name = 'Tin of Biscuits'
    healthRegen = 9
    cost = 10
    level = (1,15)
class BleachBottle(Food):
    name = 'Bleach Bottle'
    healthRegen = -10
    cost = 15
    level = (5,20)
    #Put effect of removing posion and whatnot

#make food better value if you pay more
if __name__ == "__main__":
    print("This is a module that contains food data for the game.")
    input("\n\nPress the enter key to exit.")