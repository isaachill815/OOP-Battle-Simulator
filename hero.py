import random
class Hero:
    """The hero blueprint will be implemented later in the project."""

    def __init__ (self, name):
        self.name = name # each hero shold haveits own name
        self.health = 120 
        self.attack_power = 25
    
    def attack(self):
        """ attack returns a number of damage """
        return random.randint(1,self.attack_power)
    def take_damage(self, damage):
        self.health  = self.health - damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0


