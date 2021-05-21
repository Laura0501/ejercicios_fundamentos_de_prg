# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:23:11 2021

@author: laura
"""

def mostrar_ma(v1,v2,v3):
    print("El valor mayor de los tres numeros es: ")
    if v1>v2 and v1>v3:
        print(v1)
    else:
        if v2>v3:
            print(v2)
        else:
            print(v3)


def cargar():
    va_1=int(input("Ingrese el primer valor:"))
    va_2=int(input("Ingrese el segundo valor:"))
    va_3=int(input("Ingrese el tercer valor:"))
    mostrar_ma(va_1,va_2,va_3)


# programa principal

cargar()