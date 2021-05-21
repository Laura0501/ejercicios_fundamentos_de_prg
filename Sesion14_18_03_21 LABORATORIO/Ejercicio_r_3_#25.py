# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:40:53 2021

@author: laura
"""

def largo_palabra(cadena):
    return len(cadena)


# bloque principal

nombre1=input("Ingrese primer nombre:")
nombre2=input("Ingrese segundo nombre:")
la_1=largo_palabra(nombre1)
la_2=largo_palabra(nombre2)
if la_1==la_2:
    print("Los nombres:",nombre1,nombre2,"tienen la misma cantidad de caracteres")
else:
    if la_1>la_2:
        print(nombre1,"es mas largo")
    else:
        print(nombre2,"es mas largo")