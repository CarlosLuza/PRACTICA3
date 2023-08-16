"""
Problema 5:
Cree una clase Alumno e inicialícela con el nombre y el número de registro. Haga los métodos
para:
1. Display - Debe mostrar toda la información del estudiante (nombre y número de
registro).
2. setAge - Debe asignar la edad al estudiante
3. setNota - Debe asignar las notas al estudiante.
"""
class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []
        
    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.notas:
            print("Notas:")
            for i, nota in enumerate(self.notas, start=1):
                print(f"Nota {i}: {nota}")
                
    def setAge(self, edad):
        self.edad = edad
        
    def setNota(self, notas):
        self.notas = notas
nombre_alumno = input("Ingrese el nombre del alumno: ")
numero_registro_alumno = input("Ingrese el número de registro del alumno: ")
alumno = Alumno(nombre_alumno, numero_registro_alumno)
edad_alumno = int(input("Ingrese la edad del alumno: "))
alumno.setAge(edad_alumno)

num_notas = int(input("Ingrese el número de notas del alumno: "))
notas_alumno = []
for i in range(num_notas):
    nota = float(input(f"Ingrese la nota {i + 1}: "))
    notas_alumno.append(nota)
alumno.setNota(notas_alumno)

print("\nInformación del Alumno:")
alumno.display()
