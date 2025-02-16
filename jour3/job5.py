import random

class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom
        self.vie = vie
    
    def attaquer(self, adversaire):
        degats = random.randint(5, 15)
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et inflige {degats} points de dégâts.")
    
    def est_vivant(self):
        return self.vie > 0

class Jeu:
    def __init__(self):
        self.niveau = None
    
    def choisirNiveau(self):
        print("Choisissez un niveau de difficulté :")
        print("1. Facile (PV: 100)")
        print("2. Moyen (PV: 75)")
        print("3. Difficile (PV: 50)")
        
        choix = input("Votre choix (1/2/3) : ")
        if choix == "1":
            self.niveau = 100
        elif choix == "2":
            self.niveau = 75
        elif choix == "3":
            self.niveau = 50
        else:
            print("Choix invalide, par défaut niveau Facile.")
            self.niveau = 100
    
    def lancerJeu(self):
        self.choisirNiveau()
        joueur = Personnage("Joueur", self.niveau)
        ennemi = Personnage("Ennemi", self.niveau)
        
        print(f"Le combat commence ! {joueur.nom} ({joueur.vie} PV) vs {ennemi.nom} ({ennemi.vie} PV)")
        
        while joueur.est_vivant() and ennemi.est_vivant():
            input("Appuyez sur Entrée pour attaquer...")
            joueur.attaquer(ennemi)
            if ennemi.est_vivant():
                ennemi.attaquer(joueur)
            print(f"{joueur.nom}: {joueur.vie} PV | {ennemi.nom}: {ennemi.vie} PV")
        
        self.verifierGagnant(joueur, ennemi)
    
    def verifierGagnant(self, joueur, ennemi):
        if joueur.est_vivant():
            print("Bravo ! Vous avez gagné !")
        else:
            print("Dommage, vous avez perdu...")

jeu = Jeu()
jeu.lancerJeu()
