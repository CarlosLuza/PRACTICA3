"""
Problema 8:
Cree un módulo llamado operaciones.py el cual contendrá 4 funciones para realizar una suma,
una resta, un producto y una división entre dos números. Todas ellas devolverán el resultado.
En las funciones del módulo deberá de haber tratamiento e invocación manual de errores para
evitar que se quede bloqueada una funcionalidad, esto incluye:
● En caso de que se envíen valores a las funciones que no sean números, deberá
aparecer un mensaje que informe Error: Tipo de dato no válido.
● En caso de realizar una división por cero, deberá aparecer un mensaje que informe
Error: No es posible dividir entre cero.
Una vez creado el módulo, crea un script calculos.py en el mismo directorio en el que deberás
importar el módulo y ejecutar las funciones.
"""


import operaciones

if __name__ == "__main__":
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        print(f"Suma: {num1} + {num2} =", operaciones.suma(num1, num2))
        print(f"Resta: {num1} - {num2} =", operaciones.resta(num1, num2))
        print(f"Producto: {num1} * {num2} =", operaciones.producto(num1, num2))
        print(f"División: {num1} / {num2} =", operaciones.division(num1, num2))
    except ValueError:
        print("Error: Tipo de dato no válido.")
    except KeyboardInterrupt:
        print("\nOperación interrumpida por el usuario.")
