from grafo import *
import sys

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

def main():
    
    g = Grafo(aristas1)
    g.dijkstra_voraz("A")
    g.mostrar_caminos()

if __name__ == "__main__":
    if '--test' in sys.argv:
        import doctest
        doctest.test()
    else:
        main()
