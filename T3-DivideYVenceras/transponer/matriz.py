def transponer_matriz(matriz: list[list[int]]) -> list[list[int]]:
    """
    Función que transpone una matriz cuadrada dividida en cuatro cuadrantes.

    Parameters:
        matriz (list[list[int]]): La matriz cuadrada a transponer.

    Returns:
        list[list[int]]: La matriz transpuesta.
    """
    # Condición de parada
    if len(matriz) == 1:
        return matriz
    else:
        # Dividir la matriz en cuatro cuadrantes
        submat = dividir_cuadrantes(matriz)

        # Transponer cada cuadrante recursivamente
        for i in range(4):
            submat[i] = transponer_matriz(submat[i])

        # Unir las submatrices transpuestas
        return unir_cuadrantes([submat[0], submat[2], submat[1], submat[3]])

        
def unir_cuadrantes(submatrices: list[list[list[int]]]) -> list[list[int]]:
    """
    Función que une cuatro submatrices en una matriz más grande.

    Parameters:
        submatrices (list[list[list[int]]]): Lista de las cuatro submatrices.

    Returns:
        list[list[int]]: La matriz resultante.
    """
    longitud = int(len(submatrices[0]) * 2)
    punto_medio = int(longitud / 2)
    matriz = iniciar_matrizN(longitud)

    for i in range(0, longitud):
        for j in range(0, longitud):
            if i < punto_medio and j < punto_medio:
                matriz[i][j] = submatrices[0][i][j] 
            elif i < punto_medio and j >= punto_medio:
                matriz[i][j] = submatrices[1][i][j - punto_medio] 
            elif i >= punto_medio and j < punto_medio:
                matriz[i][j] = submatrices[2][i - punto_medio][j]
            elif i >= punto_medio and j >= punto_medio:
                matriz[i][j] = submatrices[3][i - punto_medio][j - punto_medio]

    return matriz

def dividir_cuadrantes(matriz: list[list[int]]) -> list:
    """
    Función que divide una matriz en cuatro cuadrantes.

    Parameters:
        matriz (list[list[int]]): La matriz a dividir.

    Returns:
        list: Lista de las cuatro submatrices.
    """
    punto_medio = len(matriz) // 2
    division = [iniciar_matrizN(punto_medio) for _ in range(4)]

    for i in range(punto_medio):
        for j in range(punto_medio):
            division[0][i][j] = matriz[i][j]
            division[1][i][j] = matriz[i][j + punto_medio]
            division[2][i][j] = matriz[i + punto_medio][j]
            division[3][i][j] = matriz[i + punto_medio][j + punto_medio]

    return division

def iniciar_matrizN(n: int) -> list[list[int]]:
    """
    Función que inicializa una matriz de tamaño N x N con ceros.

    Parameters:
        n (int): Tamaño de la matriz.

    Returns:
        list[list[int]]: La matriz inicializada.
    """
    matriz = []
    for _ in range(n):
        matriz.append([0] * n)
    return matriz

def mostrar_matriz(matriz: list[list[int]]) -> None:
    """
    Función que muestra una matriz en la consola.

    Parameters:
        matriz (list[list[int]]): La matriz a mostrar.

    Returns:
        None
    """
    for fila in matriz:
        print("|", end=" ")
        for elemento in fila:
            print(elemento, end=" ")
        print("|")
