class Mahasiswa:
    count = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        # variabel instance private
        self.__private = "private"
        # variabel instance protected
        self._protected = "Shimamura"

    


adachi = Mahasiswa("Adachi Sakura",17)
print(adachi.__dict__)

adachi.protected = "awa"
print(adachi._protected)