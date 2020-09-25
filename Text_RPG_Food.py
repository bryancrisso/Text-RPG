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
    cost = 2

class Apple(Food):
    name = 'Apple'
    healthRegen = 25
    cost = 4

if __name__ == "__main__":
    print("This is a module that contains food data for the game.")
    input("\n\nPress the enter key to exit.")