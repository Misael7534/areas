def cuadrado(lado1):
    if lado1<0 :
        return None
    cuadrado=lado1*lado1
    return cuadrado
#llama a la funcion del area del circulo
def area_circulo(radio):
    if radio <0:
        return None
    pi=3.14159
    area_circulo=pi*radio**2
    return area_circulo
#llama a la funcion del area del triangulo
def area_triangulo(base,altura):
    if base<0 or altura<0:
        return None
    triangulo_formula=(base*altura)/2
    return triangulo_formula