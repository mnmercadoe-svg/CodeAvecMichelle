class Vehiculo:
    def __init__(self, marca, año):
        self.marca = marca
        self.año = año 
    def mostrar_info(self):
        print(f"La marca del vehiculo es {self.marca} y el año es {self.año}")
class Coche(Vehiculo):
    def __init__(self, marca, año, modelo):
        super().__init__(marca, año)
        self.modelo = modelo 
    def mostrar_modelo(self):
        print(f"El modelo del vehiculo es {self.modelo}")

coche1 = Coche("BMW", 2025, "M5")
coche1.mostrar_info()
coche1.mostrar_modelo()