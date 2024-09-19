class Automasina:
    def __init__(self,marka,modelis,krasa):
        self.marka = marka
        self.modelis = modelis
        self.krasa = krasa

    def printet(self):
        print(f"{self.modelis} modelis ar krasu {self.krasa}")
        
audi = Automasina("Audi", "a4", "sarkana")
bmw = Automasina("Bmw", "m5", "balts")

audi.printet()
bmw.printet()

    