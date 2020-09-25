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
    damage = (12, 18)
    durabilityDecrease = 2
    cost = 25 #make random

class Fists(Weapon):
    name = 'Fists'
    damage = (4, 5)
    durabilityDecrease = 0 #fists should not break
    def __str__(self):
        rep = self.name + ': Deals ' + str(self.damage) + ' Damage'
        return rep
class BattleAxe(Weapon):
    name = "Battle Axe"
    damage = (20,30)
    durabilityDecrease = 4
    cost = 50
class ShoddyShank(Weapon):
    name = 'Shoddy Shank'
    damage = (9,12) 
    durabilityDecrease = 8
    cost = 10
class Lance(Weapon):
    name = 'Lance'
    damage = (10,40)
    durabilityDecrease = 3
    cost = 40
class Katana(Weapon):
    name = 'Katana'
    damage = (25,45)
    durabilityDecrease = 2
    cost = 70
if __name__ == "__main__":
    print("This is a module that contains weapon data for the game.")
    input("\n\nPress the enter key to exit.")