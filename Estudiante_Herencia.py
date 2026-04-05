class Persona: 
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_info(self):
        print(f"El nombre es {self.nombre} y la edad es {self.edad}")


class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad) 
        self.grado = grado

    def mostrar_grado(self):
        print(f"El grado del estudiante es {self.grado}")


estudiante1 = Estudiante("Valentina", 20, 4.5)
estudiante1.mostrar_info()
estudiante1.mostrar_grado()