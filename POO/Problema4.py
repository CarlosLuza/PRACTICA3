"""
Problema 4:
Definir una clase llamada “RECTANGULO” que puede ser construida por los atributos largo y
ancho. La clase “RECTANGULO” debe tener un método que puede calcular el área utilizando los
atributos de la clase.
"""

class RECTANGULO:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
        
    def calcular_area(self):
        area = self.largo * self.ancho
        return area
largo_rectangulo = float(input("Ingrese el largo del rectángulo: "))
ancho_rectangulo = float(input("Ingrese el ancho del rectángulo: "))
rectangulo = RECTANGULO(largo_rectangulo, ancho_rectangulo)
area = rectangulo.calcular_area()
print(f"El área del rectángulo con largo {largo_rectangulo} y ancho {ancho_rectangulo} es: {area:.2f}")
