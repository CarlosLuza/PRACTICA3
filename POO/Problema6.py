import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return "Primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "Segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "Tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "Cuarto cuadrante"
        elif self.x == 0 and self.y != 0:
            return "Sobre eje Y"
        elif self.x != 0 and self.y == 0:
            return "Sobre eje X"
        else:
            return "Origen"
    
    def vector(self, otro_punto):
        return Punto(otro_punto.x - self.x, otro_punto.y - self.y)
    
    def distancia(self, otro_punto):
        dx = otro_punto.x - self.x
        dy = otro_punto.y - self.y
        distancia = math.sqrt(dx**2 + dy**2)
        return distancia

class Rectangulo:
    def __init__(self, punto_inicial=Punto(), punto_final=Punto()):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final
    
    def base(self):
        return abs(self.punto_final.x - self.punto_inicial.x)
    
    def altura(self):
        return abs(self.punto_final.y - self.punto_inicial.y)
    
    def area(self):
        return self.base() * self.altura()

# Ingreso de coordenadas por el usuario
x1 = float(input("Ingrese la coordenada x del punto 1: "))
y1 = float(input("Ingrese la coordenada y del punto 1: "))
x2 = float(input("Ingrese la coordenada x del punto 2: "))
y2 = float(input("Ingrese la coordenada y del punto 2: "))

# Creación de objetos Punto y Rectangulo
punto1 = Punto(x1, y1)
punto2 = Punto(x2, y2)

print(f"Distancia entre Punto 1 y Punto 2: {punto1.distancia(punto2)}")

rectangulo = Rectangulo(punto1, punto2)
print(f"Base del rectángulo: {rectangulo.base()}")
print(f"Altura del rectángulo: {rectangulo.altura()}")
print(f"Área del rectángulo: {rectangulo.area()}")

