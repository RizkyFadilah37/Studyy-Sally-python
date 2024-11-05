# Template Class
class Mahasiswa:
    # Constructor
    def __init__(self,inputName, inputAge):
        self.name = inputName
        self.age = inputAge

# Object
mahasiswa1 = Mahasiswa("Adachi Sakura",17)
mahasiswa2 = Mahasiswa("Shimamura Hougetsu",17)
mahasiswa3 = Mahasiswa("Awa Subaruu",18)

# Print Object
print(mahasiswa1.__dict__)
print(mahasiswa2.name)
print(mahasiswa3.age)