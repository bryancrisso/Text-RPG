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
    type = 'enemy' #is that right? 
    maxHealth = 100
    damage = (4,5)
    level = (1,7)
    gold = (10,30)
class Brute(Enemy):
    name = 'Brute'
    type = 'enemy'
    maxHealth = 125
    damage = (6,8)
    level = (2,10)
    gold = (10,40)
class Skeleton(Enemy):
    name = 'Skeleton'
    type = 'enemy'
    maxHealth = 50
    damage = (4,5)
    level = (1,5)
    gold = (5,20)
class KnifeGoblin(Enemy):
    name = 'Knife Goblin'
    type = 'enemy'
    maxHealth = 70
    damage = (12,18)
    level = (5,15)
    gold = (20,45)
class Ghoul(Enemy):
    name = 'Ghoul'
    type = 'enemy'
    maxHealth = 110
    damage = (10,12)
    level = (5,10)
    gold = (15,40)
class MutantGuard(Enemy):
    name = 'Mutant Guard'
    type = 'enemy'
    maxHealth = 150
    damage = (15,30)
    level = (7,20)
    gold = (40,80)
class ThiccArab(Enemy):
    name = 'Thicc Arab'
    type = 'enemy'  
    maxHealth = 130
    damage = (20,30)
    level = (10,20)
    gold = (80,100)