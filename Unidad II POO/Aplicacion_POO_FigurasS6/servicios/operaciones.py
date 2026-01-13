# servicios/operaciones.py

def mostrar_area(figura):
    """
    Función que recibe un objeto de tipo Figura.
    Aplica polimorfismo, ya que el método calcular_area()
    se ejecuta según la clase real del objeto recibido.
    """
    print(f"Área calculada: {figura.calcular_area():.2f}")

