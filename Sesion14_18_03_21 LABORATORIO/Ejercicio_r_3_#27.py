# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 16:59:17 2021

@author: laura
"""

def f_cargar_datos():
    nombre=[]
    edad=[]
    for x in range(5):
        v1=input("Ingrese el nombre de la persona:")
        nombre.append(v1)
        v2=int(input("Ingrese la edad:"))
        edad.append(v2)
    return [nombre,edad]


def f_pmayores_edad(nombre,edad):
    print("Nombres de personas mayores de edad")
    for x in range(len(nombres)):
        if edad[x]>=18:
            print(nombre[x])


def f_promedio_edades(edad):
    suma=0
    for x in range(len(edad)):
        suma=suma+edad[x]
    promedio=suma//5
    print("La edad promedio de las personas:",promedio)
    

# bloque principal
nombres,edades=f_cargar_datos()
f_pmayores_edad(nombres, edades)
f_promedio_edades(edades)  