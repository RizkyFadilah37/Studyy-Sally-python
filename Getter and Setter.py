class Hero:

    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        

    @property
    def info(self):
        return "Name {}  \n\tHealth: {}".format(self.name, self.__health)

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self, input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print("armor dihapus")
        self.__armor = None




print("Change name")
adachi = Hero("Adachi", 100, 10)
print(adachi.info)
adachi.name = "Shimamura"
print(adachi.info)

print(adachi.__dict__)

print("getter and setter for __armor: ")
print(adachi.armor)

adachi.armor = 50
print(adachi.armor)

print(adachi.__dict__)
del adachi.armor

print(adachi.armor)
        