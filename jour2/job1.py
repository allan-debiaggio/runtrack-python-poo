class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur

    def set_longueur(self, longueur):
        if longueur > 0:
            self.__longueur = longueur
        else:
            print("La longueur doit être positive.")
    
    def set_largeur(self, largeur):
        if largeur > 0:
            self.__largeur = largeur
        else:
            print("La largeur doit être positive.")

    def afficher_dimensions(self):
        print(f"Longueur: {self.__longueur}, Largeur: {self.__largeur}")

rect = Rectangle(10, 5)
rect.afficher_dimensions()

rect.set_longueur(15)
rect.set_largeur(8)

rect.afficher_dimensions()
