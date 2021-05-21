# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 19:24:30 2021

@author: laura
"""

masa=float(input("Ingrese el valor de la masa de la caja en kg: "))
#masa del cuerpo a mover en la mesa

co_es=float(input("Ingrese el valor del coeficiente de rozamiento estatico:" ))
#co_es es el coeficiente de rozamiento estatico

gravedad=9.8

fuerza=masa*co_es*gravedad
print("La  fuerza que se debe aplicar para mover el cuerpo en la superficie horizontal es: ", fuerza)