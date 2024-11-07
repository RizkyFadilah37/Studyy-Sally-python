class Person:
    # class variable
    count_person = 0

    def __init__(self,inputName,inputAge):
        self.name = inputName
        self.age = inputAge
        Person.count_person += 1

    # void function (method without return/argument)
    def sayHi(self):
        print("Hello "+ self.name)

    # method with argument
    def addAge(self,up):
        self.age += up

    # method with return
    def Age(self):
        return self.age

# with void function
person1 = Person("Adachi",17)
person1.sayHi()


# with method argument
person2 = Person("Takagi",19)
person2.addAge(1)
print(person2.age)

# with method return
person3 = Person("Awawa",25)
print(person3.Age())