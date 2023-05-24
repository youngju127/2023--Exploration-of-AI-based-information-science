

class Pokemon:
    pokemon_count = 0
    def __init__(self, name, hp, level):
        self.__name = name
        self.hp = hp
        self.level = level
        Pokemon.pokemon_count += 1

    def __add__(self, other):
        """
        both pokemon's total hp and level
        :param other:
        :return:
        """
        return f'total hp  {self.hp + other.hp}, total level : {self.level + other.level}'

    def __str__(self):
        """
        make print 'I'm []' instead of address
        :return:
        """
        return f"I'm a {self.__name}"
    @staticmethod
    def intro():
        print("ISHS Pokemon GAME")
    @classmethod
    def print_pokemon_count(cls):
        print(f"pokemon population : {cls.pokemon_count}")
    @property
    def name(self):
        print("getter executed")
        return self.__name

    @name.setter
    def name(self, name):
        print("setter executed")
        self.__name = name

    def info(self):
        print("=============")
        print(f"Name : {self.__name}")
        print(f"Hp : {self.hp}")
        print(f"Level : {self.level}")
        print("=============")




if __name__ == "__main__":
    Pokemon.intro()
    p1 = Pokemon("Pikachu", 35, 1)
    p2 = Pokemon("Squirtle", 40, 1)
    p3 = Pokemon("charizard", 60, 25)
    Pokemon.print_pokemon_count()
    print(p1 + p2)
    print(p3)
    print(p1)