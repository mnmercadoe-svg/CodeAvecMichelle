class Estudiante():
    def __init__(self,nombre,edad,calificacion): 
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion  
        
    def aprobar(self):
        if self.calificacion >= 3.0:
         print(f"El estudiante {self.nombre} aprobo la asignatura")
        else: 
         print(f"El estudiante reprobo la asignatura")
            
    def mostrar_info(self):
        print(f"El estudiante {self.nombre}, tiene {self.edad} años y obtuvo una calificacion de {self.calificacion} ")
        

Estudiante1 = Estudiante("Marie",20,4.5)
Estudiante2 = Estudiante("Jean", 18, 3.2)
Estudiante3 = Estudiante("Angèle", 21, 1.5)

Estudiante1.mostrar_info()
Estudiante1.aprobar()
Estudiante2.mostrar_info()
Estudiante2.aprobar()
Estudiante3.mostrar_info()
Estudiante3.aprobar()
    