# main.py

from modelos.Figura import Figura
from modelos.Circulo import Circulo
from servicios.operaciones import mostrar_area

# Creación de objetos (instancias de clases)
figura_generica = Figura("Figura Genérica")
circulo1 = Circulo(5)

# Uso de métodos para demostrar el funcionamiento del programa
print(figura_generica.mostrar_datos())
mostrar_area(figura_generica)

print(circulo1.mostrar_datos())
mostrar_area(circulo1)
