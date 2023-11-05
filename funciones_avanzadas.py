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

def funcion_logaritmo_base_x(base, argumento):
    """
    Calcula el logaritmo en base x de un número.

    Args:
    base (float): La base del logaritmo.
    argumento (float): El número del cual se calculará el logaritmo.

    Returns:
    float: El valor del logaritmo en base x del número.
    """
    return math.log(argumento, base)

def funcion_logaritmo_natural(argumento):
    """
    Calcula el logaritmo natural (en base e) de un número.

    Args:
    argumento (float): El número del cual se calculará el logaritmo natural.

    Returns:
    float: El valor del logaritmo natural del número.
    """
    return math.log(argumento)

def funcion_seno(angulo_grados):
    """
    Calcula el seno de un ángulo en grados.

    Args:
    angulo_grados (float): El ángulo en grados.

    Returns:
    float: El valor del seno del ángulo.
    """
    angulo_radianes = math.radians(angulo_grados)
    return math.sin(angulo_radianes)

def main():
    resultado = 0
    print("Ingrese el número de la opcion de la operacion avanzada que desea realizar: ")
    operacion = int(input("1 = logaritmo en base 10, 2 = logaritmo en base x, 3 = logaritmo natural, 4 = función seno: "))
    
    if (operacion < 1 or operacion > 4):
        return print("Opción no válida")
    else:
        if ( operacion in [1, 2, 3] ):
            argumento = float(input("Ingrese el argumento: "))
            
            if ( argumento == 0 ):
                return print("Error en el calculo del logaritmo natural: El argumento debe ser mayor a 0")
            elif (operacion == 1):
                resultado = funcion_logaritmo_base_10(argumento)
            elif (operacion == 2):
                base = float(input("Ingrese la base del logaritmo: "))
                resultado = funcion_logaritmo_base_x(base, argumento)
            elif (operacion == 3):
                resultado = funcion_logaritmo_natural(argumento)
        elif ( operacion in [4, 5, 6] ):
            angulo_grados = float(input("Ingrese el ángulo en grados: "))
            
            if (operacion == 4):
                resultado = funcion_seno(angulo_grados)

        return print(f"El resultado de la operación es: {resultado}")

main()