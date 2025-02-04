class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages if isinstance(pages, int) and pages > 0 else 0

    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_pages(self):
        return self.__pages
    
    def set_titre(self, titre):
        self.__titre = titre
    
    def set_auteur(self, auteur):
        self.__auteur = auteur
    
    def set_pages(self, pages):
        if isinstance(pages, int) and pages > 0:
            self.__pages = pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

    def afficher_info(self):
        print(f"Titre: {self.__titre}, Auteur: {self.__auteur}, Pages: {self.__pages}")

livre = Livre("1984", "George Orwell", 328)
livre.afficher_info()

livre.set_titre("Animal Farm")
livre.set_auteur("George Orwell")
livre.set_pages(112)

livre.afficher_info()

livre.set_pages(-50)
