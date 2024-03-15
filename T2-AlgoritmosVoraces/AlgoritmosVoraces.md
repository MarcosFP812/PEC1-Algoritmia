# Tema 2. Algoritmos Voraces

## Conceptos clave

Los algoritmos voraces son utilizados para resolver problemas de optimización. Funcionan eligiendo en cada paso la mejor opción disponible sin considerar futuras consecuencias. Se basan en tres condiciones: una entrada de tamaño n, un subconjunto de candidatos que cumple ciertas restricciones (llamado solución factible), y una función objetivo que se busca maximizar o minimizar. 

El proceso se realiza por pasos, añadiendo en cada uno el mejor candidato disponible según algún criterio de optimización. Después de cada paso, se verifica si el conjunto seleccionado es completable; si lo es, se incorpora al conjunto de escogidos, y si no, se rechaza y no se considera en el futuro. El algoritmo termina cuando se obtiene una solución, siendo correcto si la solución es siempre óptima. 

Aunque son eficientes y fáciles de diseñar, no todos los problemas pueden resolverse con algoritmos voraces, ya que en ocasiones no encuentran la solución óptima o ninguna solución.

El esquema general del algoritmo voraz es:

```python=
func voraz(candidatos)
  Solucion = []
```
