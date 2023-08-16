
"""
Problema 3:
Definir una clase llamada “CIRCULO” la cual contenga un atributo inicializador radio. La clase
“CIRCULO” debe tener un método que puede calcular el área en utilizando el atributo radio
"""
import math

class CIRCULO:
    def __init__(self, radio):
        self.radio = radio
        
    def calcular_area(self):
        area = math.pi * (self.radio ** 2)
        return area
radio_circulo = float(input("Ingrese el radio del círculo: "))
circulo = CIRCULO(radio_circulo)
area = circulo.calcular_area()
print(f"El área del círculo con radio {radio_circulo} es: {area:.2f}")
