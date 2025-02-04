class Point:
    def __init__(self, x, y) :
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        print(f"Coordonnée X = {self.x}\nCoordonnée Y = {self.y}")

    def afficherX(self):
        print(f"Coordonnée X seule = {self.x}")

    def afficherY(self):
        print(f"Coordonnée Y seule = {self.y}")

    def changerX(self):
        self.x = int(input("Quelle est la nouvelle valeur de X ? "))
        print(f"Nouvelle coordonnée X = {self.x}")

    def changerY(self):
        self.y = int(input("Quelle est la nouvelle valeur de Y ? "))
        print(f"Nouvelle coordonnée Y = {self.y}")

Point(14, -12).afficherLesPoints()
Point(8, 42).afficherX()
Point(8,42).afficherY()
Point(8,42).changerX()
Point(8,42).changerY()