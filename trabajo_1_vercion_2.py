# cosas correjidas las funciones y una fallas de las opciones
#llamada de la funcion del area del cuadrado
def cuadrado(lado1):
    if lado1==0 :
        return None
    cuadrado=lado1*lado1
    return cuadrado
#llama a la funcion del area del circulo
def area_circulo(radio):
        if radio ==0:
            return None
        pi=3.14159
        area_circulo=pi*radio**2
        return area_circulo
#llama a la funcion del area del triangulo
def area_triangulo(base,altura):
        if base==0 or altura==0:
            return None
        triangulo_formula=(base*altura)/2
        return triangulo_formula
# menu para que sea mas facil el uso de el codigo y no proboque errores 
while True:
    print("\nSelecciona una opción:")
    print("1.- Area del cuadrado")
    print("2.- Area de un Circulo")
    print("3.- Area de un triangulo")
    print("4.- Finalizar")
    # es para la seleccion de la opcion
    try:
        op = int(input("Opción: "))
    except ValueError:
    # si por al guna rason pone una opcion que no este imprime esto
        print("Esa no es una opcion intente con una que este :)")
        continue
    if op ==4:
        print("Finalización completada")
        break
    try:
    # este de aqui esta para que si pone un numero que no este en la lista explique por que no hace nada 
        if op>=5:
                print("escoja una opcion que este")
                #op==" lo hice asi por que es el unico que solo pide un dato si seleccionas este para que solo pida un dato
        if op==2:
                valor1=float(input("Ingrese el radio en cm : "))
        elif op==1:
                # a qui es para los demas opciones para que pida sus dos datos
                valor1=float(input("Ingrese el lado del cuadrado en cm : ")) 
                #a qui ocupe diviir las cosas pra que se entienda en que unidad se meten los datos 
        elif op==3:
                # parte para las demas opciones las separe para que se entienda de que figura se mete 
                valor1=float(input("ingresa la base del triangulo en cm: "))
                valor2=float(input("ingrese la altura del triangulo en cm: "))
    except ValueError:
            print("Eso no es un numero por favor intente de nuevo")
            continue
    if op == 1:
            resultado=cuadrado(valor1)
            print("El resultado del Area del cuadardo es",resultado,"cm^2")
    # aqui es para que si selecciona la opcion 2 o 3 se ejecute
    elif op== 2:
            resultado=area_circulo(valor1)
            print("El area del circulo es",resultado,"cm^2")
    # aqui es para que si selecciona la opcion 3 se ejecute
    elif op==3:
            resultado=area_triangulo(valor1,valor2)
            print("El resultado del area del triangulo es",resultado,"cm^2")
    