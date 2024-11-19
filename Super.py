class Arcanist:
    def __init__(self, name, Realdmg,mentalDmg):
        self.name = name
        self.Realdmg = Realdmg
        self.mentalDmg = mentalDmg

    def info(self):
        print ("Arcanist Status\n\nName : {}\nAttack Power : {}\nMagic Power : {}".format(self.name,self.Realdmg, self.mentalDmg))


class physical(Arcanist):
    def __init__(self, name):
        super().__init__(name, 100,0)
        super().info()

class mental(Arcanist):
    def __init__(self, name):
        super().__init__(name, 0,100)
        super().info()


# Reverse 1999 mentioned !!!
kakania = mental("Kakania")
lilya = physical("Lilya")