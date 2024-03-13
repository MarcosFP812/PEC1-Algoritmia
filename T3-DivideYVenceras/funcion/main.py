import funcion as f

def main():
    p = f.Polinomio([-2,1,1])
    print(p.__str__())

    intervalo = [-1,20]
    k = 1
    
    print(p.dyv(intervalo, k, 0.05))


main()