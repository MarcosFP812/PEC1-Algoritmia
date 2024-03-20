

def sumaR(n, resultado=0):
    """
    Función recursiva para calcular la suma de los números naturales hasta n.

    Parameters:
        n (int): El número hasta el cual se desea calcular la suma.
        resultado (int, opcional): El resultado parcial de la suma. Por defecto es 0.

    Returns:
        int: La suma de los números naturales hasta n.
    """
    if n <= 0:
        return resultado
    else:
        return sumaR(n-1, resultado+n)
    