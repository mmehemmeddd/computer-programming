class PartyAnimal:
    def __init__(self):
        self.x = 0

    # İndi bu metod class-ın içindədir
    def party(self):
        self.x = self.x + 1
        print("So far", self.x)


an = PartyAnimal()
an.party()
an.party()
an.party()