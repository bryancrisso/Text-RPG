class Armour(object):
    name = 'armour'
    type = 'armour'
    defense = 0
    durability = 100 #percentage
    durabilityDecrease = 0 #by how much percent the durability decreases
    cost = 0
    isStackable = False
    level = 0
    quality = 0
    maxProtection = 0
    def __str__(self):
        rep = self.name + ': Reduces damage by ' + str(self.defense) + '% | ' + 'Maximum protection is ' + str(self.maxProtection) + ' Damage | ' + 'Current Durability is ' + str(self.durability) + '%'
        return rep

###############
#LEVEL 1 ITEMS#
###############

class ClothArmour(Armour):
    name = 'Cloth Clothes'
    defense = 0
    maxProtection = 0
    durability = 100
    durabilityDecrease = 0
    cost = 0
    def __str__(self):
        rep = self.name + ': Just your regular clothes'
        return rep
class LeatherArmour(Armour):
    name = 'Leather Clothes'
    defense = 10
    maxProtection = 15
    durabilityDecrease = 3
    cost = 100
    level = 1
    quality = 1
class TinSuit(Armour):
    name = 'Tin Suit'
    defense = 20
    maxProtection = 20
    durabilityDecrease = 1
    cost = 150
    level = 1
    quality = 2

###############
#LEVEL 2 ITEMS#
###############

class ChainArmour(Armour):
    name = 'Chainmail Armour'
    defense = 25
    maxProtection = 40
    durabilityDecrease = 2
    cost = 300
    level = 2
    quality = 2
class PlateArmour(Armour):
    name = 'Plate Armour'
    defense = 35
    maxProtection = 40
    durabilityDecrease = 1
    cost = 250
    level = 2
    quality = 3
class HeavyPlateArmour(Armour):
    name = 'Heavy Plate Armour'
    defense = 50
    maxProtection = 60
    durabilityDecrease = 0.5
    cost = 500
    level = 2
    quality = 4

###############
#LEVEL 3 ITEMS#
###############

class ReinforcedLeatherArmour(Armour):
    name = "Reinforced Leather Armour"
    defense = 15
    maxProtection = 80
    durabilityDecrease = 1
    cost = 200
    level = 3
    quality = 1