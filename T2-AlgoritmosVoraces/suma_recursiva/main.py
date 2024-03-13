import sys
import sumaR as s
        
def main(argv):
    try:
        a = s.sumaR(int(argv[1]))
        print(a)
    except ValueError:
        print("Introduce un numero porfavor")
    except IndexError:
        print("Introduce el numero porfavor")

if __name__ == "__main__":                                                      # Si este modulo es el principal 
    if "--test" in sys.argv:
        import doctest
        doctest.testsuma()
    main(sys.argv)     