class Fruit:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} is {self.price} dollars."

    def __repr__(self):
        return f"Fruit('{self.name}', {self.price})"
    
    def __add__(self, other):
        return self.price + other.price
    
    def __sub__(self, other):
        return self.price - other.price
    
    def __mul__(self, other):
        return self.price * other.price
    
    def __truediv__(self, other):
        return self.price / other.price
    
    def __floordiv__(self, other):
        return self.price // other.price
    
    @property
    def __dict__(self):
        return "This is a dictionary"
    

apple = Fruit("Apple", 2)
banana = Fruit("Banana", 3)
print(apple)
print(repr(apple))
print(banana)
print(f"total price apple + banana =" , apple + banana)
