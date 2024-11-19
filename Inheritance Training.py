class Hero:

    def __init__(self,name):
        self.health_pool = [0,100,200,300,400,500]
        self.attPower_pool = [10,20,30,40,50,60]
        self.armor_pool = [1,2,3,4,5,6]
        self.__name = name
        self.__exp = 0
        self.__level = 0

    def show_info(self):
        print("Info Hero {} \n\tLevel : {}\n\tHealth : {}\n\tAttack Power : {}\n\tArmor : {}".format(
                self.__name,
                self.__level,
                self.__health,
                self.__attPower,
                self.__armor
            )
        )

    @property
    def health_pool(self):
        pass

    @property
    def attPower_pool(self):
        pass

    @property
    def armor_pool(self):
        pass

    @property
    def levelUp(self):
        pass

    @property
    def gainExp(self):
        pass

    @health_pool.setter
    def health_pool(self,input):
        self.__health_pool = input
    
    @attPower_pool.setter
    def attPower_pool(self,input):
        self.__attPower_pool = input

    @armor_pool.setter
    def armor_pool(self,input):
        self.__armor_pool = input

    @gainExp.setter
    def gainExp(self,input):
        self.__exp += input
        if(self.__exp >= 100):
            self.levelUp = self.__exp // 100
            self.__exp %= 100

    @levelUp.setter
    def levelUp(self,input):
        self.__level += input
        self.__health = self.__health_pool[self.__level]
        self.__attPower = self.__attPower_pool[self.__level]
        self.__armor = self.__armor_pool[self.__level]
        

class HeroMagic(Hero):

    def __init__(self,name):
        super().__init__(name)
        self.health_pool = [0,50,100,150,200,250]
        self.attPower_pool = [15,25,35,45,55,65]
        self.armor_pool = [0,1,2,3,4,5]
        self.levelUp = 1  


class HeroPhysical(Hero):

    def __init__(self,name):
        super().__init__(name)
        self.health_pool = [0,200,300,400,500,600]
        self.attPower_pool = [5,10,15,20,25,30]
        self.armor_pool = [2,3,4,5,6,7]
        self.levelUp = 1


gusion = HeroMagic('Gusion')
ling = HeroPhysical("Ling")

gusion.show_info()

gusion.gainExp = 200
gusion.show_info()



