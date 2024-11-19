class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("{} Health : {}".format(
            self.name,
            self.health
            )
        )

class Hero_magic(Hero):
    def __init__(self,name):
        super().__init__(name,100)

    # Override Method
    def showInfo(self):
        print("{} \n\tRole : Magic\n\tHealth : {}".format(
            self.name,
            self.health
            )
        )
class Hero_physical(Hero):
    def __init__(self,name):
        super().__init__(name,100)


gusion = Hero_magic("Gusion")
Ling = Hero_physical("Ling")

gusion.showInfo()
Ling.showInfo()   
