from matriz import *


matriz_16x16 = [
    [1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1],
    [0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
    [0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0],
    [1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0],
    [1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0]
]

matriz_8x8 = [
    [1, 0, 0, 1, 0, 1, 1, 1],
    [0, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1],
    [0, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 1, 0]
]
matriz_4x4 = [
    [1, 0, 0, 1],
    [0, 1, 0, 1],
    [1, 0, 1, 1],
    [0, 0, 1, 1]
]

matriz_16x16_traspuesta = [
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0]
]

matriz_8x8_traspuesta = [
    [1, 0, 1, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0]
]

matriz_4x4_traspuesta = [
    [1, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 1],
    [1, 1, 1, 1]
]

def iguales(m1, m2):
    """
    Compara dos matrices y devuelve True si son iguales y False si son diferentes.

    Parameters:
        m1 (list): La primera matriz.
        m2 (list): La segunda matriz.

    Returns:
        bool: True si las matrices son iguales, False en caso contrario.
    """
    # Verificar si las matrices tienen las mismas dimensiones
    if len(m1) != len(m2) or len(m1[0]) != len(m2[0]):
        return False

    # Verificar cada elemento de las matrices
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            if m1[i][j] != m2[i][j]:
                return False

    return True

def test():

    fin = transponer_matriz(matriz_4x4)
    mostrar_matriz(fin)
    print(" Se ha traspuesto correctamente: ", iguales(fin, matriz_4x4_traspuesta))
    print("==================================================================")
    fin = transponer_matriz(matriz_8x8)
    mostrar_matriz(fin)
    print(" Se ha traspuesto correctamente: ", iguales(fin, matriz_8x8_traspuesta))
    print("==================================================================")
    fin = transponer_matriz(matriz_16x16)
    mostrar_matriz(fin)
    print(" Se ha traspuesto correctamente: ", iguales(fin, matriz_16x16_traspuesta))
    print("==================================================================")

