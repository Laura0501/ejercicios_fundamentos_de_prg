# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:38:33 2021

@author: laura
"""

def retornar_mayor(v_1,v_2):
    if v_1>v_2:
        return  v_1
    else:
        return  v_2



# bloque principal
valor_1=int(input("Ingrese el primer valor:"))
valor_2=int(input("Ingrese el segundo valor:"))
print("El mayor valor de los dos numeros es: ", retornar_mayor(valor_1,valor_2))
