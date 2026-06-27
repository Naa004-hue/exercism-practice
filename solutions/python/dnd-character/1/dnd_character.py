import random
class Character:
    def ability(self) :
        rolls = []  
        for _ in range(4):
             rolls.append(random.randint(1, 6))
        rolls.remove(min(rolls))
        score=sum(rolls)
        return score
            
    def __init__(self): 
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

def modifier(value):
    return ( value - 10 ) // 2