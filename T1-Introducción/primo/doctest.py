from primo import es_primo
import matplotlib.pyplot as plt

def testmod():
    test_cases = [
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (8, False),
        (9, False),
        (10, False),
        (11, True),
        (12, False),
        (13, True),
        (14, False),
        (15, False),
        (16, False),
        (17, True),
        (18, False),
        (19, True),
        (20, False),
        (21, False),
        (22, False),
        (23, True),
        (24, False),
        (25, False),
        (26, False),
        (27, False),
        (28, False),
        (29, True),
        (30, False),
    ]
    
    for n, expected_result in test_cases:
        result = es_primo(n)
        print(f"Comprobando : {n} - Resultado {result}")
        assert result == expected_result, f"Para n={n}, se esperaba {expected_result} pero se obtuvo {result}"
    
    print("Todos los casos de prueba han pasado correctamente.")
