class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        self.buts += 1
        print(f"{self.nom} a marqué un but !")

    def effectuerUnePasseDecisive(self):
        self.passes_decisives += 1
        print(f"{self.nom} a réalisé une passe décisive !")

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes += 1
        print(f"{self.nom} a reçu un carton jaune !")

    def recevoirUnCartonRouge(self):
        self.cartons_rouges += 1
        print(f"{self.nom} a reçu un carton rouge !")

    def afficherStatistiques(self):
        print(f"Statistiques de {self.nom} (#{self.numero}, {self.position}):")
        print(f"  - Buts marqués: {self.buts}")
        print(f"  - Passes décisives: {self.passes_decisives}")
        print(f"  - Cartons jaunes: {self.cartons_jaunes}")
        print(f"  - Cartons rouges: {self.cartons_rouges}")
        print("--------------------------------")


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)
        print(f"{joueur.nom} a été ajouté à l'équipe {self.nom}.")

    def afficherStatistiquesJoueurs(self):
        print(f"Statistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom_joueur, action):
        for joueur in self.joueurs:
            if joueur.nom == nom_joueur:
                if action == "but":
                    joueur.marquerUnBut()
                elif action == "passe":
                    joueur.effectuerUnePasseDecisive()
                elif action == "jaune":
                    joueur.recevoirUnCartonJaune()
                elif action == "rouge":
                    joueur.recevoirUnCartonRouge()
                break
        else:
            print(f"Joueur {nom_joueur} non trouvé dans l'équipe {self.nom}.")


equipe1 = Equipe("Les Lions")
equipe2 = Equipe("Les Tigres")

joueur1 = Joueur("Paul", 10, "Attaquant")
joueur2 = Joueur("Lucas", 8, "Milieu")
joueur3 = Joueur("Hugo", 5, "Défenseur")
joueur4 = Joueur("Antoine", 9, "Attaquant")
joueur5 = Joueur("Mathieu", 6, "Milieu")

equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur3)
equipe2.ajouterJoueur(joueur4)
equipe2.ajouterJoueur(joueur5)

print("\n--- Avant le match ---")
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

equipe1.mettreAJourStatistiquesJoueur("Paul", "but")
equipe1.mettreAJourStatistiquesJoueur("Lucas", "passe")
equipe2.mettreAJourStatistiquesJoueur("Antoine", "but")
equipe2.mettreAJourStatistiquesJoueur("Mathieu", "passe")
equipe1.mettreAJourStatistiquesJoueur("Lucas", "jaune")
equipe2.mettreAJourStatistiquesJoueur("Hugo", "rouge")

print("\n--- Après le match ---")
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()
