class Producto:
 def __init__(self,nombre,precio,stock):
  self.nombre = nombre
  self.precio = precio
  self.stock = stock
  def verificar_disponibilidad(cantidad):
   if self.stock > cantidad:
     return f"Hay suficientes unidades"
   else:
    return f"No hay suficiente stock"
   
Producto = Producto("Laptop", 1200, 10)
Cantidad = input("Cuantas unidades desea comprar?")



