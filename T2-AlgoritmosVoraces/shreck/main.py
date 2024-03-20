
import random as r

def mejor_escalera(lista):
    menor = lista[0]
    for elem in lista[1:]:
        if elem < menor:
            menor = elem
    return menor

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
            print(elem, end=' ')
            tiempo_total += elem
        print("Total: ", tiempo_total)
    return tiempo_total

def sumatorio(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

for i in range(0, 5):
    lista = [r.randint(1,10),r.randint(1,10),r.randint(1,10)
                           ,r.randint(1,10),r.randint(1,10),r.randint(1,10)
                           ,r.randint(1,10),r.randint(1,10),r.randint(1,10)]
    total = sumatorio(lista)
    t1 = seleccionar_escaleras(lista, total, mejor_escalera)

    print(t1)