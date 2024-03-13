"""
OBJ: Este programa implementa el algoritmo de Divide y Vencerás para encontrar el valor de x donde f(x) = k, dado un polinomio.
IN: 
    - coeficientes: Una lista de coeficientes del polinomio.
    - intervalo: Un intervalo [a, b] donde se buscará el valor de x.
    - paso: Un valor opcional que indica el paso para la búsqueda del mínimo en el intervalo.
    - k: El valor objetivo que se desea encontrar.
    - e: La precisión o margen de error permitido.
    - minim: Un valor booleano opcional que indica si se busca el mínimo en el intervalo o no.
OUT:
    - Una lista de valores de x donde f(x) = k, dentro del intervalo especificado con una precisión dada.

"""

def distancia(i):
    """Calcula la distancia entre dos puntos en el intervalo."""
    return i[1] - i[0]

class Polinomio:
    def __init__(self, coeficientes):
        """
        OBJ: Inicializa un objeto Polinomio con los coeficientes dados.
        IN:
            - coeficientes: Una lista de coeficientes del polinomio.
        """
        self.coeficientes = coeficientes

    def evaluar(self, x):
        """
        OBJ: Evalúa el polinomio para un valor dado de x.
        IN:
            - x: El valor de x para el cual se evalúa el polinomio.
        OUT:
            - El resultado de evaluar el polinomio en x.
        """
        resultado = 0
        for i, coeficiente in enumerate(self.coeficientes):
            resultado += coeficiente * (x ** i)
        return resultado
    
    def encontrar_minimo_en_intervalo(self, intervalo, paso=0.01):
        """
        OBJ: Encuentra el mínimo local del polinomio en un intervalo dado.
        IN:
            - intervalo: El intervalo [a, b] donde se busca el mínimo.
            - paso: El tamaño del paso para la búsqueda del mínimo.
        OUT:
            - El valor de x donde se encuentra el mínimo local del polinomio en el intervalo dado.
        """
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

    def __str__(self):
        """
        OBJ: Representa el polinomio como una cadena de caracteres.
        OUT:
            - Una cadena que representa el polinomio.
        """
        resultado = ""
        for i, coeficiente in enumerate(self.coeficientes):
            if coeficiente != 0:
                if i == 0:
                    resultado += str(coeficiente)
                else:
                    resultado += f" + {coeficiente}x^{i}"
        return resultado

    def dyv(self, intervalo, k, e, minim=True):
        """
        OBJ: Implementación del algoritmo de Divide y Vencerás para encontrar el valor de x donde f(x) = k.
        IN:
            - intervalo: El intervalo [a, b] donde se busca el valor de x.
            - k: El valor objetivo que se desea encontrar.
            - e: La precisión o margen de error permitido.
            - minim: Un indicador booleano que especifica si se busca el mínimo en el intervalo.
        OUT:
            - Una lista de valores de x donde f(x) = k, dentro del intervalo especificado con una precisión dada.
        """
        solucion = []
        # Caso base: intervalo suficientemente pequeño.
        if distancia(intervalo) < e:
            return []
        else:
            v0 = self.evaluar(intervalo[0])  # Valor de f(x) en el extremo izquierdo del intervalo.
            v1 = self.evaluar(intervalo[1])  # Valor de f(x) en el extremo derecho del intervalo.
            
            if minim:
                # Si se busca el mínimo, encontrar el mínimo local.
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
                # Si k está entre v0 y f(x0), se busca en la mitad izquierda del intervalo.
                solucion += self.dyv([intervalo[0], x0], k, e, False)
            
            if self.evaluar(x0) < k < v1 or self.evaluar(x0) > k > v1:
                # Si k está entre f(x0) y v1, se busca en la mitad derecha del intervalo.
                solucion += self.dyv([x0, intervalo[1]], k, e, False)

        return list(set(solucion))
