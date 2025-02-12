class Part:
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def change_material(self, new_material):
        self.material = new_material

    def __str__(self):
        return f"{self.name} en {self.material}"


class Ship:
    def __init__(self, name):
        self.name = name
        self.__parts = {}
        self.history = []

    def add_part(self, part):
        self.__parts[part.name] = part

    def display_state(self):
        print(f"\nÉtat actuel du {self.name}:")
        for part in self.__parts.values():
            print(part)

    def replace_part(self, part_name, new_part):
        if part_name in self.__parts:
            old_material = self.__parts[part_name].material
            self.__parts[part_name] = new_part
            self.history.append(f"Remplacement de {part_name} ({old_material}) par {new_part.material}")
        else:
            print(f"La pièce {part_name} n'existe pas.")

    def change_part(self, part_name, new_material):
        if part_name in self.__parts:
            old_material = self.__parts[part_name].material
            self.__parts[part_name].change_material(new_material)
            self.history.append(f"Modification de {part_name} ({old_material} -> {new_material})")
        else:
            print(f"La pièce {part_name} n'existe pas.")

    def display_history(self):
        print("\nHistorique des modifications:")
        for record in self.history:
            print(record)


class RacingShip(Ship):
    def __init__(self, name, max_speed):
        super().__init__(name)
        self.max_speed = max_speed

    def display_speed(self):
        print(f"Vitesse maximale: {self.max_speed} nœuds")


def main():
    ship = Ship("Navire de Thésée")
    ship.add_part(Part("Mât", "Bois"))
    ship.add_part(Part("Coque", "Bois"))
    ship.add_part(Part("Voile", "Lin"))

    while True:
        print("\nMenu:")
        print("1. Afficher l'état du navire")
        print("2. Modifier le matériau d'une pièce")
        print("3. Remplacer une pièce")
        print("4. Afficher l'historique des modifications")
        print("5. Quitter")
        choix = input("Choisissez une option: ")

        if choix == "1":
            ship.display_state()
        elif choix == "2":
            part_name = input("Nom de la pièce: ")
            new_material = input("Nouveau matériau: ")
            ship.change_part(part_name, new_material)
        elif choix == "3":
            part_name = input("Nom de la pièce à remplacer: ")
            new_material = input("Matériau de la nouvelle pièce: ")
            ship.replace_part(part_name, Part(part_name, new_material))
        elif choix == "4":
            ship.display_history()
        elif choix == "5":
            break
        else:
            print("Option invalide, veuillez réessayer.")


if __name__ == "__main__":
    main()
