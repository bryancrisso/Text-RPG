class Enemy(object):
    name = 'enemy'
    type = 'enemy'
    maxHealth = 0
    currentHealth = 0
    damage = (0,0)
    level = (0,0)
    gold = (0,0)
    def __str__(self):
        rep = self.name + ': Deals ' + str(self.damage) + ' Damage | ' + 'Has ' + str(self.currentHealth) + ' Health'
        return rep
        pass
    def __init__(self):
        self.currentHealth = self.maxHealth


class Mutant(Enemy):
    name = 'Mutant'
    type = 'enemy'
    maxHealth = 100
    damage = (4,5)
    level = (1,6)
    gold = (10,30)
class Brute(Enemy):
    name = 'Brute'
    type = 'enemy'
    maxHealth = 125
    damage = (6,8)
    level = (2,8)
    gold = (20,50)
class Skeleton(Enemy):
    name = 'Skeleton'
    type = 'enemy'
    maxHealth = 50
    damage = (4,5)
    level = (1,5)
    gold = (10,20)
class KnifeGoblin(Enemy):
    name = 'Knife Goblin'
    type = 'enemy'
    maxHealth = 70
    damage = (12,18)
    level = (6,15)
    gold = (20,60)
class Ghoul(Enemy):
    name = 'Ghoul'
    type = 'enemy'
    maxHealth = 110
    damage = (10,13)
    level = (4,15)
    gold = (15,55)
class MutantGuard(Enemy):
    name = 'Mutant Guard'
    type = 'enemy'
    maxHealth = 120
    damage = (9,12)
    level = (5,15)
    gold = (40,70)
class BruteGuard(Enemy):
    name = 'Brute Guard'
    type = 'enemy'
    maxHealth = 150
    damage = (11,15)
    level = (7,20)
    gold = (50,90)
class MutantWarrior(Enemy):
    name = 'Mutant Warrior'
    type = 'enemy'
    maxHealth = 180
    damage = (14,18)
    level = (10,34)
    gold = (60,100)
class ThiccArab(Enemy):
    name = 'Thicc Arab'
    type = 'enemy'  
    maxHealth = 130
    damage = (20,30)
    level = (15,30)
    gold = (80,100)
class DarkKnight(Enemy):
    name = 'Dark Knight'
    type = 'enemy'
    maxHealth = 150
    damage = (10,35)
    level = (10,30)
    gold = (70,140)
class Drunk(Enemy):
    name = 'Drunk'
    type = 'enemy'
    maxHealth = 75
    damage = (4,5)
    level = (1,10)
    gold = (0,5)
class Knight(Enemy):
    name = 'Knight'
    type = 'enemy'
    maxHealth = 125
    damage = (12,18)
    level = (8,20)
    gold = (70,100)
class Giant(Enemy):
    name = 'Giant'
    type = 'enemy'
    maxHealth = 300
    damage = (10,20)
    level = (20,45)
    gold = (100,180)
class Looter(Enemy):
    name = 'Looter'
    type = 'enemy'
    maxHealth = 110
    damage = (16,25)
    level = (5,25)
    gold = (80,125)
class Samurai(Enemy):
    name = 'Samurai'
    type = 'enemy'
    maxHealth = 200
    damage = (25,45)
    level = (20,35)
    gold = (80,140)
class Goblin(Enemy):
    name = 'Goblin'
    type = 'enemy'
    maxHealth = 70
    damage = (5,6)
    level = (2,12)
    gold = (15,45) 
class PoisonousSpider(Enemy): #make poisonous
    name = 'Poisonous Spider'
    type = 'enemy'
    maxHealth = 20
    damage = (3,4)
    level = (1,40)
    gold = (0,0)         #no gold as animals dont carry gold
class Hound(Enemy): 
    name = 'Hound'
    type = 'enemy'
    maxHealth = 60
    damage = (11,12)
    level = (10,20)
    gold = (0,0)
class WildBoar(Enemy): 
    name = 'Wild Boar'
    type = 'enemy'
    maxHealth = 70
    damage = (8,9)
    level = (5,20)
    gold = (0,0)
class Hunter(Enemy): 
    name = 'Hunter'
    type = 'enemy'
    maxHealth = 100
    damage = (35,40)
    level = (17,35)
    gold = (90,120)
class HostileTrader(Enemy): 
    name = 'Hostile Trader'
    type = 'enemy'
    maxHealth = 250
    damage = (40,60)
    level = (20,45)
    gold = (140,230) 
class Primitive(Enemy): 
    name = 'Primitive'
    type = 'enemy'
    maxHealth = 100
    damage = (7,9)
    level = (1,6)
    gold = (15,45)
class PrimitiveLeader(Enemy): 
    name = 'Primitive Leader'
    type = 'enemy'
    maxHealth = 115
    damage = (11,13)
    level = (2,6)
    gold = (25,50)
class PrimitiveSlave(Enemy): 
    name = 'Primitive Slave'
    type = 'enemy'
    maxHealth = 90
    damage = (4,5)
    level = (1,6)
    gold = (10,15)
class PrimitiveGuard(Enemy): 
    name = 'Primitive Guard'
    type = 'enemy'
    maxHealth = 125
    damage = (12,15)
    level = (2,6)
    gold = (15,45)