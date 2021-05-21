

#Programa que calcula el cuadrado de los 100 números

#Area de declaracion de variables 

acu_suma=0
cuadrado_num=0
num=1
contador_rep_while=1

#Entradas
cantidad_de_numeros=int(input("Cantidad de numeros : "))

#Procesos
#Ciclo para de 1 hasta 100

while contador_rep_while<=cantidad_de_numeros:
    cuadrado_num=contador_rep_while*contador_rep_while
    acu_suma=acu_suma+cuadrado_num
    print("El cuadrado de", contador_rep_while, "es: ", cuadrado_num)
    print("La suma acumulada es: ", acu_suma)
    contador_rep_while=contador_rep_while+1
#Fin ciclo

print("La suma de los cuadrados es: ", acu_suma)