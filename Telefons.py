class Telefons:
    def __init__(self,marka,modelis,gads,cena):
        self.marka = marka
        self.modelis = modelis
        self.gads = gads 
        self.cena = cena
    
    def printet(self):
        print(f"{self.modelis} modelis ražots {self.gads}.")
        