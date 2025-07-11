# test_area.py
# Asegúrate de que pytest esté instalado en tu entorno: pip install pytest
import pytest
from funciones import cuadrado, area_circulo, area_triangulo  # Cambia 'tu_modulo' por el nombre real del archivo .py

def test_cuadrado():
    assert cuadrado(0) is None
    assert cuadrado(5) == 25
    assert cuadrado(-3) == 9

def test_area_circulo():
    assert area_circulo(0) is None
    assert round(area_circulo(2), 5) == 12.56636
    assert round(area_circulo(-3), 5) == 28.27431

def test_area_triangulo():
    assert area_triangulo(0, 10) is None
    assert area_triangulo(5, 0) is None
    assert area_triangulo(4, 6) == 12
    assert area_triangulo(-4, 6) == -12
    assert area_triangulo(-4, -6) == 12
print("✅ Todas las pruebas pasaron correctamente.")