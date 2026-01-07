"""
Archivo: taller.py
Descripción:
Este módulo contiene la clase Taller, encargada de la gestión de los
vehículos dentro del sistema. Su función principal es registrar,
almacenar y mostrar los vehículos disponibles. Actúa como la capa
de servicios que maneja la lógica del negocio.
"""

class Taller:
    """
    Clase que representa un taller de vehículos.
    """

    def __init__(self, nombre):
        """
        Constructor de la clase Taller.

        :param nombre: Nombre del taller (str)
        """
        self.nombre = nombre
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        """
        Agrega un vehículo a la lista del taller.

        :param vehiculo: Objeto de tipo Vehiculo o VehiculoElectrico
        """
        self.vehiculos.append(vehiculo)

    def mostrar_vehiculos(self):
        """
        Muestra por pantalla todos los vehículos registrados en el taller.
        """
        for vehiculo in self.vehiculos:
            print(vehiculo)
