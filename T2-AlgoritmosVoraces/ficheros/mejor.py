import fichero as f

def mejor_prod(datos):
    """
    mejor :: list(ficheros) -> Fichero
    Devuelve el fichero cuyo producto sea mayor
    """
    primero = datos[0]
    
    for i in range(1, len(datos)):
        if (primero.producto() <= datos[i].producto()):
            primero = datos[i]
    return primero

def mejor_long(datos):
    """
    mejor :: list(ficheros) -> Fichero
    Devuelve el fichero cuya longitud sea menor
    """
    primero = datos[0]
    
    for i in range(1, len(datos)):
        if (primero.longitud >= datos[i].longitud):
            primero = datos[i]
    return primero


def mejor_pet(datos):
    """
    mejor :: list(ficheros) -> Fichero
    Devuelve el fichero cuyas peticiones sean menores
    """
    primero = datos[0]
    
    for i in range(1, len(datos)):
        if (primero.peticiones >= datos[i].peticiones):
            primero = datos[i]
    return primero

def mejor_div(datos):
    """
    mejor :: list(ficheros) -> Fichero
    Devuelve el fichero cuyo cociente sea menor
    """
    primero = datos[0]
    
    for i in range(1, len(datos)):
        if (primero.div() <= datos[i].div()):
            primero = datos[i]
    return primero

def leer(d, mejor, debugging=True):
    """
    leer :: [list(Ficheros), function] -> int
    Funcion que lee un conjunto de ficheros segun la politica que inidique la 
    funcion establecida, el metodo de lectura consiste en colocar un fichero 
    detras de otro para que se lean tantas veces como su numero de peticiones.
    Devuelve el tiempo que ha tardado el cojunto de ficheros en leerse
    """
    #Lista de candidatos
    datos = d[:]        #Se realiza una copia para eliminar la referenciacion
    datos_leer = []     #Lista en la que se guardará la solucion
    peticiones = 0      #Controla cuantas peticiones quedan en datos_leer
    tiempo_total = 0    #Tiempo que tarda en leerse

    #Bucle de lectura de los ficheros, sale de él si la suma de las peticiones 
    #es 0 y los candidatos se han acabado 
    while (peticiones != 0 or len(datos)!=0):
        
        peticiones = 0              #Iniciar el contador de peticiones

        #Añadir candidatos a la solucion
        if (len(datos)!=0):         #Si hay candidatos para seleccionar
            m = mejor(datos)        #Elegir al mejor con la f. seleccion
            datos_leer.append(m)    #Añadir a la solucion
            datos.remove(m)         #Eliminar el candidato

        #Leer la solucion
        for fichero in datos_leer:
            if debugging: print(fichero.longitud, fichero.peticiones, end=", ") #Debugging

            if(fichero.peticiones != 0): #Si el fichero aun no se ha leido
                fichero.peticiones -= 1  #tantas veces como peticiones
                                         #Reducir las peticiones

            tiempo_total += fichero.longitud    #Agregar al tiempo
            peticiones += fichero.peticiones    #Agregar las peticiones
            
        if debugging: print() #Debugging

    return tiempo_total


        
