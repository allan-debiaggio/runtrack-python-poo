class Animal :
    def __init__(self, age = 0, prenom = None):
        self.age = age
        print(f"L'age de l'animal est : {self.age} ans")
        self.prenom  = prenom

    def vieillir(self):
        self.age += 1
        print(f"L'age de l'animal est : {self.age} ans")

    def nommer(self, prenom):
        self.prenom = prenom
        print(f"L'animal se nomme {self.prenom}")

animal1 = Animal()
animal1.vieillir()
animal1.nommer("Barry")