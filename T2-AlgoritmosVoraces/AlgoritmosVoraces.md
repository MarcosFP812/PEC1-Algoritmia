# Tema 2. Algoritmos Voraces

## Conceptos clave

Los algoritmos voraces son utilizados para resolver problemas de optimización. Funcionan eligiendo en cada paso la mejor opción disponible sin considerar futuras consecuencias. Se basan en tres condiciones: una entrada de tamaño n, un subconjunto de candidatos que cumple ciertas restricciones (llamado solución factible), y una función objetivo que se busca maximizar o minimizar. 

El proceso se realiza por pasos, añadiendo en cada uno el mejor candidato disponible según algún criterio de optimización. Después de cada paso, se verifica si el conjunto seleccionado es completable; si lo es, se incorpora al conjunto de escogidos, y si no, se rechaza y no se considera en el futuro. El algoritmo termina cuando se obtiene una solución, siendo correcto si la solución es siempre óptima. 

Aunque son eficientes y fáciles de diseñar, no todos los problemas pueden resolverse con algoritmos voraces, ya que en ocasiones no encuentran la solución óptima o ninguna solución.

El esquema general del algoritmo voraz es:

```python=
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
```python=
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
```python=
def mejor_long(datos):
    primero = datos[0]
    for i in range(1, len(datos)):
        if (primero.longitud >= datos[i].longitud):
            primero = datos[i]
    return primero
```
Sin embargo esta solución es incompleta, puesto que es posible que aunque tenga un tamaño pequeño puede que sus peticiones sean también pocas por lo que se estará iterando con 0 peticiones una gran cantidad de veces, lo que significa que se está perdiendp tiempo en un fichero ya leido. Recordemos que el objetivo es no malgastar lecturas en primera instancia. Así pues obtenemos la siguiente función:
```python=
def mejor_pet(datos):
    primero = datos[0]
    for i in range(1, len(datos)):
        if (primero.peticiones >= datos[i].peticiones):
            primero = datos[i]
    return primero
```
Pero con esta aproximación no tenemos en cuenta la longitud por lo que a igualdad de numero de peticiones no hay ninguna forma de discriminar el que tenga menor longitud, puesto que sería lo más eficiente. Así pues debemos de buscar una relación entre ambos valores, la cual puede ser un producto o un cociente.
Respecto al producto no será la opción más óptima por motivos parecidos al de la longitud, por lo que el mayor cociente entre peticiones y longitud será la mejor opción, ya que si tienen una longitud grande, el cociente será menor, por lo que según el criterio se encolarán al final. En caso de ser muy demandante de peticiones su cociente será mayor y por lo tanto mejor colocarlo de los primeros. De esta forma sería el código:
```python= 
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



