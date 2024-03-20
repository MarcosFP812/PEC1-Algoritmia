import fichero as f
import mejor as m
import sys

def main():
    funciones = [m.mejor_prod, m.mejor_long, m.mejor_pet, m.mejor_div]
    print("Prueba 1")
    for funcion in funciones:
        #print(funcion.__name__)
        ficheros = [f.Fichero(10,3), f.Fichero(3,7), f.Fichero(4,3), f.Fichero(5,2), f.Fichero(2,4)]
        m.leer(ficheros, funcion)
    
    print("Prueba 2")
    for funcion in funciones:
        #print(funcion.__name__)
        ficheros = [f.Fichero(5, 5), f.Fichero(2, 8), f.Fichero(6, 2), f.Fichero(4, 3), f.Fichero(3, 6)]
        m.leer(ficheros, funcion)

    print("Prueba 3")
    for funcion in funciones:
        #print(funcion.__name__)
        ficheros = [f.Fichero(8, 5), f.Fichero(1, 9), f.Fichero(5, 5), f.Fichero(3, 5), f.Fichero(3, 2)]
        m.leer(ficheros, funcion)

    print("Prueba 4")
    for funcion in funciones:
        #print(funcion.__name__)
        ficheros = [f.Fichero(1, 1), f.Fichero(2, 2), f.Fichero(10, 10), f.Fichero(11, 4), f.Fichero(3, 5)]
        m.leer(ficheros, funcion)

if __name__ == "__main__":                                                      # Si este modulo es el principal 
    if "--test" in sys.argv:
        import doctest
        doctest.test()
    elif "--random" in sys.argv:
        import doctest
        doctest.testrandom()
    else:
        main()     