class Rectangulo:
    def __init__(self, largo, ancho):
        self.__largo = largo
        self.__ancho = ancho 
        
    
    def cambiar_dimensiones(self, nuevo_largo, nuevo_ancho):
        if nuevo_largo > 0:
            self.__largo = nuevo_largo
        else:
            print("El largo debe ser mayor que 0")
        
        if nuevo_ancho > 0:
            self.__ancho = nuevo_ancho
        else:
            print("El ancho debe ser mayor que 0")
    
    def calcular_area(self):
        self.area = self.__largo * self.__ancho
    
    def mostrar_area(self):
        print(f"El area del rectangulo es {self.area}")
    
    def calcular_perimetro(self):
        self.perimetro = 2 *(self.__largo + self.__ancho)
    
    def mostrar_perimetro(self):
        print(f"El perimetro del rectangulo es {self.perimetro}")
    def mostrar_dimensiones(self):
        print(f"Las dimensiones actuales del rectangulo son largo {self.__largo} y ancho {self.__ancho}")

        
rectangulo1 = Rectangulo(15,10)
rectangulo1.cambiar_dimensiones(8,4)
rectangulo1.calcular_area()
rectangulo1.mostrar_area()
rectangulo1.calcular_perimetro ()
rectangulo1.mostrar_perimetro()
rectangulo1.mostrar_dimensiones()