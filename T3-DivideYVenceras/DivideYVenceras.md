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



