

def sumaR(n, resultado = 0):
    if n == 0:
        return resultado
    elif n<0:
        return 0
    else:
        return sumaR(n-1, resultado+n)
    