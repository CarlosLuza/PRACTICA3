"""
Problema 2:
Cree un programa que solicite al usuario una lista de calificaciones separadas por comas. Divida
la cadena en calificaciones individuales y almacénelas en una lista para luego convertir cada
calificación en un entero. Deberá utilizar una sentencia try/except para informar al usuario
cuando los valores introducidos no puedan ser convertidos debido a un error de tipeo o
formato. (Los métodos de cadena le serán de utilidad)
"""

def main():
    while True:
        try:
            calificaciones_str = input("Ingrese las calificaciones separadas por comas: ")
            calificaciones = calificaciones_str.split(',')
            
            calificaciones_enteros = []
            for calificacion in calificaciones:
                try:
                    calificacion_entero = int(calificacion.strip())
                    calificaciones_enteros.append(calificacion_entero)
                except ValueError:
                    print(f"La calificación '{calificacion}' no es un número entero válido.")
            
            if calificaciones_enteros:
                print("Calificaciones enteras convertidas:", calificaciones_enteros)
                break
            else:
                print("No se encontraron calificaciones válidas. Intente nuevamente.")
                
        except Exception as e:
            print("Ocurrió un error:", e)
            
if __name__ == "__main__":
    main()
