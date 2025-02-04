class Personne : 
    def __init__(self, prenom,nom) :
        self.prenom = prenom
        self.nom = nom

    def SePresenter(self) :
        prenom = self.prenom
        nom = self.nom
        print(f"Je suis {prenom} {nom}")

Personne("John","Doe").SePresenter()
Personne("Billy","Boy").SePresenter()