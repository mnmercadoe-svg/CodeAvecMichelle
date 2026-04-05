class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima, velocidad_actual):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = velocidad_actual

    def acelerar(self, incremento):
        self.incremento = incremento
        self.velocidad_actual = self.velocidad_actual + incremento
        print(f"La nueva velocidad del vehiculo es {self.incremento} km/h")

    def frenar(self, decremento):
        self.decremento = decremento
        print("Usted a frenado el carro")
        print(f"La nueva velocidad del vehiculo es {self.decremento} km/h")

    def verficar_limite(self, velocidad_limite):
        if velocidad_actual > velocidad_maxima:
            print("Usted ha excedido el limite de velocidad")
            return True
        else:
            print("Aun se encuentra dentro del limite de velocidad")
            return False


Carro = Vehiculo("Porsche", 2019, 300, 150)

while True:

    print("Menu")
    print("Acelerar = 1")
    print("Frenar = 2")
    print("Verificar limite de velocidad = 3")
    print("Salir del programa = 4")
    opcion = int(input("Por favor seleccione la opcion correspondiente a la accion que desea realizar" ))
    if opcion == 1:
        Carro.acelerar(15)
    elif opcion == 2:
        Carro.frenar(150)
    elif opcion == 3:
        Carro.verficar_limite(Carro.velocidad_actual)
    elif opcion == 4:
        break
