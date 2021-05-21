# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 19:09:39 2021

@author: laura
"""

n_empleados1=int(input("Ingrese el numero de empleados: "))
k=int(input("Ingrese el numero de horas: "))
k1=int(input("ingrese el numeros de horas en que se debe realizar la actividad: "))
#k es horas
#k1 es el numero de horas en que los empleados deben realizar la actividad
n_empleados2=(k1*n_empleados1)/k
print("El numero de empleados que se necesitan para realizar la actividad es: ", n_empleados2)
