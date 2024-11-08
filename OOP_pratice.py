class Character:

    def __init__(self,name,attack,defense,health):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.health = health


    def Attack(self,enemy):
        print(self.name+" attack "+enemy.name)
        enemy.Attacked(self,self.attack)
        enemy.death()
        
    def Attacked(self,enemy,attack_enemy):
        print(self.name+" was attacked by "+enemy.name)
        total_attack = (attack_enemy // (self.defense*0.5))
        print("Total attack : "+str(total_attack))
        self.health -= total_attack
        
    def death(self):
        if self.health <= 0:
            print(self.name+" is dead")
        


adachi = Character("Adachii",1000,10,100)
tomari = Character("Tomari",30,10,100)

adachi.Attack(tomari)
        
