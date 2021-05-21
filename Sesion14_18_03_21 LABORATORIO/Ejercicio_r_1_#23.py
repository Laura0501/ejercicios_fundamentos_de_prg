

def f_present_programa():
    print("Programa que permite cargar dos valores por teclado.")
    print("Se efectua la suma de los valores")
    print("Muestra el resultado de la suma")
    print("*******************************")


def f_carga_suma():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    suma=valor1+valor2
    print("La suma de los dos valores", valor1, "+12", valor2, "es =",suma)


def f_finalizacion():
    print("*******************************")    
    print("Gracias por utilizar este programa, ADIOS....")


# BLOQUE PRINCIPAL

f_present_programa()
f_carga_suma()
f_finalizacion()