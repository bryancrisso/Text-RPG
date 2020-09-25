class Food(object):
    name = ''
    healthRegen = 0
    type = 'food'
    cost = 0
    isStackable = True
    amount = 0
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

class Apple(Food):
    name = 'Apple'
    healthRegen = 5
    cost = 6

class CornishPasty(Food):
    name = 'Cornish Pasty'
    healthRegen = 40
    cost = 35

class SteamedHam(Food):
    name = 'Steamed Ham'
    healthRegen = 60
    cost = 45
#class BatStew(Food):
    #name = 'Bat Stew'
    #healthRegen = 20 ! CHANCE OF DAMAGING PLAYER?
    #cost = 10        ! dk how to impliment



if __name__ == "__main__":
    print("This is a module that contains food data for the game.")
    input("\n\nPress the enter key to exit.")