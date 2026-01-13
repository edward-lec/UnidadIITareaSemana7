# modelos/Circulo.py

from .Figura import Figura
import math

class Circulo(Figura):
    """
    Clase Circulo que hereda de la clase Figura.
    Representa un círculo y redefine el cálculo del área.
    """

    def __init__(self, radio):
        """
        Constructor de la clase Circulo.
        :param radio: Radio del círculo
        """
        # Herencia: se inicializa el atributo nombre
        # usando el constructor de la clase base
        super().__init__("Círculo")

        # Encapsulación: atributo protegido
        self._radio = radio

    def calcular_area(self):
        """
        Sobrescritura del método calcular_area().
        Aplica polimorfismo ya que redefine el comportamiento
        del método de la clase base Figura.
        """
        return math.pi * self._radio ** 2

    def mostrar_datos(self):
        """
        Retorna la información completa del círculo,
        incluyendo su radio y área.
        """
        return (
            f"{self._nombre} | "
            f"Radio: {self._radio} | "
            f"Área: {self.calcular_area():.2f}"
        )
