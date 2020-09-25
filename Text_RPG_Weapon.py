class Weapon(object):
    name = 'weapon'
    type = 'weapon'
    damage = 0
    durability = 100 #percentage
    durabilityDecrease = 0 #by how much percent the durability decreases
    cost = 0
    isStackable = False
    def __str__(self):
        rep = self.name + ': Deals ' + str(self.damage) + ' Damage | ' + 'Current Durability is ' + str(self.durability) + '%'
        return rep


class TrustyDagger(Weapon):
    name = 'Trusty Dagger'
    damage = (15, 20)
    durabilityDecrease = 5
    cost = 25 #make random

class Fists(Weapon):
    name = 'Fists'
    damage = (8, 10)
    durabilityDecrease = 0 #fists should not break
    def __str__(self):
        rep = self.name + ': Deals ' + str(self.damage) + ' Damage'
        return rep

if __name__ == "__main__":
    print("This is a module that contains weapon data for the game.")
    input("\n\nPress the enter key to exit.")