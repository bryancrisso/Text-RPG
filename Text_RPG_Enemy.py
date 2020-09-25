class Enemy(object):
    name = 'enemy'
    type = 'enemy'
    maxHealth = 0
    currentHealth = 0
    damage = 0
    level = (0,0)
    def __str__(self):
        #rep = self.name + ': Deals ' + str(self.damage) + ' Damage | ' + 'Current Durability is ' + str(self.durability) + '%'
        #return rep
        pass
    def __init__(self):
        self.currentHealth = self.maxHealth