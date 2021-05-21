# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 19:36:43 2021

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

#Inicio del ciclo
for conrepciclo in range(multiplicador+1) :
    resultado=tabla*conrepciclo
    sumaresultado=sumaresultado+resultado
    print(tabla, " * ", conrepciclo, "=", resultado)
   #Se imprime la suma por fuera del ciclo
print("La suma de los resultados es: ", sumaresultado)