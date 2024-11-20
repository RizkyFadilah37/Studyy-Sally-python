class method_A:
    def method_A(self):
        print("This is method A")

class method_B:
    def method_B(self):
        print("This is method B")

class method_C(method_A,method_B):
    pass

obj_C = method_C()
obj_C.method_A()
obj_C.method_B()


print("=====================================")
# Example
class Team:
    def setTeam(self,team):
        self.team = team

    def showTeam(self):
        print(self.team)

class Type:
    def setType(self,type):
        self.type = type

    def showType(self):
        print(self.type)

class Hero(Team,Type):
    def __init__(self,name,health):
        self.name = name
        self.health = health

gusion = Hero('Gusion',100)
gusion.setTeam('Blue')
gusion.setType('Assassin')
gusion.showTeam()
gusion.showType()
