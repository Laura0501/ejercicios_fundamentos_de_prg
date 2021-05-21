# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 19:37:23 2021

@author: laura
"""

#Declarar variables

num=0    #Variable que almacena que alamacena los nuemros que digita el usuario
suma=0   #Variable que almacena que alamacena la suma de los numeros positivos
media=0.0  ##Variable que almacena la media
can_ele=0  #Variable que almacena la cantidad de numeros digitado

num=int(input("Numero: ")) #Lectura del primer numero

while (num>0):
    suma = suma+num
    num=int(input("Numero : "))#Lectura de los otros numeros
    can_ele=can_ele+1
    
#Termina el ciclo
if can_ele != 0 :
   media=suma/can_ele  #Calcular la media
   print("La media es: ", media) #Imprimir la media
   
else: print("No hay numeros para calcular")



    

