class Pokemon():
    def __init__(self, name, level, hp):
        self.name = name
        self.level = level
        self.hp = hp
    def say(self):
        print(f"I am pokemon!, My name is {self.name}")
class Pikachu(Pokemon): #is-a realtionship
    pass
class Squirtle(Pokemon):
    pass
class Charizard(Pokemon):
    pass

if __name__ =="__main__":
    pikachu = Pikachu("pikachu", 1, 35) # instance creation
    squirtle = Squirtle("squirtle", 1, 44)
    charizard = Charizard("charrizard", 36, 78)

    print(squirtle.name)
    pikachu.say()
    print(issubclass(Squirtle, Pokemon))
    charizard.say()


