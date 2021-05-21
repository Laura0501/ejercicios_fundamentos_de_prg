# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:16:39 2021

@author: laura
"""

def mostrar_men(mensaje):
    print("*************************************************")
    print(mensaje)
    print("*************************************************")

def carga_suma():
    v_1=int(input("Ingrese el primer valor:"))
    v_2=int(input("Ingrese el segundo valor:"))
    suma=v_1+v_2
    print("La suma de los dos valores es:",suma)


# programa principal

mostrar_men("El programa calcula la suma de dos valores ingresados por teclado.")
carga_suma()
mostrar_men("Gracias por utilizar este programa")