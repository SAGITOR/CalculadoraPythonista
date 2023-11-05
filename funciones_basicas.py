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

def división(dividendo, divisor):
    """
    Esta función realiza una división de dos números.

    Args:
    dividendo (int): El número que será dividido.
    divisor (int): El número por el cual se divide.

    Returns:
    int: El cociente de dividir dividendo por divisor.
    """
    return dividendo / divisor

def cociente(dividendo, divisor):
    """
    Esta función calcula el cociente entero de una división.

    Args:
    dividendo (int): El número que será dividido.
    divisor (int): El número por el cual se divide.

    Returns:
    int: El cociente entero de dividendo entre divisor.
    """
    return dividendo // divisor

def resto(dividendo, divisor):
    """
    Esta función calcula el resto de una división entera.

    Args:
    dividendo (int): El número que será dividido.
    divisor (int): El número por el cual se divide.

    Returns:
    int: El resto de dividendo entre divisor.
    """
    return dividendo % divisor

def raíces(radicando, indice):
    """
    Esta función calcula la raíz de un número.

    Args:
    radicando (int): El número del cual se calculará la raíz.
    indice (int): El índice de la raíz (por ejemplo, 2 para la raíz cuadrada).

    Returns:
    float: El resultado de la raíz.
    """
    return radicando ** (1/indice)

def main():
    resultado = 0
    print("Ingrese el número de la opcion de la operacion basica que desea realizar: ")
    operacion = int(input("1 = suma, 2 = resta, 3 = multiplicación, 4 = división, 5 = cociente, 6 = resto, 7 = raiz: "))

    
    if (operacion < 1 or operacion > 6):
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
            dividendo = int(input("dividendo: "))
            divisor = int(input("divisor: "))
            if ( divisor == 0 ):
                return print("Error en la division: No se puede dividir por cero")
                
            resultado = división(divisor, divisor)
        elif (operacion == 5):
            dividendo = int(input("dividendo: "))
            divisor = int(input("divisor: "))
            if ( divisor == 0 ):
                return print("Error en la division: No se puede dividir por cero")
                
            resultado = cociente(dividendo, divisor)
        elif (operacion == 6):
            dividendo = int(input("dividendo: "))
            divisor = int(input("divisor: "))
            if ( divisor == 0 ):
                return print("Error en la division: No se puede dividir por cero")
                
            resultado = resto(dividendo, divisor)
        elif (operacion == 7): 
            radicando = int(input("radicando: "))
            indice = int(input("indice: "))
            if ( indice == 0 ):
                return print("Error en el calculo de la raiz: El indice no puede ser 0")
            
            resultado = raíces(radicando, indice)

        print(f"El resultado de la operacion es: {resultado}")

main()