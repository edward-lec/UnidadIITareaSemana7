# modelos/Figura.py

class Figura:
    """
    Clase base Figura.
    Representa una figura geométrica genérica.
    Aplica encapsulación y polimorfismo.
    """

    def __init__(self, nombre):
        """
        Constructor de la clase Figura.
        :param nombre: Nombre de la figura
        """
        # Encapsulación: atributo protegido
        self._nombre = nombre

    def calcular_area(self):
        """
        Método que calcula el área de la figura.
        Este método será sobrescrito por las clases hijas
        para aplicar el concepto de polimorfismo.
        """
        return 0

    def mostrar_datos(self):
        """
        Retorna una cadena con la información básica
        de la figura.
        """
        return f"Figura: {self._nombre}"
