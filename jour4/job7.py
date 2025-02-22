import random

class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur
    
    def __repr__(self):
        return f"{self.valeur} de {self.couleur}"
    
    def get_valeur(self):
        if self.valeur in ['Valet', 'Dame', 'Roi']:
            return 10
        elif self.valeur == 'As':
            return 11
        else:
            return int(self.valeur)

class Jeu:
    def __init__(self):
        self.paquet = []
        self.creer_paquet()
        random.shuffle(self.paquet)
    
    def creer_paquet(self):
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        valeurs = [str(i) for i in range(2, 11)] + ['Valet', 'Dame', 'Roi', 'As']
        self.paquet = [Carte(valeur, couleur) for valeur in valeurs for couleur in couleurs]
    
    def piocher(self):
        return self.paquet.pop() if self.paquet else None

def calculer_score(main):
    score = sum(carte.get_valeur() for carte in main)
    nombre_as = sum(1 for carte in main if carte.valeur == 'As')
    while score > 21 and nombre_as:
        score -= 10
        nombre_as -= 1
    return score

def jouer_blackjack():
    jeu = Jeu()
    joueur_main = [jeu.piocher(), jeu.piocher()]
    croupier_main = [jeu.piocher(), jeu.piocher()]
    
    print(f"Votre main: {joueur_main} (Score: {calculer_score(joueur_main)})")
    print(f"Carte visible du croupier: {croupier_main[0]}")
    
    while calculer_score(joueur_main) < 21:
        action = input("Voulez-vous prendre une carte (p) ou passer (s) ? ").lower()
        if action == 'p':
            joueur_main.append(jeu.piocher())
            print(f"Votre main: {joueur_main} (Score: {calculer_score(joueur_main)})")
        else:
            break
    
    if calculer_score(joueur_main) > 21:
        print("Vous avez dépassé 21. Vous perdez !")
        return
    
    print(f"Main du croupier: {croupier_main} (Score: {calculer_score(croupier_main)})")
    while calculer_score(croupier_main) < 17:
        croupier_main.append(jeu.piocher())
        print(f"Le croupier pioche : {croupier_main} (Score: {calculer_score(croupier_main)})")
    
    score_joueur = calculer_score(joueur_main)
    score_croupier = calculer_score(croupier_main)
    
    if score_croupier > 21 or score_joueur > score_croupier:
        print("Félicitations, vous avez gagné !")
    elif score_joueur < score_croupier:
        print("Le croupier gagne.")
    else:
        print("Égalité !")

if __name__ == "__main__":
    jouer_blackjack()
