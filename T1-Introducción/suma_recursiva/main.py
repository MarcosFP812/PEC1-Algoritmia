import sys
import sumaR as s
        
def main(argv):
    try:
        a = s.sumaR(int(argv[1]))
        print(a)
    except ValueError:
        print("Introduce un numero porfavor")
    except IndexError:
        print("Introduce el numero deseado en la ejecución del comando porfavor")

if __name__ == "__main__":
    if "--test" in sys.argv:
        import doctest
        doctest.test()
    else:
        main(sys.argv)     