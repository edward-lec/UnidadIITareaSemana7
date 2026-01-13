"""
Archivo: vehiculo.py
Descripción:
Este módulo define la clase Vehiculo, que representa un vehículo genérico
dentro del sistema. Contiene los atributos comunes a todos los vehículos,
como la marca, el modelo, el año de fabricación y su disponibilidad.
Sirve como clase base para otros tipos de vehículos y permite modelar
objetos del mundo real de manera clara y estructurada.
"""

class Vehiculo:
    """
    Clase que representa un vehículo.
    """

    def __init__(self, marca, modelo, anio, disponible):
        """
        Constructor de la clase Vehiculo.

        :param marca: Marca del vehículo (str)
        :param modelo: Modelo del vehículo (str)
        :param anio: Año de fabricación (int)
        :param disponible: Estado de disponibilidad (bool)
        """
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.disponible = disponible

    def __str__(self):
        """
        Retorna una representación en texto del vehículo.
        """
        estado = "Disponible" if self.disponible else "No disponible"
        return f"{self.marca} {self.modelo} ({self.anio}) - {estado}"