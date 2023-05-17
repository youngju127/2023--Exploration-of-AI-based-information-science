class Pokemon():
    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.hp = hp
    def say(self):
        print(f"I am pokemon!, My name is {self.name}")
    def attack(self):
        print(f"{self.name} launches an area attack")
    def attack_target(self, target):
        print(f"{self.name} launches an area attack to {target}")
class Pikachu(Pokemon): #is-a realtionship
    def attack(self):
        print(f"{self.name} casts a million volt attack")

    def attack_target(self, target):
        print(f"{self.name} casts a million volt to {target}")
class Squirtle(Pokemon):
    def attack(self):
        print(f"{self.name} casts a water gun attack")

    def attack_target(self, target):
        print(f"{self.name} casts a water gun to {target}")
class Charizard(Pokemon):
    def attack(self):
        print(f"{self.name} casts a flamethrower attack")

    def attack_target(self, target):
        print(f"{self.name} casts a flamethrower to {target}")
if __name__ =="__main__":
    pikachu = Pikachu("pikachu", 1, 35) # instance creation
    squirtle = Squirtle("squirtle", 1, 44)
    charizard = Charizard("charrizard", 36, 78)

    pikachu.attack()
    squirtle.attack_target(charizard.name)
    charizard.attack_target(squirtle.name)


