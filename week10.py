class PrettyMixin:
    def dump(self):
        #print(f'{self.name} pokemon')
        import pprint
        pprint.pprint(vars(self))

class Pokemon(PrettyMixin):
    def __init__(self, name, hp, level):
        self.__name = name
        self.hp = hp
        self.level = level
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
    p1 = Pokemon("Pikachu", 35, 1)
    p2 = Pokemon("Squirtle", 40, 1)
    p1.dump()
    p1.info()
    p2.level = 2
    p2.info()
    print(p2._Pokemon__name)
    p2.__name = "wartotle"
    print(p2.__name)