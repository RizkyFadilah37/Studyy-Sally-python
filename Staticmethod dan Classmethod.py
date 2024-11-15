class Hero:
    
    # private class variable
    __count = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health
        Hero.__count += 1

    # this method only applies to objects
    def getJumlah(self):
        return Hero.__count
    
    # this method does not apply to objects but applies to the class
    def getJumlah1():
        return Hero.__count
    
    # static method (decorator) applies to both objects and the class
    @staticmethod
    def getJumlah2():
        return Hero.__count
    
    @classmethod
    def getJumlah3(cls):
        return cls.__count
    
hero1 = Hero("Adachi",100)
print(hero1.getJumlah())
hero2 = Hero("Shimamura",100)
print(hero2.getJumlah())
hero3 = Hero("Sally",100)
print(hero3.getJumlah())