class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"Marque: {self.marque}, Modèle: {self.modele}, Année: {self.annee}, Prix: {self.prix}€")
    
    def demarrer(self):
        print("Attention, je roule")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de portes: {self.portes}")
    
    def demarrer(self):
        print("La voiture démarre en douceur...")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roues = 2
    
    def informationsVehicule(self):
        super().informationsVehicule()
        print(f"Nombre de roues: {self.roues}")
    
    def demarrer(self):
        print("La moto vrombit et démarre !")

voiture = Voiture("Toyota", "Corolla", 2022, 25000)
voiture.informationsVehicule()
voiture.demarrer()

print("\n")

moto = Moto("Yamaha", "R1", 2023, 18000)
moto.informationsVehicule()
moto.demarrer()
