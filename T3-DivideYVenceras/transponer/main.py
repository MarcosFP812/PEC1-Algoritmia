from matriz import *
import sys

matriz_4x4 = [
    [1, 0, 0, 1],
    [0, 1, 0, 1],
    [1, 0, 1, 1],
    [0, 0, 1, 1]
]

def main():
    print("Matriz: ")
    mostrar_matriz(matriz_4x4)
    fin = transponer_matriz(matriz_4x4)
    print("Matriz transpuesta: ")
    mostrar_matriz(fin)

if __name__ == "__main__":
    if '--test' in sys.argv:
        import doctest
        doctest.test()
    else:
        main()