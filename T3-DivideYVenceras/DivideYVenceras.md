# Tema 3. Algoritmos Divide Y Vencerás

## Conceptos clave

El enfoque de divide y vencerás descompone el problema en subproblemas más pequeños, los resuelve de manera independiente y luego combina las soluciones parciales para obtener la solución del problema original. El enfoque implica tres pasos fundamentales:

- Dividir: El problema original se divide en subproblemas más pequeños y manejables. Estos subproblemas pueden ser del mismo tipo que el problema original pero de tamaño reducido.
- Conquistar: Cada subproblema se resuelve de manera independiente. Esto puede implicar resolverlos directamente si son lo suficientemente simples o reducirlos a casos aún más simples, típicamente de forma recursiva.
- Combinar: Las soluciones parciales de los subproblemas se combinan para construir la solución del problema original. Esto puede implicar fusionar las soluciones, agregarlas, compararlas, etc.

En resumen, la eficiencia de este enfoque depende de cómo se resuelvan los subproblemas y cómo se combinen sus soluciones.

El esquema de este tipo de algoritmos es:

```
función DivideYVenceras(c: tipocaso) : tiposolucion;
var
  x1,..., xk : tipocaso;
  y1,...,yk: tiposolucion;
inicio
  si c es suficientemente simple entonces
    devolver solucion_simple(c)
  sino
    descomponer c en x1, ..., xk
    para i ← 1 hasta k hacer
      yi ← DivideYVenceras(xi)
    fin para
    devolver combinar_solucion_subcasos(y1, ..., yk)
  fsi
fin función
```


## Ejercicios

### Hallar x en un intervalo

Se tiene acceso a una función f(x) de la que se sabe que en el intervalo real [p1, p2] tiene un único mínimo local en el punto x0, que es estrictamente decreciente entre [p1, x0] y que es estrictamente creciente entre [x0, p2]. Hay que observar que x0 puede coincidir con p1 o con p2.
Se tiene que buscar, de la manera más eficiente posible, todos los puntos x (si es que existen) del intervalo [p1, p2] tales que la función f tome un cierto valor k, es decir, se busca el conjunto de valores {x ∈ [p1, p2] tal que f(x) = k}. Para simplificar el proceso, en vez del valor exacto de cada x puede indicarse un intervalo de valores [α, β], con β – α < ε, donde se encuentre x. Los datos del algoritmo serán el intervalo [p1, p2], el valor k que se está buscando, y el valor ε para la aproximación.

La solución propuesta es la siguiente:

```python
class Polinomio:
    """
    Polinomio de n grado
    """
    def __init__(self, coeficientes):
        self.coeficientes = coeficientes

    def evaluar(self, x):
        resultado = 0
        for i, coeficiente in enumerate(self.coeficientes):
            resultado += coeficiente * (x ** i)
        return resultado
    
    def encontrar_minimo_en_intervalo(self, intervalo, paso=0.01):
        min_x = intervalo[0]
        min_y = self.evaluar(min_x)
        
        x = intervalo[0]
        while x < intervalo[1]:
            y = self.evaluar(x)
            if y < min_y:
                min_x = x
                min_y = y
            x += paso
        
        return min_x

    def dyv(self, intervalo, k, e, minim=True):
        solucion = []
        # Caso base: intervalo suficientemente pequeño.
        if distancia(intervalo) < e:
            return []
        else:
            v0 = self.evaluar(intervalo[0])  # Valor de f(x) en el extremo izquierdo del intervalo.
            v1 = self.evaluar(intervalo[1])  # Valor de f(x) en el extremo derecho del intervalo.
            
            if minim:
                # En la primera iteracion se busca el mínimo, encontrar el mínimo local.
                min = self.encontrar_minimo_en_intervalo(intervalo)   
                print(f"Hay mínimo {min}")
                x0 = min    
            else:
                # De lo contrario, se toma el punto medio del intervalo.
                x0 = ((intervalo[0] + intervalo[1]) / 2)

            if -e <= self.evaluar(x0) - k <= e:
                # Si f(x0) es aproximadamente igual a k dentro del margen de error, se añade a la solución.
                solucion.append(x0)

            if v0 < k < self.evaluar(x0) or v0 > k > self.evaluar(x0):
                # Si k está entre f(p0) y f(x0), se busca en la mitad izquierda del intervalo.
                solucion += self.dyv([intervalo[0], x0], k, e, False)
            
            if self.evaluar(x0) < k < v1 or self.evaluar(x0) > k > v1:
                # Si k está entre f(x0) y f(p1), se busca en la mitad derecha del intervalo.
                solucion += self.dyv([x0, intervalo[1]], k, e, False)

        return list(set(solucion))
```

#### Estructura

He optado por la orientación a objetos para mayor simplicidad de la respuesta, la clase se llama `Polinomio`, tiene como atributo una lista con los coeficientes del polinomio. Para hallar f(x) tenemos em método `evaluar` con una complejidad $O(n)$, para hallar el mínimo de un intervalo tenemos la función `encontrar_minimo_en_intervalo`, que se ha simplificado haciendo un bucle desde el inicio hasta el fin del intervalo evaluando cada punto con un paso.

Ahora analizaremos la función dyv recursiva que implementa el esquema divide y vencerás, `dyv(self, intervalo, k, e, minim=True)` los parámetros que le pasamos a la función son  los siguientes:
- **intervalo**: se refiere al intervalo [p0,p1] que se presenta en el problema, es este se encontrará el valor de k
- **k**: El valor en y que se pide encontrar.
- **e**: el epsilon, es decir el margen de error que puede tener la solución
- **minim**: es una varaiable que se usa para saber si se tiene que calcular el mínimo del interalo, ya que solo se realizará la primera interación.

#### Partes

##### Dividir 

En este problema hay dos formas de dividir. Una en la que se dividirá según el mínimo, el cual no tiene porque estar situado en el medio y otra en la que se partirá en el punto medio. En ambos casos se modifica el valor de `x0` donde se realizarán 2 llamdas recursdivas a la función una entre p0 y x0 (solo cuando k esté entre f(p0) y f(x0))y otra entre x0 y p1 (cuando k esté entre f(p1) y f(x0)).

##### Conquistar

El caso base será cuando la distancia del intervalo sea menor al epsilon dado, devolviendo una lista vacía. 

##### Combinar

En caso de que sea el puntop medio del intervalo el valor que buscamos se añadirea a la la solucion el valor.



### Abecelandia

En Abecelandia, ciudad famosa por sus N bellas plazas y que puede que conozcas, tienen un curioso sistema de carreteras: desde cada plaza sale una calle a todas las otras plazas que comienzan con una letra que se encuentre en su nombre (por ejemplo, de la plaza Aro salen calles que llevan a las plazas que empiezan por R, como las plaza Ruido y Reto, o por O, como la plaza Osa, pero no salen calles a plazas como Duende, Cascada o Tiara). Las calles son de sentido único (de la plaza Aro se puede ir a la plaza Ruido, pero no al
revés ya que no cumple la regla de las letras; obviamente, otras plazas como Aro y Osa están conectadas entre sí en ambas direcciones). Todas estas conexiones entre las N plazas están recogidas en un callejero, representado por una matriz de adyacencia de tamaño NxN; así, el valor de Callejero[p, q] indica si se puede ir de la plaza p a la plaza q. Se acerca el día 26 de Abril, festividad de San Isidoro de Sevilla (patrón de las Letras y, casualmente, de los informáticos), y en el Ayuntamiento de Abecelandia han decidido
que para celebrarlo van a invertir la dirección de todas las calles que conectan sus plazas.
En ese día no se podrá circular de Aro a Ruido, pero sí se permitirá ir de Ruido a Aro; obviamente, Aro y Osa seguirán conectadas entre sí. Diseñar formalmente un algoritmo Divide y Vencerás estándar que, teniendo por dato el callejero de la ciudad (representado por la matriz de adyacencia), obtenga el nuevo callejero válido para el día de San Isidoro de Sevilla, indicando las estructuras de datos que se utilicen.

La forma de repesentar las conexiones entre las distintas plazas se puede realizar con una matriz de adyacencia, donde la fila i y la columna j, tal que i = j, corresponden a una plaza, en caso de que haya una conexión se representa con un 1, sino es un 0. 

Por ejemplo para el siguiente grafo su matriz de adyacencia sería:

![image](https://github.com/MarcosFP812/PEC1-Algoritmia/assets/124279256/d5420eb2-2d21-44ba-97ac-22fcda0cf0ff)

|       | RUIDO | ORO  | OSA  | ARO   |
|-------|-------|------|------|-------|
| RUIDO | 0     | 1    | 1    | 0     |
| ORO   | 0     | 1    | 1    | 0     |
| OSA   | 0     | 0    | 0    | 1     |
| ARO   | 0     | 1    | 1    | 0     |

Ahora como se muestra en el enunciado invertimos las clases quedando de la siguiente forma

![image](https://github.com/MarcosFP812/PEC1-Algoritmia/assets/124279256/25373354-5002-44c1-9e2f-096aad56e987)

|       | RUIDO | ORO  | OSA  | ARO   |
|-------|-------|------|------|-------|
| RUIDO | 0     | 0    | 0    | 0     |
| ORO   | 1     | 1    | 0    | 1     |
| OSA   | 1     | 1    | 0    | 1     |
| ARO   | 0     | 0    | 1    | 0     |

Si nos fijamos atentamente la operación que se está realizando sobre la matriz es una transposición, esto consiste en cambiar las posiciones [i,j] por las posiciones [j,i]. Así pues para abordar la transposición de una matriz desde un enfoque divide y vencerás separaremos la matriz en 4 cuadrantes iguales en cada iteración (vease que la matriz debe ser cuadrada y de $2^nx2^n$), tantas veces como se necesarias, para después transponer esas submatrices y unirlas. De la siguiente manera:

| 0     | 0    | 0    | 0     |
|-------|------|------|-------|
| 1     | 1    | 0    | 1     |
| 1     | 1    | 0    | 1     |
| 0     | 0    | 1    | 0     |

Dividimos en cuadrantes:

| 0  | 0  |
|----|----|
| 1  | 1  |

| 0  | 0  |
|----|----|
| 0  | 1  |

| 1  | 1  |
|----|----|
| 0  | 0  |

| 0  | 1  |
|----|----|
| 1  | 0  |

Transponemos las submatrices:

| 0  | 1  |
|----|----|
| 0  | 1  |

| 0  | 0  |
|----|----|
| 0  | 1  |

| 1  | 0  |
|----|----|
| 1  | 0  |

| 0  | 1  |
|----|----|
| 1  | 0  |


Ahora unimos las submatrices transponiendolas:

| 0     | 1    | 1    | 0     |
|-------|------|------|-------|
| 0     | 1    | 1    | 0     |
| 0     | 0    | 0    | 1     |
| 0     | 1    | 1    | 0     |

El código proporcionado para resolver el problema es el siguiente:

```python= 
def transponer_matriz(matriz: list[list[int]]) -> list[list[int]]:
    #condicion de parada
    if len(matriz) == 1:
        return matriz
    else:
        submat = dividir_cuadrantes(matriz)

        for i in range(4):
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

```

Como se observa la solución es muy simple, solamente debemos de crear funciones que inicien una matriz de dimensiones deseadas, una que una los cuadrantes y otra que los divida. Con estas funciones podemos hacer el algoritmo DYV, la condición de parada será que la matriz sea 1x1 para que ocupe menos lineas de código (se podría parar en las 2x2 y devolver la matriz transpuesta), en caso de ser una matriz de tamaño menor la dividiremos y llamaremos a la función con cada una de las submatrices, una vez que termine las llamadas se unirán las matrices pero transponiendolas.



