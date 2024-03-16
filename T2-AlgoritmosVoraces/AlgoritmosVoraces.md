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
