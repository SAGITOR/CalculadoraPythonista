import math

def funcion_logaritmo_base_10(argumento):
    """
    Calcula el logaritmo en base 10 de un número.

    Args:
    argumento (float): El número del cual se calculará el logaritmo en base 10.

    Returns:
    float: El valor del logaritmo en base 10 del número.
    """
    return math.log10(argumento)

def main():
    resultado = 0
    print("Ingrese el número de la opcion de la operacion avanzada que desea realizar: ")
    operacion = int(input("1 = logaritmo en base 10: "))
    
    if (operacion < 1 or operacion > 1):
        return print("Opción no válida")
    else:
        if (operacion in [1, 2, 3]):
            argumento = float(input("Ingrese el argumento: "))
            
            if ( argumento == 0 ):
                return print("Error en el calculo del logaritmo natural: El argumento debe ser mayor a 0")
            elif (operacion == 1):
                resultado = funcion_logaritmo_base_10(argumento)

        return print(f"El resultado de la operación es: {resultado}")

main()