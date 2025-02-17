class Produit:
    def __init__(self, nom, prixHT, TVA):
        self._nom = nom
        self._prixHT = prixHT
        self._TVA = TVA

    def calculer_prix_TTC(self):
        return self._prixHT * (1 + self._TVA / 100)

    def afficher(self):
        return f"Produit: {self._nom}, Prix HT: {self._prixHT:.2f}€, TVA: {self._TVA}%, Prix TTC: {self.calculer_prix_TTC():.2f}€"
    
    def set_nom(self, nouveau_nom):
        self._nom = nouveau_nom
    
    def set_prixHT(self, nouveau_prixHT):
        self._prixHT = nouveau_prixHT
    
    def get_nom(self):
        return self._nom
    
    def get_prixHT(self):
        return self._prixHT
    
    def get_TVA(self):
        return self._TVA
    
produit1 = Produit("Ordinateur", 1000, 20)
produit2 = Produit("Smartphone", 800, 20)
produit3 = Produit("Tablette", 500, 10)

print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())

produit1.set_nom("PC Gamer")
produit1.set_prixHT(1200)
produit2.set_nom("iPhone")
produit2.set_prixHT(900)
produit3.set_nom("iPad")
produit3.set_prixHT(550)

print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())
