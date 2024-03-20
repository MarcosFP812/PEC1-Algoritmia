import fichero as f
import mejor as m
import random
import copy as c

funciones = [m.mejor_prod, m.mejor_long, m.mejor_pet, m.mejor_div]

def generar_numeros_aleatorios():
    r = []
    for _ in range(5):
        r.append(f.Fichero(random.randint(1, 10), random.randint(1, 10)))
    
    return r

def test():
    l = []

    print("Test:")
    print("Se realizaran pruebas con cada uno de los algorítmos de selección para comparar cual es el mejor")
    print("==================================================================")

    print("Prueba 1")
    for funcion in funciones:
        print("Usando la funcion: ", funcion.__name__)
        ficheros = [f.Fichero(10,3), f.Fichero(3,7), f.Fichero(4,3), f.Fichero(5,2), f.Fichero(2,4)]
        t = m.leer(ficheros, funcion)
        l.append(t)
        print(t)
        print("------------------------------------")
    print("La mejor funcion de seleccion ha sido: ", funciones[l.index(min(l))].__name__)
    l = []
    print("==================================================================")

    print("Prueba 2")
    for funcion in funciones:
        print("Usando la funcion: ", funcion.__name__)
        ficheros = [f.Fichero(5, 5), f.Fichero(2, 8), f.Fichero(6, 2), f.Fichero(4, 3), f.Fichero(3, 6)]
        t = m.leer(ficheros, funcion)
        l.append(t)
        print(t)
        print("------------------------------------")
    print("La mejor funcion de seleccion ha sido: ", funciones[l.index(min(l))].__name__)
    l = []
    print("==================================================================")

    print("Prueba 3")
    for funcion in funciones:
        print("Usando la funcion: ", funcion.__name__)
        ficheros =  [f.Fichero(8, 5), f.Fichero(1, 9), f.Fichero(2, 5), f.Fichero(3, 5), f.Fichero(3, 2)]
        t = m.leer(ficheros, funcion)
        l.append(t)
        print(t)
        print("------------------------------------")
    print("La mejor funcion de seleccion ha sido: ", funciones[l.index(min(l))].__name__)
    l = []
    print("==================================================================")

    print("Prueba 4")
    for funcion in funciones:
        print("Usando la funcion: ", funcion.__name__)
        ficheros = [f.Fichero(1, 1), f.Fichero(2, 2), f.Fichero(10, 10), f.Fichero(11, 4), f.Fichero(3, 5)]
        t = m.leer(ficheros, funcion)
        l.append(t)
        print(t)
        print("------------------------------------")
    print("La mejor funcion de seleccion ha sido: ", funciones[l.index(min(l))].__name__)
    l = []
    print("==================================================================")

    print("*Nota: es posible que varias funciones de seleccion den el mismo resultado y como mejor solo se muetre una")
    print("Usa --random para hacer pruebas aleatorias")


def testrandom():
    funciones = [m.mejor_prod, m.mejor_long, m.mejor_pet, m.mejor_div]
    fun = ""
    pruebas = [(generar_numeros_aleatorios(), f"Prueba {i+1}") for i in range(50)]
    
    print("\t\t", end="")
    for funcion in funciones:
        fun += f"{funcion.__name__}\t"
    print(fun, end="mejor\n")
    for prueba in pruebas:
        print(prueba[1], end="\t")

        resultados = []
        for funcion in funciones:
            r = m.leer(c.deepcopy(prueba[0]), funcion, False)
            resultados.append(r)
            print(r, end="\t\t")
        print(f"{funciones[resultados.index(min(resultados))].__name__}")
        