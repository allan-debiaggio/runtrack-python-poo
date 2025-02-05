class Ville:
    def __init__(self, nom, habitants):
        self.__nom = nom
        self.__habitants = habitants
    
    def ajouter_habitant(self):
        self.__habitants += 1
    
    def get_habitants(self):
        return self.__habitants
    
    def get_nom(self):
        return self.__nom


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.__ville.ajouter_habitant()


paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

print(f"Habitants à Paris : {paris.get_habitants()}")
print(f"Habitants à Marseille : {marseille.get_habitants()}")

john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

print(f"Habitants à Paris après l'arrivée de John et Myrtille : {paris.get_habitants()}")
print(f"Habitants à Marseille après l'arrivée de Chloé : {marseille.get_habitants()}")