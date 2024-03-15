

def sumaR(n, resultado = 0):
    if n =< 0:
        return resultado
    else:
        return sumaR(n-1, resultado+n)
    
