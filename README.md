
**1. Introducción**

La Programación Orientada a Objetos (POO) es un paradigma de programación que permite estructurar el código de manera organizada, reutilizable y fácil de mantener. Este paradigma se basa en la creación de clases y objetos, y en el uso de principios fundamentales como la encapsulación, la herencia y el polimorfismo.

En el presente trabajo se desarrolló un programa en Python utilizando el IDE PyCharm, con el objetivo de aplicar de forma práctica los conceptos aprendidos de POO. El programa fue estructurado adecuadamente y posteriormente preparado para su publicación en un repositorio de GitHub.

**2. Objetivo**

Aplicar los conocimientos adquiridos sobre Programación Orientada a Objetos mediante el desarrollo de un programa en Python que implemente:

Definición de una clase base y una clase derivada.

Uso de herencia entre clases.

Aplicación de encapsulación en los atributos.

Implementación de polimorfismo mediante métodos sobrescritos.

Creación de objetos y demostración de su funcionamiento.

**3. Descripción del programa**

El programa desarrollado corresponde a un sistema de figuras geométricas, en el cual se define una figura genérica y una figura específica (círculo). Para una mejor organización del código, se utilizó una arquitectura por capas separando los modelos y los servicios.

**3.1 Arquitectura del proyecto**

El proyecto se organizó de la siguiente manera:

**modelos/:** contiene las clases principales del sistema.

Figura.py: clase base.

Circulo.py: clase derivada.

**servicios/:** contiene funciones que operan sobre los objetos.

operaciones.py.

main.py: archivo principal que ejecuta el programa.

Esta estructura permite una mejor legibilidad, mantenimiento y escalabilidad del código.

**4. Aplicación de los conceptos de POO**
**4.1 Definición de clases y objetos**

Se definió la clase base Figura, la cual representa una figura geométrica genérica. A partir de esta clase se creó la clase Circulo, que representa una figura específica.

En el archivo main.py se crearon instancias de estas clases (objetos) para demostrar su funcionamiento.

**4.2 Herencia**

La herencia se implementó cuando la clase Circulo hereda de la clase Figura. Esto permite que la clase derivada reutilice atributos y métodos de la clase base, evitando la duplicación de código.

Ejemplo conceptual:

Clase base: Figura

Clase derivada: Circulo(Figura)

**4.3 Encapsulación**

La encapsulación se aplicó utilizando atributos protegidos, identificados por el prefijo _. Estos atributos no deben ser accedidos directamente desde fuera de la clase, sino a través de métodos.

Ejemplos de atributos encapsulados:

_nombre

_radio

Esto protege la información interna de las clases y mejora la seguridad del código.

**4.4 Polimorfismo**

El polimorfismo se evidenció mediante la sobrescritura del método calcular_area(). Este método existe tanto en la clase Figura como en la clase Circulo, pero su implementación es diferente en cada una.

Gracias al polimorfismo, el mismo método puede comportarse de manera distinta según el tipo de objeto que lo invoque.

Además, se implementó una función en el módulo de servicios que recibe objetos de tipo Figura y ejecuta el método correspondiente sin importar la clase concreta del objeto.

**5. Demostración del funcionamiento**

En el archivo main.py se crearon instancias de las clases y se utilizaron sus métodos para mostrar información y calcular áreas. Al ejecutar el programa, se obtienen resultados correctos que demuestran el uso de herencia, encapsulación y polimorfismo.

Esto confirma que el programa cumple con todos los requisitos planteados en la tarea.

**6. Conclusión**

En conclusión, el programa desarrollado cumple satisfactoriamente con los principios de la Programación Orientada a Objetos en Python. Se implementaron correctamente la herencia, la encapsulación y el polimorfismo, además de definir adecuadamente clases, atributos y métodos.

La correcta organización del proyecto en carpetas de modelos y servicios facilita la comprensión y el mantenimiento del código. Este trabajo permitió reforzar los conocimientos teóricos de POO mediante su aplicación práctica, logrando un programa funcional, ordenado y bien documentado.
