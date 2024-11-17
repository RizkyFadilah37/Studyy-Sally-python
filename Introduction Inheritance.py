class Super:

    def __init__(self):
        print("This is Super Class")

class Inheritor_1(Super):
    
        def __init__(self):
            print("This is Inheritor 1 Class")

class Inheritor_2(Super):
    
    def __init__(self):
        print("This is Inheritor 2 Class")


# Super()
super = Super()
print(super)

# Inheritor_1()
inheritor_1 = Inheritor_1()
print(inheritor_1)

# Inheritor_2()
inheritor_2 = Inheritor_2()
print(inheritor_2)