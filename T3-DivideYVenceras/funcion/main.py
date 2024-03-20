import funcion as f

def main():
    p = f.Polinomio([-2,1,1])
    print("El polinomio es ", p.__str__())
    print("El intervalo ", [-2,2])
    print("La k es ", 1)
    intervalo = [-1,20]
    k = 1
    
    print(p.dyv(intervalo, k, 0.05))


main()