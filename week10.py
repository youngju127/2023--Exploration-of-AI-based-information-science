class PrettyMixin:
    def dump(self):
        #print(f'{self.name} pokemon')
        import pprint
        pprint.pprint(vars(self))

class Pokemon(PrettyMixin):
    def __init__(self, name, hp, level):
        self.hidden_name = name
        self.hp = hp
        self.level = level

    def get_name(self):
        print("getter executed")
        return self.hidden_name
    def set_name(self, name):
        print("setter executed")
        self.hidden_name = name

    def info(self):
        print("=============")
        print(f"Name : {self.hidden_name}")
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
    p2.set_name("wartotle")
    print(p2.get_name())