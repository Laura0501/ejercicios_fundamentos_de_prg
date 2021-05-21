# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:03:36 2021

@author: laura
"""

#Programa que lee una tabla y la imprime desde la 1 al 20 y suma los resultados

#Declarar variables 
tabla= 0
multiplicador= 1
resultado=0
sumaresultado=0
conrepciclo=1

#Leer el numero de la tabla por la cual vamos a realizar las operaciones
tabla =int(input("Tabla: "))

#Leer el multiplicador
multiplicador=int(input("Multiplicador: "))

#Inicio ciclo repetitivo WHILE

while(conrepciclo <= multiplicador):
    resultado=tabla*conrepciclo
    sumaresultado=sumaresultado+resultado
    print(tabla, " * ", conrepciclo, "=", resultado)
    #Incrementar la varibale que controla el ciclo
    conrepciclo=conrepciclo+1
print("La suma de los resultados es: ", sumaresultado)
    
    

