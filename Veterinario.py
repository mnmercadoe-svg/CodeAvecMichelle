class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
    def mostrar_info(self):
        print(f"El nombre del animal es {self.nombre} y pertenece a la especie {self.especie}")

class Perro(Animal):
    def __init__(self, nombre, especie, raza):
     super().__init__(nombre,especie)
     self.raza = raza
    
    def mostrar_raza(self):
        print(f"La raza del perro es {self.raza}")
        
perro1 = Perro( "Perro", "Canis lupus", "Golden")

perro1.mostrar_info()
perro1.mostrar_raza()