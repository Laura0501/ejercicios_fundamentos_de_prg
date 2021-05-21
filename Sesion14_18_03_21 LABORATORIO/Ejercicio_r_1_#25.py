# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:33:27 2021

@author: laura
"""

def retornar_sup(lado):
    sup=lado*lado
    return sup


# bloque principal del programa

va_cu=int(input("Ingrese el valor del lado del cuadrado:"))
superficie=retornar_sup(va_cu)
print("La superficie del cuadrado es",superficie)