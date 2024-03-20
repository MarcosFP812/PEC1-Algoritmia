from grafo import *

aristas1 = [
    Arista("A", "B", 1),
    Arista("A", "C", 3),
    Arista("A", "D", 5),
    Arista("A", "E", 7),
    Arista("A", "F", 2),
    Arista("H", "G", 4),
    Arista("C", "H", 6),
    Arista("D", "I", 1),
    Arista("B", "H", 7),
    Arista("B", "F", 3),
    Arista("B", "G", 2),
    Arista("C", "D", 3),
    Arista("D", "J", 7),
    Arista("E", "J", 2),
    Arista("F", "I", 4),
    Arista("G", "J", 6),
    Arista("H", "J", 1),
    Arista("I", "E", 3),
    Arista("I", "J", 3)
]

aristas2 = [
        Arista("A", "B", 5),
        Arista("B", "C", 2),
        Arista("A", "C", 1),
        Arista("C", "D", 4),
        Arista("D", "A", 2),
        Arista("C", "E", 7),
        Arista("D", "E", 1),
        Arista("B", "E", 3)
    ]
    
def test():
    print("Test 1:")

    g = Grafo(aristas2)
    g.dijkstra_voraz("A")
    g.mostrar_caminos()

    print("==================================================================")

    print("Test 2: ")

    g = Grafo(aristas1)
    g.dijkstra_voraz("A")
    g.mostrar_caminos()

    print("==================================================================")
    print("Recuerda que la representación gráfica de los grafos son las imágenes Test1 y Test2 ")