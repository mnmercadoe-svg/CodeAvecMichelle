class Libro():
    def __init__(self,titulo,autor,num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas
        
    def mostrar_libro(self):
     print(f"El libro seleccionado es: {self.titulo} fue escrito por {self.autor} y tiene {self.num_paginas} paginas")

    def actualizar_paginas(self):
     nuevo_num = input("Cual es el numero de paginas actualizado?")
     self.num_paginas = nuevo_num
     


Livre1 = Libro("Les Misérables","Victor Hugo", 510)
Livre2 = Libro("Le Petit Prince", "Antoine de Saint-Exupéry",96)
Livre3 = Libro("Les Trois Mousquetaires","Alexandre Dumas",625)


Livre1.mostrar_libro()
Livre1.actualizar_paginas()
Livre1.mostrar_libro()

print()

Livre2.mostrar_libro()
Livre2.actualizar_paginas()
Livre2.mostrar_libro()

print()

Livre3.mostrar_libro()
Livre3.actualizar_paginas()
Livre3.mostrar_libro()

