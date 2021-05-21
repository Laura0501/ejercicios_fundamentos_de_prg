# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 18:49:50 2021

@author: laura
"""

#Programa que calcula el cuadrado de los 100 números

#Area de declaracion de variables 

acu_suma=0
cuadrado_num=0
num=1

#Entradas
cantidad_de_numeros=int(input("Cantidad de numeros : "))

#Procesos
#Ciclo para de 1 hasta 100

for num in range(1,cantidad_de_numeros+1,1):
    cuadrado_num=num*num
    acu_suma=acu_suma+cuadrado_num
    print("El cuadrado de", num, "es: ", cuadrado_num)
    print("La suma acumulada es: ", acu_suma)
#Fin ciclo

print("La suma de los cuadrados es: ", acu_suma)