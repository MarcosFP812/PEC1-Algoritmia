# Tema 2. Algoritmos Voraces

## Conceptos clave

Los algoritmos voraces son utilizados para resolver problemas de optimización. Funcionan eligiendo en cada paso la mejor opción disponible sin considerar futuras consecuencias. Se basan en tres condiciones: una entrada de tamaño n, un subconjunto de candidatos que cumple ciertas restricciones (llamado solución factible), y una función objetivo que se busca maximizar o minimizar. 

El proceso se realiza por pasos, añadiendo en cada uno el mejor candidato disponible según algún criterio de optimización. Después de cada paso, se verifica si el conjunto seleccionado es completable; si lo es, se incorpora al conjunto de escogidos, y si no, se rechaza y no se considera en el futuro. El algoritmo termina cuando se obtiene una solución, siendo correcto si la solución es siempre óptima. 

Aunque son eficientes y fáciles de diseñar, no todos los problemas pueden resolverse con algoritmos voraces, ya que en ocasiones no encuentran la solución óptima o ninguna solución.

El esquema general del algoritmo voraz es:

```python
func voraz(Candidatos):
  Solucion = []
  mientras haya Candidatos y no Solucionado(Solucion)
    x=mejor(candidatos)
    si x entra en solucion
      Añadir x a solucion
    eliminar x de candidatos
  devolver solucion
```


## Ejercicios

### Cinta Magnética

Se tiene que almacenar un conjunto de n ficheros en una cinta magnética (soporte de almacenamiento de recorrido secuencial), teniendo cada fichero una longitud conocida l1, l2, …, ln. Para simplificar el problema, puede suponerse que la velocidad de lectura es constante, así como la densidad de información en la cinta.
Se conoce de antemano la tasa de utilización de cada fichero almacenado, es decir, se sabe la cantidad de peticiones pi correspondiente al fichero i que se van a realizar. Por
tanto, el total de peticiones al soporte será la cantidad $P = \sum\limits_{i=2}^{n} (pi)$ . Tras la petición de un fichero, al ser encontrado la cinta es automáticamente rebobinada hasta el comienzo de la misma.
El objetivo es decidir el orden en que los n ficheros deben ser almacenados para que se minimice el tiempo medio de carga, creando un algoritmo voraz correcto.

Se propone el siguiente código:
```python
def leer(d, mejor):
    datos = d[:]       #+1
    datos_leer = []    #+1
    peticiones = 0     #+1
    tiempo_total = 0   #+1

    while (peticiones != 0 or len(datos)!=0): #sumatorio(1+1
        peticiones = 0                        #+1

        if (len(datos)!=0):                   #+1 
            m = mejor(datos)                  #+3n+1 
            datos_leer.append(m)              #+1 
            datos.remove(m)                   #+1 

        for fichero in datos_leer:            #sumatorio(
            if(fichero.peticiones != 0):      #+1
                fichero.peticiones -= 1       #+1
            tiempo_total += fichero.longitud  #+1
            peticiones += fichero.peticiones  #+1))
            
    return tiempo_total  #+1
```

Recordemos las partes del algoritmo y expliquemos donde se encuentras y porqwue se han elegido

#### Candidatos

Los candidatos serán los que se introduzcan como parámetros de la función, en este caso se realiza una copia para eliminar la referenciación de python y se conservarán en la variable llamada `datos`, en esta las primeras n iteraciones del bucle se irá eliminmando el mejor elemento de la lista de candidatos hasta que deje de haber datos.

#### Solución

La solución se almacenará en la variable `datos_leer`, que guarda los datos que se leen en la cinta, hasta la iteración n del bucle se añadirá el mejor elemento de la lista de candidatos, después se leeran todos los ficheros hasta que el sumatorio de las peticiones de todos haya quedado reducido a 0, lo cual se controla con la variable `leidos`, importante que para salir del bucle se compruebe que ya no hay más ficheros en la lista de candidatos, lo que daría un error en la lógica del programa.

#### Lectura de ficheros

La lógica sobre la lectura de los ficheros se realiza en la última parte del bucle while, aquí se itera sobre los datos almacenados en la solución y se decrementa si es posible sus peticiones, además de sumar su longitud al tiempo total, suponemos que para computar cada unidad de longitud hace falta una unidad de tiempo.

#### Función de selección

Aquí está la complicación de este tipo de algoritmos, y es elegir cual será la manera en el que elegiremos el mejor elemento de los candidatos para que entre en la solución. Para ello deberemos de analizar los parámetros relevantes a la hora de la selección, los cuales son los atributos del Fichero, `longitud` y `peticiones`. 

Razonando podemos pensar que queremos primero debemos seleccionar los ficheros con menor longitud, puesto que si los primeros se leeran una gran cantidad de iteraciones conviene que su aportación al tiempo total sea la minima posible. De este razonamiento podemos suponer la siguiente funcion:
```python
def mejor_long(datos):
    primero = datos[0]
    for i in range(1, len(datos)):
        if (primero.longitud >= datos[i].longitud):
            primero = datos[i]
    return primero
```
Sin embargo esta solución es incompleta, puesto que es posible que aunque tenga un tamaño pequeño puede que sus peticiones sean también pocas por lo que se estará iterando con 0 peticiones una gran cantidad de veces, lo que significa que se está perdiendp tiempo en un fichero ya leido. Recordemos que el objetivo es no malgastar lecturas en primera instancia. Así pues obtenemos la siguiente función:
```python
def mejor_pet(datos):
    primero = datos[0]
    for i in range(1, len(datos)):
        if (primero.peticiones >= datos[i].peticiones):
            primero = datos[i]
    return primero
```
Pero con esta aproximación no tenemos en cuenta la longitud por lo que a igualdad de numero de peticiones no hay ninguna forma de discriminar el que tenga menor longitud, puesto que sería lo más eficiente. Así pues debemos de buscar una relación entre ambos valores, la cual puede ser un producto o un cociente.
Respecto al producto no será la opción más óptima por motivos parecidos al de la longitud, por lo que el mayor cociente entre peticiones y longitud será la mejor opción, ya que si tienen una longitud grande, el cociente será menor, por lo que según el criterio se encolarán al final. En caso de ser muy demandante de peticiones su cociente será mayor y por lo tanto mejor colocarlo de los primeros. De esta forma sería el código:
```python 
def mejor_div(datos):
    primero = datos[0]   
    for i in range(1, len(datos)):
        if (primero.div() <= datos[i].div()):
            primero = datos[i]
    return primero
```
#### Coste 

En cuanto al coste, observamos que la función mejor tendrá un coste en tiempo de ejecución de:

$T(n) = \sum\limits_{i=0}^{n} (1+1+1) + 1 = \sum\limits_{i=0}^{n} (3) + 1 = 3n + 1$

Por lo que el coste será: $O(n)$

Centrandonos en la función principal:

$T(n) = 5 + \sum\limits_{i=0}^{n} (7 + 3n + \sum\limits_{i=0}^{n}(4)) = 5 + \sum\limits_{i=0}^{n} (7 + 3n + 4n) = 5 + n(7 + 7n) = 7n^2 + 7n +5$

Por lo que la complejidad será $O(n^2)$

### Algoritmo de Dijkstra

Se tiene un grafo dirigido G = < N, A >, siendo N = {1, …, n} el conjunto de nodos y A ⊆ NxN el conjunto de aristas. Cada arista (i, j) ∈ A tiene un coste asociado cij (cij > 0 ∀i, j ∈ N; si (i, j) ∉ A puede considerarse cij = +∞). Sea M la matriz de costes del grafo G, es decir, M [i, j] = cij.
Teniendo como datos la cantidad de nodos n y la matriz de costes M, se pide encontrar tanto el camino mínimo entre los nodos 1 y n como la longitud de dicho camino usando el algoritmo de Dijkstra, utilizando las siguientes ideas:
- Crear un estructura de datos que almacene las distancias temporales conocidas (inicializadas al coste de la arista del vértice 1 a cada vértice j, o +∞ si no existe
dicha arista) para los vértices no recorridos (inicialmente, todos salvo el 1).
- Seleccionar como candidato el que tenga menor distancia temporal conocida, eliminarle del conjunto de vértices no recorridos, y actualizar el resto de distancias temporales si pueden ser mejoradas utilizando el vértice actual.
- Se necesitará almacenar de alguna manera la forma de recorrer el grafo desde el vértice 1 al vértice n (no necesariamente igual al conjunto de decisiones tomadas).

#### Estructura

Para este apartado para mejorar la estructiración de la práctica se ha utilizado un paradigma estructural orientado a objetos, con 3 clases principales `Vertices`, `Aristas` y `Grafo`, aquí se aporta el código de cada una de ellas:

```python
class Arista():
    def __init__(self, o, d, v) -> None:
        self.origen = o
        self.destino = d
        self.valor = v
        self.recorrida = False
    
    def __str__(self) -> str:
        return f"Arista {self.origen}-{self.destino}:{self.valor}"

class Vertice():
    def __init__(self, n, d=float('inf')) -> None:
        self.nombre = n
        self.distancia = d
        self.recorrido = []

    def usado(self):
        return self.distancia != float("inf")

class Grafo():
    def __init__(self, aristas) -> None:
        self.aristas = aristas
        self.vertices = self.iniciar_vertices()

    def iniciar_vertices(self):
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
        mejor = Arista("test", "test", float("inf"))
        for v in self.vertices:
            for a in self.aristas:
                if v.usado() and not a.recorrida and a.origen == v.nombre and a.valor < mejor.valor:
                    mejor = a 
        mejor.recorrida = True
        return mejor
    
    def buscar_vertice(self, nombre):
        for v in self.vertices:
            if (nombre==v.nombre):
                return v

    def aristas_recorridas(self):
        for a in self.aristas:
            if not a.recorrida:
                return False
        return True

    def set_vertice(self, nombre, d, camino_origen=[]):
        v = self.buscar_vertice(nombre)
        v.distancia = d
        v.recorrido = camino_origen
        v.recorrido += nombre

    def dijkstra_voraz(self, inicio):
        #Iniciar el primer vértice
        self.set_vertice(inicio, 0)              

        while(not self.aristas_recorridas()):
            #Funcion de seleccion
            a = self.mejor_arista()

            v_origen = self.buscar_vertice(a.origen)
            rec = v_origen.recorrido[:]
            v_destino = self.buscar_vertice(a.destino)

            nueva_distancia = v_origen.distancia + a.valor

            if nueva_distancia < v_destino.distancia:
                self.set_vertice(v_destino.nombre, nueva_distancia, rec)
            
```

Los vertices serán las estructuras que guardarán la distancia y el recorrido necesario para llegar desde el primer vértice, en cuanto a las aristas tendran 2 vertices (origen y destino), se sabrá si están o no recorridas por uno de sus atributos y también tendrá un valor que indica la distancia entre vertices. Finalmente tenemos la clase principal que se llama Grafo, este tiene un conjunto de vértices que deberán ser inicializados en base a las aristas que se le aporten.

En cuanto al funcionamiento del algoritmo expliquemos algunas de las funciones accesorio a `dijkstra_voraz`:

- **`iniciar_vertices(self)`** Es una función que se aplica en el constructor de la clase, su función esencialmente es transformar el grafo de aristas dado en los vértices necesarios, inicializados todos con unha distancia de &infin;, su complejidad es de $O(n^2)$, ya que consta de un doble bucle for.
- **`buscar_vertice(self, nombre)`**: Devuelve el vértice que tenga el nombre solicitado mediante una búsqueda secuencial. La complejidad es de $O(n)$.
- **`aristas_recorridas(self)`**: Devuelve True si todas las aristas del grafo han sido recorridas, False en caso contrario. La complejidad es de $O(n)$.
- **`mejor_arista(self)`**: Es la función de selección devulve la arista con menor tamaño que haya en la lista de aristas, las condiciones para que esto ocurra son que el vértice que se está evaluando esté usado (significa que su distancia no sea &infin;, es decir que haya alguna forma de llegar a el) y que la arista no haya sido recorrida. Se la arista cuyo valor sea el menor y se devuelve colocandola como recorrida. El coste es $O(n^2)$ por tener un doble bucle for, sin embargo uno iterara sobre los vértices y otro sobre las aristas, por lo que esta complejidad variará en caso de ser un grafo denso o disperso.
- **`set_vertice(self, nombre, d, camino_origen=[])`**: Cambia los valores de un vértice indicado, tanto la distancia para llegar a él, como el recorrido necesario. Tiene la misma complejidad que `buscar_vertice(self, nombre)`

Una vez vistas estas funciones podemos entrar en la **`dijkstra_voraz(self, inicio)`**, aquí contamos con el grupo de aristas candidatas y un valor de inicio el cual se colocará dicho vértice con distancia 0 y un camino nulo, posteriormente comenzará un el bucle voraz el cual no terminará hasta que se recorran todas las aristas (Destacar que todas las aristas deben de estar interconectadas sino será un bucle infinito). Se elegirá la mejor arista, recordemos que cada arista tiene un origen y un destino, por lo que se tomará el vertice origen para calcular la nueva distancia y recorrido del vértice destino, posteriormente se comprobará si esa distancia es menor que la existente y si es así se colocará en la lista de vértices.
La complejidad total del algoritmo será $O(n^3)$, puesto que la función de selección es $O(n^2)$ la cual está dentro de un bucle while.


### Escaleras

Shrek, Asno y Dragona llegan a los pies del altísimo castillo de Lord Farquaad para liberar a Fiona de su encierro. Como sospechaban que el puente levadizo estaría vigilado por numerosos soldados se han traído muchas escaleras, de distintas alturas, con la esperanza
de que alguna de ellas les permita superar la muralla; pero ninguna escalera les sirve porque la muralla es muy alta. Shrek se da cuenta de que, si pudiese combinar todas las escaleras en una sola, conseguiría llegar exactamente a la parte de arriba y poder entrar al
castillo.

Afortunadamente las escaleras son de hierro, así que con la ayuda de Dragona van a “soldarlas”. Dragona puede soldar dos escaleras cualesquiera con su aliento de fuego, pero tarda en calentar los extremos tantos minutos como metros suman las escaleras a soldar. Por ejemplo, en soldar dos escaleras de 6 y 8 metros tardaría 6 + 8 = 14 minutos. Si a esta escalera se le soldase después una de 7 metros, el nuevo tiempo sería 14 + 7 = 21 minutos, por lo que habrían tardado en hacer la escalera completa un total de 14 + 21 = 35 minutos.
Diseñar un algoritmo eficiente que encuentre el mejor coste y manera de soldar las escaleras para que Shrek tarde lo menos posible es escalar la muralla, indicando las estructuras de datos elegidas y su forma de uso. Se puede suponer que se dispone exactamente de las escaleras necesarias para subir a la muralla (ni sobran ni faltan), es decir, que el dato del problema es la colección de medidas de las “miniescaleras” (en la estructura de datos que se elija), y que solo se busca la forma óptima de fundir las escaleras.

En este caso el algoritmo voraz consiste en seleccionar la mejor escalera primero hasta que no queden más, importante recalcar que el conjunto de candidatos es exactamente la altura que queremos obtener, en caso de lo contrario está solución discreparia según diferentes casos. 

Para la función de selección hay dos posibilidades, elegir la más alta o la más baja de los candidatos. No es complicado razonar que si las que primero se escojan serán las que más se repitan, conviene seleccionar la más baja primero ya que aportará menos al tiempo total (lo cual queremos minimizar).

De manera similar al ejercicio de los ficheros se hace posteriormente el calculo del tiempo total.

Por lo que la función de selección es la siguiente:

```python
def mejor_escalera(lista):
    menor = lista[0]
    for elem in lista[1:]:
        if elem > menor:
            menor = elem
    return menor
```

Y la función principal queda de esta manera:

```python
def seleccionar_escaleras(c, altura, mejor_escalera):
    solucion = []
    candidatos = c[:]
    altura_actual = 0
    tiempo_total = 0

    while (altura > altura_actual and len(candidatos)):
        mejor = mejor_escalera(candidatos)

        solucion.append(mejor)
        candidatos.remove(mejor)

        altura_actual += mejor

        for elem in solucion:
            tiempo_total += elem
    return tiempo_total
```

En cuanto a la complejidad, para calcular el mejor será $0(n)$ por ser un bucle for, el cual está dentro del bucle voraz así que la complejidad será de $0(n^2)$. Se podría mejorar haciendo uso de un algoritmo de ordenación quicksort.








