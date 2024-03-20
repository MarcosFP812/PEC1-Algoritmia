# Tema 1. Introducción

En esta sección realizaremos los primeros pasos para el análisis, diseño y aplicación de los algoritmos. Nos servirá para sentar las bases del futuro estudio exhaustivo a una serie de esquemnas algorítmicos.

## Conceptos clave

Antes de comenzar debemos repasar brevemente unos conceptos básicos.

- **Algortimo:** es un conjunto de pasos definidos y ordenados, que se debe de seguir para realizar una tarea en concreto. Cuando se le aporte una entrada válida el algoritmo debe devolver siempre una salida correcta dentro de los casos que el algoritmo afirma resolver. Es posible que para un mismo problema haya diferentes aproximaciones algorítmicas, pero deben de retornar el mismo valor.
- **Eficiencia:** La eficiencia de un algoritmo se refiere a su capacidad para resolver un problema de manera óptima, utilizando recursos como el tiempo y la memoria de manera eficiente. En el contexto del Principio de Invarianza, se establece que dos implementaciones diferentes de un mismo algoritmo no diferirán en eficiencia más que, a lo sumo, en una constante multiplicativa. Esto significa que si dos implementaciones consumen t1(n) y t2(n) unidades de tiempo respectivamente para resolver un caso de tamaño n, entonces siempre existe una constante positiva c tal que t1(n) <= c * t2(n), siempre que n sea suficientemente grande.
- **La complejidad:** se refiere a la cantidad de recursos computacionales, como el tiempo y la memoria, que requiere para ejecutar una tarea en función del tamaño de la entrada. En el contexto mencionado, se define que un algoritmo consume un tiempo de orden t(n), para una función dada t, si existe una constante positiva c y una implementación del algoritmo capaz de resolver cualquier caso del problema en un tiempo acotado superiormente por c * t(n) unidades de tiempo, donde n es el tamaño del caso considerado.
- **La notación asintótica:** denotada como O(f(n)), es una herramienta que describe cómo crece el tiempo de ejecución o la complejidad de un algoritmo en relación con el tamaño de la entrada, en términos asintóticos, es decir, para tamaños de entrada suficientemente grandes. Esto significa que cuando la función se acerque al infinito las constantes serán despreciables, por lo que no se tendrán en cuenta.

## Cálculo de la eficiencia

un código se compone de una serie de instrucciones, las cuales influiran en el rendimiento del algoritmo, ya que cada una de ellas consumirá recursos computacionales. Sin embargo no todas las operaciones influyen de la misma manera en la ejecución, por lo que las podemos diferenciar de la siguiente manera:

### Operaciones elementales
Una operación elemental es una operación cuyo tiempo de ejecución se puede acotar por una constante, independientemente del tamaño del conjunto de datos. Por simplicidad, se considera que el costo de una operación elemental es 1.
Las operaciones que se consideran como operaciones elementales incluyen operaciones aritméticas básicas, operaciones lógicas, operaciones de orden, lectura o escritura, asignación de valores y la instrucción de devolución.

### Operaciones condicionales
Estas vienen dadas por una condición la cual se debe evaluar siempre y posterirmente una sección de código en cada caso de la condición, la cual tomaremos la sección con mayor coste.

### Bucles
Para los bucles determinados, el costo incluye el máximo entre los costos de las variables de inicio y fin, junto con el costo acumulado de las instrucciones en el bucle.

### Operaciones Recursivas
Para determinar la eficiencia de un método recursivo, se utiliza el método de la ecuación característica, que consiste en encontrar las raíces de la ecuación matemática que representa el uso de recursos del método recursivo. Este método permite estimar la eficiencia de un algoritmo recursivo mediante el análisis de sus características de recursión.

## Calculo de la complejidad

Ahora nos centraremos en obtener el valor de complejidad anteriormente definido observando de manera exhaustiva el código del algoritmo. Para ello tenemos 2 reglas:

- **Regla de la suma:**

Consideremos dos segmentos de programa, P1 y P2, con tiempos de ejecución T1(n) y T2(n) respectivamente. Si T1(n) es O(f(n)) y T2(n) es O(g(n)), entonces el tiempo de ejecución de ejecutar primero P1 y luego P2, es decir T1(n) + T2(n), es O(max(f(n), g(n))). Por ejemplo, si tenemos un algoritmo con tres etapas, con tiempos de ejecución respectivos de O(n^2), O(n^3) y O(n log n), entonces:

El tiempo de ejecución de las dos primeras etapas ejecutadas secuencialmente es O(max(n^2, n^3)), es decir O(n^3).
El tiempo de ejecución de las tres etapas juntas es O(max(n^2, n^3, n log n)), es decir O(n^3).

- **Regla del producto:**
  
Si T1(n) y T2(n) son los tiempos de ejecución de dos segmentos de programa, P1 y P2, donde T1(n) es O(f(n)) y T2(n) es O(g(n)), entonces T1(n) * T2(n) es O(f(n) * g(n)). De esta regla se deduce que O(c * f(n)) es lo mismo que O(f(n)) si c es una constante positiva, por lo tanto, por ejemplo, O(n^2/2) es lo mismo que O(n^2).

## Ejercicios

### Numeros primos 

A continuación realizaremos un algoritmos, para su posterior análisis, que determine si un número recibido como parámetro es primo o no. 
Un número primo es un número natural mayor que 1 que solo es divisible por sí mismo y por 1. En otras palabras, un número primo es aquel que tiene exactamente dos divisores positivos: 1 y el propio número. Por ejemplo, los primeros números primos son 2, 3, 5, 7, 11, 13, 17, etc.
Por lo que al introducir alguno de los anteriores valores al algoritmo deberemos de obtener una respuesta afirmativa.

El algoritmo que decidiremos usar es muy simple, dado n, consiste en realizar el resto de n y de los valores que van desde 2 hasta n**0,5 uno a uno, en caso de que alguno de estos restos de 0, significa que ese valor es divisor de n por lo que no es primo, así que saldremos del bucle y concluiremos. Si completa el bucle entero siginifica que es primo.
Cabe destacar que este no es el algoritmo mas eficiente que se puede usar para solucionar este problema, pero es suficiente para un inicio.

Ahora analizaremos la eficiencia del algoritmo:

```python=
def es_primo(n):
    """
    es_primo ::[int] -> [bool]
    Indica si un numero es primo o no
    siendo n el numero a identificar
    """
    
    if n < 2:                             #+1
        return False                      #+1

    for i in range(2, int(n**0.5) + 1):      #sumatorio(   
        if n % i == 0:                       #+1
            return False                     #+1)
    return True                           #+1
```

Por lo que observamos que el tiempo de ejecución en función de n es:

$T(n) = 2 + \sum\limits_{i=2}^{\sqrt{n}} (2)$

Como estamos en notación asintótica podemos obviar que el bucle inicia en i=2, ya que con un n muy grande lo que aportan dichas iteraciones al tiempo de ejecución es despreciable.
Por lo que:

$T(n) = 3 + \sum\limits_{i=0}^{\sqrt{n}} (2)$ = $3 + 2*\sqrt{n}$

En base a este tiempo de ejecución podemos concluir que la complejidad de este algoritmo es:

$O({\sqrt{n}})$

### Suma recursiva

Consiste ne crear una función recursiva que devuleva el sumatorio de n desde 1 hasta n, tal que:

$S = \sum\limits_{i=0}^{n} (i) = 1+2+3+...+n-2+n-1+n$

Es un algoritmo muy simple puesto que usaremos como parámetros el número n y el resultado, en la recursión la condición de parada será cuando n = 0 y la llamada recursiva se realizará decrementando en 1 la n y sumando dicho valor de n al resultado, así se realizará hasta que llegue a n = 0 y devuelva el resultado.

```python= 
def sumaR(n, resultado = 0):
    if n =< 0:                          #+1
        return resultado                
    else:
        return sumaR(n-1, resultado+n)  #T(n-1)
```
La ecuación de recurrencia será:
$T(n) = 1 + T(n-1)$

$T(n) - T(n-1) = 1$

$x^n - x^{n-1} = 1$

Ecuación recursiva homogénea:

$x^{(H)} = x^n - x^{n-1} = 0 = x^{n-1}(x-1)$

La raíz es x = 1. Por lo que:

$x^{(H)} = A$

Ecuación particular:
$x^{(P)} = x^n - x^{n-1} = 1$

$x^{(P)} = nB$

$x = A + nB$

Por lo que la complejidad será
$O(n)$




