def transponer_matriz(matriz: list[list[int]]) -> list[list[int]]:
    #condicion de parada
    if len(matriz) == 1:
        return matriz
    else:
        
        submat = dividir_cuadrantes(matriz)

        for i in range(4):
            print("Longitud = ", len(submat[1]))
            mostrar_matriz(submat[i])
            submat[i] = transponer_matriz(submat[i])

        # Unir las submatrices transpuestas
        return unir_cuadrantes([submat[0], submat[2], submat[1], submat[3]])

        
def unir_cuadrantes(submatrices):

    longitud = int(len(submatrices[0])*2)

    punto_medio = int(longitud/2)

    matriz = iniciar_matrizN(longitud)

    for i in range(0, longitud):
        for j in range(0, longitud):
            if i<punto_medio and j<punto_medio:
                matriz[i][j] = submatrices[0][i][j] 
            elif i<punto_medio and j>=punto_medio:
                matriz[i][j] = submatrices[1][i][j-punto_medio] 
            elif i>=punto_medio and j<punto_medio:
                matriz[i][j] = submatrices[2][i-punto_medio][j]
            elif i>=punto_medio and j>=punto_medio:
                matriz[i][j] = submatrices[3][i-punto_medio][j-punto_medio]

    return matriz

def dividir_cuadrantes(matriz: list[list[int]]) -> list:

    punto_medio = int(len(matriz)/2)

    division = [iniciar_matrizN(punto_medio), iniciar_matrizN(punto_medio), iniciar_matrizN(punto_medio), iniciar_matrizN(punto_medio)]

    for i in range(0, len(matriz)):
        for j in range(0, len(matriz)):
            if i<punto_medio and j<punto_medio:
                division[0][i][j] = matriz[i][j]
            elif i<punto_medio and j>=punto_medio:
                division[1][i][j-punto_medio] = matriz[i][j]
            elif i>=punto_medio and j<punto_medio:
                division[2][i-punto_medio][j] = matriz[i][j]
            elif i>=punto_medio and j>=punto_medio:
                division[3][i-punto_medio][j-punto_medio] = matriz[i][j]

    return division 

def iniciar_matrizN(n:int) ->  list[list[int]]:
    matriz = []
    for i in range(0, n):
        matriz.append([])
        for j in range(0, n):  
            matriz[i].append(0)
    return matriz

def mostrar_matriz(matriz: list[list[int]]) -> None:
    for i in range(0, len(matriz)):
        print("|", end=" ")
        for j in range(0, len(matriz)):
            #print(i,j)
            print(matriz[i][j], end=" ")
        print("|")


matriz_16x16 = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
    [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32],
    [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48],
    [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64],
    [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
    [81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96],
    [97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
    [113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128],
    [129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144],
    [145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160],
    [161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176],
    [177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192],
    [193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208],
    [209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224],
    [225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240],
    [241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256]
]
matriz_8x8 = [
    [1, 3, 3, 8, 5, 6, 7, 8],
    [2, 4, 3, 4, 5, 6, 7, 8],
    [5, 2, 7, 4, 5, 6, 7, 8],
    [2, 2, 3, 1, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 4, 6, 8],
    [1, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 3, 8]
]
matriz_4x4 = [
    [1, 3, 3, 8],
    [2, 4, 3, 4],
    [5, 2, 7, 4],
    [2, 2, 3, 1]

]
matriz_2x2 = [
    [1,2],
    [1,2]
]

fin = transponer_matriz(matriz_16x16)

mostrar_matriz(fin)