from abc import ABC

class Commande(ABC):
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}
        self.__statut = "en cours"
    
    def ajouter_plat(self, nom_plat, prix):
        if self.__statut == "en cours":
            self.__plats_commandes[nom_plat] = prix
            print(f"Plat ajouté : {nom_plat} ({prix}€)")
        else:
            print("Impossible d'ajouter un plat à une commande terminée ou annulée.")
    
    def annuler_commande(self):
        if self.__statut == "en cours":
            self.__statut = "annulée"
            print("Commande annulée.")
        else:
            print("Impossible d'annuler une commande déjà terminée ou annulée.")
    
    def __calculer_total(self):
        return sum(self.__plats_commandes.values())
    
    def afficher_commande(self):
        print(f"Commande n°{self.__numero_commande} - Statut: {self.__statut}")
        for plat, prix in self.__plats_commandes.items():
            print(f"- {plat}: {prix}€")
        total = self.__calculer_total()
        print(f"Total à payer: {total}€ (TVA incluse: {self.calculer_tva(total)}€)")
    
    def calculer_tva(self, total):
        return round(total * 0.20, 2)
    
    def terminer_commande(self):
        if self.__statut == "en cours":
            self.__statut = "terminée"
            print("Commande terminée.")
        else:
            print("Impossible de terminer une commande annulée ou déjà terminée.")

def main():
    commande1 = Commande(101)
    commande1.ajouter_plat("Pizza", 12)
    commande1.ajouter_plat("Pâtes", 10)
    commande1.afficher_commande()
    commande1.terminer_commande()
    commande1.afficher_commande()
    
    commande2 = Commande(102)
    commande2.ajouter_plat("Salade", 8)
    commande2.annuler_commande()
    commande2.afficher_commande()

if __name__ == "__main__":
    main()
