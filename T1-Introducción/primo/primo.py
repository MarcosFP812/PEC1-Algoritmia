import sys                                                                      # importamos el módulo sys para usarlo 

def es_primo(n):
    """
    es_primo ::[int] -> [bool]
    Indica si un numero es primo o no
    siendo n el numero a identificar
    """

    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def es_primoR(num, n=2):
    if n >= num:
        print("Es primo")
        return True
    elif num % n != 0:
        return es_primo(num, n + 1)
    else:
        print("No es primo", n, "es divisor")
        return False
    
def main():
    """
        main :: [String] -> None
        programa principal argv debe contener al menos un elemento a procesar
        consultar https://docs.python.org/3/library/sys.html#sys.argv
    """
    print("Programa es primo") 
    try:  
        n = int(input("Escribe el numero: "))
        print("Analizamos: ", n)                             
        print(es_primo(n))
    except:
        print("Error")
    return None

if __name__ == "__main__":                                                      # Si este modulo es el principal 
    if '--test' in sys.argv:                                                    # Entonces si existe "--test" en la linea de argumentos
        import doctest                                                          # entonces importamos el módulo DoctTest
        doctest.testmod()                                                       # y lanzamos los test que hubiera definidos
    else:                                                                       # si no
        main(sys.argv)                                                          # llamamos a main y le pasamos argumentos




    

