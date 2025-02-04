class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0
        self.__level = self.__student_eval()
    
    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__student_eval()
        else:
            print("Erreur : le nombre de crédits ajoutés doit être supérieur à zéro.")
    
    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    
    def student_info(self):
        print(f"Nom: {self.__nom}\nPrénom: {self.__prenom}\nID: {self.__numero_etudiant}\nCrédits: {self.__credits}\nNiveau: {self.__level}")

john_doe = Student("Doe", "John", 145)

john_doe.add_credits(30)
john_doe.add_credits(25)
john_doe.add_credits(40)

john_doe.student_info()
