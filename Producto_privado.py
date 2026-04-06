class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio


    def cambiar_precio(self):
        nuevo_precio = int(input("Cual es el nuevo precio del producto ?"))
        if nuevo_precio > 0:
            self.__precio =  nuevo_precio 
            print(f"El nuevo precio del producto es {self.__precio}")
            
        else:
            print("El nuevo precio debe ser mayor que  0")


    def mostrar_precio(self):
        print(f"El precio actual del producto es {self.__precio}")


    def mostrar_nombre(self):
        print(f"El nombre del producto es {self.__nombre}")
    
    def aplicar_descuento(self,descuento):
        
        if descuento > 0 and descuento < 100:
            self.__precio = (self.__precio * descuento) / 100
            print(f"El precio final del producto con descuento aplicado es {self.__precio}")
        else:
            print("Error")
            
        


producto1 = Producto("Brownie con helado de vainilla", 30000)

producto1.cambiar_precio()
producto1.mostrar_precio()
producto1.mostrar_nombre()
producto1.aplicar_descuento(20)
