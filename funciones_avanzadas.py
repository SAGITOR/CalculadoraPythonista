def suma(sumando_1, sumando_2):
    """
    Esta función realiza una suma de dos números.

    Args:
    sumando_1 (float): El primer número a sumar.
    sumando_2 (float): El segundo número a sumar.

    Returns:
    float: La suma de sumando_1 y sumando_2.
    """
    return sumando_1 + sumando_2

def main():
    resultado = 0
    print("Ingrese el número de la opcion de la operacion basica que desea realizar: ")
    operacion = int(input("1 = suma: "))

    
    if (operacion < 1 or operacion > 1):
        return print("Opción no válida")
    else:
        if (operacion == 1): 
            sumando_1 = float(input("sumando 1: "))
            sumando_2 = float(input("sumando 2: "))
            resultado = suma(sumando_1, sumando_2)
        
        print(f"El resultado de la operacion es: {resultado}")

main()