class Hero:
    __count = 0

    def __init__(self, name, health, armor, attPower):
        self.__name = name
        self.__healthBase = health
        self.__armorBase = armor
        self.__attPowerBase = attPower
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthBase + (self.__level*10)
        self.__armor = self.__armorBase + (self.__level*0.8)  
        self.__attPower = self.__attPowerBase + (self.__level*2)

        self.health = self.__healthMax
        Hero.__count += 1

    @property
    def info(self):
        return "{} Status\n\nLevel : {}\nHealth : {}/{}\nAttack Power : {}\nArmor : {}".format(self.__name,self.__level, self.health, self.__healthMax, self.__attPower, self.__armor)
    
    @property
    def levelUp():
        pass

    @levelUp.setter
    def gainExp(self, exp):
        self.__exp += exp
        if self.__exp >= 100:
            print(self.__name, "Level Up!")
            self.__exp -= 100
            self.__level += 1
            self.__healthMax = self.__healthBase + (self.__level*10)
            self.__armor = self.__armorBase + (self.__level*0.8)  
            self.__attPower = self.__attPowerBase + (self.__level*2)

    def attack(self, opponent):
        damage = int(self.__attPower - opponent.__armor * 0.3)
        opponent.health -= damage
        if opponent.health <= 0:
            opponent.health = 0
            print(f"{opponent.__name} has been defeated!")
            self.gainExp = 50
        else:
            self.gainExp = 50
        return opponent.health



Tanuki = Hero("Tanuki", 100, 10, 5)
adachi = Hero("Adachi", 90, 10, 5)

adachi.gainExp = 100

adachi.attack(Tanuki)


