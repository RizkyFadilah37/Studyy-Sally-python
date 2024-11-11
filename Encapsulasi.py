class Hero:

    def __init__(self,name, attackPower, magicPower, defense, health) -> None:
        self.__name = name
        self.__attackPower = attackPower
        self.__magicPower = magicPower
        self.__defense = defense
        self.__health = health

    # getter
    def getName(self):
        return self.__name

    def getHealth(self):
        return self.__health

    # setter
    def Attacked(self, attackedPower):
        self.__health -= attackedPower

    def setAttUp(self, up):
        self.__attackPower += up

Kakania = Hero("Kakania", 10, 200, 300, 100)

print(Kakania.getName())
print(Kakania.getHealth())

# Kakania.Attacked(10)
Kakania.Attacked(20)
print(Kakania.getHealth())

