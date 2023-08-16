
"""
Problema 1:
Implemente un programa que solicite al usuario una fracción, con
formato X/Y, donde cada uno de X e Y es un número entero, y luego
muestra, como un porcentaje redondeado al número entero más
cercano, donde se indicará la cantidad de combustible en el
tanque. Se debe tener en cuenta los siguientes casos:
- Colocar E en caso X/Y sea menor a 1% del total
- Colocar F en caso X/Y sea mayor a 99%.
- En otro caso, devolver el valor en porcentaje %
También debe tomar en cuenta los siguientes casos:
- X y Y deben ser números enteros
- X debe ser mayor o igual a Y, y Y != 0
De no cumplirse estos casos, se debe volver a preguntar al usuario. Asegúrese de detectar
cualquier excepción como ValueError o ZeroDivisionError.
Ejemplos:
- Input: 4/0 Acción: Volver a preguntar al usuario dada la excepción ZeroDivisionError
- Input 1.5/3 Acción: Error dado que solo se permiten números enteros ValueError
- Input 5/4 Acción: Volver a preguntar al usuario
- Input 3/4 Output: 75%
- Input 4/4: Output F
Nota: Le será de utilidad aplicar

"""

def main():
    while True:
        try:
            entrada = input("Ingrese una fracción en formato X/Y: ")
            numerador, denominador = map(int, entrada.split('/'))
            
            if denominador == 0:
                raise ZeroDivisionError
            
            if numerador < denominador:
                porcentaje = numerador / denominador * 100
                if porcentaje < 1:
                    resultado = "E"
                elif porcentaje > 99:
                    resultado = "F"
                else:
                    resultado = f"{round(porcentaje)}%"
            elif numerador == denominador:
                resultado = "F"
            else:
                print("El numerador debe ser menor o igual que el denominador.")
                continue
            
            print(f"La cantidad de combustible en el tanque es: {resultado}")
            break
            
        except ValueError:
            print("Formato incorrecto. Ingrese dos números enteros separados por '/'")
        except ZeroDivisionError:
            print("El denominador no puede ser cero.")
            
if __name__ == "__main__":
    main()
