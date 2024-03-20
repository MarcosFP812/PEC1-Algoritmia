class Arista():
    def __init__(self, o, d, v) -> None:
        """Crea una arista con un vértice de origen, un vértice de destino y un valor (peso).

        Args:
            o (str): Nombre del vértice de origen.
            d (str): Nombre del vértice de destino.
            v (float): Valor (peso) de la arista.
        """
        self.origen = o
        self.destino = d
        self.valor = v
        self.recorrida = False
    
    def __str__(self) -> str:
        """Devuelve una representación de cadena de la arista.

        Returns:
            str: Representación de cadena de la arista en el formato "Arista origen-destino:valor".
        """
        return f"Arista {self.origen}-{self.destino}:{self.valor}"

class Vertice():
    def __init__(self, n, d=float('inf')) -> None:
        """Crea un vértice con un nombre y una distancia inicialmente establecida en infinito.

        Args:
            n (str): Nombre del vértice.
            d (float, optional): Distancia del vértice. Por defecto es infinito.
        """
        self.nombre = n
        self.distancia = d
        self.recorrido = []

    def usado(self):
        """Verifica si el vértice ha sido utilizado.

        Returns:
            bool: True si el vértice ha sido utilizado (su distancia no es infinito), False de lo contrario.
        """
        return self.distancia != float("inf")

class Grafo():
    def __init__(self, aristas) -> None:
        """Crea un grafo con una lista de aristas.

        Args:
            aristas (list): Lista de objetos de tipo Arista.
        """
        self.aristas = aristas
        self.vertices = self.iniciar_vertices()

    def iniciar_vertices(self):
        """Inicializa la lista de vértices del grafo.

        Returns:
            list: Lista de objetos de tipo Vertice.
        """
        v = []
        def nombre_in_vertices(vertices, nombre):
            for v in vertices:
                if v.nombre == nombre:
                    return True
            return False
    
        for a in self.aristas:
            if not nombre_in_vertices(v, a.origen):
                v.append(Vertice(a.origen))
            if not nombre_in_vertices(v, a.destino):
                v.append(Vertice(a.destino))
        return v
    
    def mejor_arista(self):
        """Encuentra la mejor arista disponible en el grafo.

        Returns:
            Arista: La mejor arista disponible.
        """
        mejor = Arista("test", "test", float("inf"))
        for v in self.vertices:
            for a in self.aristas:
                if v.usado() and not a.recorrida and a.origen == v.nombre and a.valor < mejor.valor:
                    mejor = a
        
        mejor.recorrida = True
        return mejor
    
    def buscar_vertice(self, nombre):
        """Busca un vértice por su nombre.

        Args:
            nombre (str): Nombre del vértice a buscar.

        Returns:
            Vertice: El vértice encontrado, o None si no se encontró.
        """
        for v in self.vertices:
            if (nombre==v.nombre):
                return v

    def set_vertice(self, nombre, d, camino_origen=[]):
        """Actualiza la distancia y el recorrido de un vértice.

        Args:
            nombre (str): Nombre del vértice a actualizar.
            d (float): Nueva distancia del vértice.
            camino_origen (list, optional): Lista que representa el recorrido hasta el vértice. Por defecto es una lista vacía.
        """
        v = self.buscar_vertice(nombre)
        v.distancia = d
        v.recorrido = camino_origen
        v.recorrido += nombre


    def dijkstra_voraz(self, inicio):
        """Implementa el algoritmo de Dijkstra utilizando un enfoque voraz.

        Args:
            inicio (str): Nombre del vértice de inicio.
        """
        print(self.devolver_nombre_vertices())
        #Iniciar el primer vértice
        self.set_vertice(inicio, 0)              
        print(self.devolver_distancia_vertices())

        while(not self.aristas_recorridas()):
            #Funcion de seleccion
            a = self.mejor_arista()

            v_origen = self.buscar_vertice(a.origen)
            rec = v_origen.recorrido[:]
            v_destino = self.buscar_vertice(a.destino)

            nueva_distancia = v_origen.distancia + a.valor

            #Si la nueva distancia es mejor que la anterior se actualiza el vértice
            if nueva_distancia < v_destino.distancia:
                self.set_vertice(v_destino.nombre, nueva_distancia, rec)

            print(self.devolver_distancia_vertices())
            

    def aristas_recorridas(self):
        """Verifica si todas las aristas del grafo han sido recorridas.

        Returns:
            bool: True si todas las aristas han sido recorridas, False de lo contrario.
        """
        for a in self.aristas:
            if not a.recorrida:
                return False
        return True


    def devolver_distancia_vertices(self):
        """Devuelve una cadena con las distancias de los vértices.

        Returns:
            str: Cadena con las distancias de los vértices.
        """
        r = ""
        for v in self.vertices:
            r += str(v.distancia)+"\t"
        return r
    
    def devolver_nombre_vertices(self):
        """Devuelve una cadena con los nombres de los vértices.

        Returns:
            str: Cadena con los nombres de los vértices.
        """
        r = ""
        for v in self.vertices:
            r += v.nombre+"\t"
        return r
    
    def mostrar_caminos(self):
        """Muestra los caminos recorridos por cada vértice."""
        for v in self.vertices:
            print(f"{v.nombre}: {v.recorrido}")

