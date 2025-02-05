class Tache:
    def __init__(self, titre, description, statut="À faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

    def marquerCommeFinie(self):
        self.statut = "Terminée"

    def __str__(self):
        return f"{self.titre} - {self.description} [{self.statut}]"


class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        self.taches = [tache for tache in self.taches if tache.titre != titre]

    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.marquerCommeFinie()
                break

    def afficherListe(self):
        return [str(tache) for tache in self.taches]

    def filterListe(self, statut):
        return [str(tache) for tache in self.taches if tache.statut == statut]

tache1 = Tache("Faire les courses", "Acheter du pain et du lait")
tache2 = Tache("Sport", "Aller courir 30 minutes")
tache3 = Tache("Lecture", "Lire 20 pages du livre en cours")

liste = ListeDeTaches()

liste.ajouterTache(tache1)
liste.ajouterTache(tache2)
liste.ajouterTache(tache3)

print("Toutes les tâches :", liste.afficherListe())

liste.supprimerTache("Sport")
print("Après suppression :", liste.afficherListe())

liste.marquerCommeFinie("Faire les courses")
print("Après mise à jour du statut :", liste.afficherListe())

print("Tâches à faire :", liste.filterListe("À faire"))
