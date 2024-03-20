
class Fichero:
    def __init__(self, l, p) -> None:
        self.longitud = l
        self.peticiones = p
    
    def producto(self):
        return self.longitud*self.peticiones
    
    def div(self):
        return self.peticiones/self.longitud

    def p(self):
        print(self.longitud, self.peticiones)

