# Template Class
class Mahasiswa:
    # class variabel
    count = 0

    # Constructor
    def __init__(self,inputName, inputAge):
        self.name = inputName
        self.age = inputAge
        Mahasiswa.count += 1
        print("Create Mahasiswa by name: "+inputName)


mahasiswa1 = Mahasiswa("Adachi Sakura",17)
print(mahasiswa1.count)
mahasiswa2 = Mahasiswa("Shimamura Hougetsu",17)
print(mahasiswa2.count)
mahasiswa3 = Mahasiswa("Sally",16)
print(mahasiswa3.count)