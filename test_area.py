# test_areas.py

from funciones import cuadrado, area_circulo, area_triangulo

# Pruebas de cuadrado
assert cuadrado(4, 4) == 16
assert cuadrado(-2, 5) is None

# Pruebas de círculo
assert round(area_circulo(2), 2) == 12.57
assert area_circulo(-1) is None

# Pruebas de triángulo
assert area_triangulo(6, 4) == 12
assert area_triangulo(-3, 5) is None

print("✅ Todas las pruebas pasaron correctamente.")