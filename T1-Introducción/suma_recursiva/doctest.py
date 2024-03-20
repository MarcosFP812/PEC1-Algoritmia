from sumaR import *


def test():
    # Casos de prueba
    test_cases = [
        (0, 0),
        (1, 1),
        (5, 15),
        (10, 55),
        (100, 5050)
    ]

    for n, expected_result in test_cases:
        result = sumaR(n)
        if result == expected_result:
            print(f"Test para n={n} PASÓ")
        else:
            print(f"Test para n={n} FALLÓ. Se esperaba {expected_result} pero se obtuvo {result}")
