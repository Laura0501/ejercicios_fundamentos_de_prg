def f_carga_suma():
    valor1=int(input("Ingrese el primer valor:"))
    valor2=int(input("Ingrese el segundo valor:"))
    suma=valor1+valor2
    print("La suma de los dos valores es:",suma)


def f_separacion():
    print("*******************************")   
    
def f_finalización_prog():
    print("Esperamos que ta haya servido, ADIOS...")


# BLOQUE PRINCIPAL

for x in range(5):
    f_carga_suma()
    f_separacion()

f_finalización_prog()