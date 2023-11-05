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

def resta(minuendo, sustraendo):
    """
    Esta función realiza una resta de dos números.

    Args:
    minuendo (float): El número del que se restará.
    sustraendo (float): El número que se restará.

    Returns:
    float: La resta de minuendo menos sustraendo.
    """
    return minuendo - sustraendo

def multiplicación(multiplicando, multiplicador):
    """
    Esta función realiza una multiplicación de dos números.

    Args:
    multiplicando (int): El primer número a multiplicar.
    multiplicador (int): El segundo número a multiplicar.

    Returns:
    int: El resultado de la multiplicación de multiplicando y multiplicador.
    """
    return multiplicando * multiplicador

def división(a, b):
    return a / b

def main():
    resultado = 0
    print("Ingrese el número de la opcion de la operacion basica que desea realizar: ")
    operacion = int(input("1 = suma, 2 = resta, 3 = multiplicación, 4 = división: "))

    
    if (operacion < 1 or operacion > 4):
        return print("Opción no válida")
    else:
        if (operacion == 1): 
            sumando_1 = float(input("sumando 1: "))
            sumando_2 = float(input("sumando 2: "))
            resultado = suma(sumando_1, sumando_2)
        elif (operacion == 2):
            minuendo = float(input("minuendo: "))
            sustraendo = float(input("sustraendo: "))
            resultado = resta(minuendo, sustraendo)
        elif (operacion == 3):
            multiplicando = int(input("multiplicando: "))
            multiplicador = int(input("multiplicador: "))
            resultado = multiplicación(multiplicando, multiplicador)
        elif (operacion == 4):
            a = int(input("a: "))
            b = int(input("b: "))
            if ( b == 0 ):
                print("Error en la division: No se puede dividir por cero")
                
            resultado = división(a, b)

        print(f"El resultado de la operacion es: {resultado}")

main()