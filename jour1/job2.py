class Operation : 
    def __init__(self, nombre1=12, nombre2=3):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def __str__(self):
        return f"Le nombre 1 est {self.nombre1}\nLe nombre 2 est {self.nombre2}"
    
print(Operation())


