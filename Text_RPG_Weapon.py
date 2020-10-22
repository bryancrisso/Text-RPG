class Weapon(object):
    name = 'weapon'
    type = 'weapon'
    damage = 0
    durability = 100 #percentage
    durabilityDecrease = 0 #by how much percent the durability decreases
    cost = 0
    isStackable = False
    level = 0
    quality = 0
    def __str__(self):
        rep = self.name + ': Deals ' + str(self.damage) + ' Damage | ' + 'Current Durability is ' + str(self.durability) + '%'
        return rep

###############
#LEVEL 1 ITEMS#
###############

class TrustyDagger(Weapon):
    name = 'Trusty Dagger'
    damage = (12, 18)
    durabilityDecrease = 2
    cost = 100 #make random
    level = 1 #based on difficulty (increments every 10 floors)
    quality = 2 #1 for common, 2 for rare, 3 for epic, 4 for legendary
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
    cost = 200
    level = 1
    quality = 3
class ShoddyShank(Weapon):
    name = 'Shoddy Shank'
    damage = (9,12) 
    durabilityDecrease = 8
    cost = 50
    level = 1
    quality = 1
class Club(Weapon):
    name = 'Club'
    damage = (7,9) 
    durabilityDecrease = 4
    cost = 50
    level = 1
    quality = 1
class Lance(Weapon):
    name = 'Lance'
    damage = (10,40)
    durabilityDecrease = 3
    cost = 100
    level = 1
    quality = 2
class Katana(Weapon):
    name = 'Katana'
    damage = (25,45)
    durabilityDecrease = 2
    cost = 300
    level = 1
    quality = 4

###############
#LEVEL 2 ITEMS#
###############

class BroadSword(Weapon):
    name = 'Broadsword'
    damage = (15,25)
    durabilityDecrease = 2
    cost = 150
    level = 2
    quality = 2
class StilettoKnife(Weapon):
    name = 'Stiletto Knife'
    damage = (14,18)
    durabilityDecrease = 3
    cost = 75
    level = 2
    quality = 1


if __name__ == "__main__":
    print("This is a module that contains weapon data for the game.")
    input("\n\nPress the enter key to exit.")