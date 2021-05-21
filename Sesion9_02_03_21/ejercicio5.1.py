# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 20:22:54 2021

@author: laura
"""

numero=0
suma=0
num_lista=int(input("Ingrese la cantidad de numeros de su lista sabiendo que el ultimo numero es negativo:"))

for i in range (num_lista):
    numero=float(input("Ingrese el numero: "))
    suma=suma+numero
print("La suma de los numeros es: ", suma)
media=suma/num_lista
print("La media de los numeros ingresados es:", media)