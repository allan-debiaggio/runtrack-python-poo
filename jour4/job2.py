class Personne:
    def __init__(self, age=14):
        self.age = age
    
    def afficherAge(self):
        print(f"J'ai {self.age} ans")
    
    def bonjour(self):
        print("Hello")
    
    def modifierAge(self, nouvel_age):
        self.age = nouvel_age

class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")
    
    def afficherAge(self):
        print(f"J’ai {self.age} ans")

class Professeur(Personne):
    def __init__(self, age=14, matiereEnseignee=""):
        super().__init__(age)
        self.__matiereEnseignee = matiereEnseignee
    
    def enseigner(self):
        print("Le cours va commencer")

p = Personne()
p.bonjour()
p.afficherAge()
p.modifierAge(30)
p.afficherAge()

e = Eleve()
e.bonjour()
e.allerEnCours()
e.modifierAge(15)
e.afficherAge()

prof = Professeur(age=40, matiereEnseignee="Mathématiques")
prof.bonjour()
prof.enseigner()
prof.afficherAge()
