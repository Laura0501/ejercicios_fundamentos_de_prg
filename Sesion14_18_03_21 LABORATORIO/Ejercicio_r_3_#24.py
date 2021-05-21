# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:26:07 2021

@author: laura
"""

def mostrar_peri(lado):
    per=lado*4
    print("El perimetro es",per)


def mostrar_sup(lado):
    sup=lado*lado
    print("La superficie es",sup)


def cargar_dato():
    la=int(input("Ingrese el valor del lado de un cuadrado:"))
    respuesta=input("Quiere calcular el perimetro o la superficie[ingresar texto: perimetro/superficie]?")
    if respuesta=="perimetro":
        mostrar_peri(la)
    if respuesta=="superficie":
        mostrar_sup(la)


# programa principal

cargar_dato()