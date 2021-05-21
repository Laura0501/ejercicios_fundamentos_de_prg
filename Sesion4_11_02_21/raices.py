# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 20:02:04 2021

@author: laura
"""

print("Se haran calculos con ecuaciones cuadraticas ax2+bx+c")
a=int(input("ingrese el valor de a: "))
b=int(input("ingrese el valor de b: "))
c=int(input("ingrese el valor de c: "))

#Aplicar ecuación cuadratica para hallar raices

import math
r=(b*b)-(4*a*c)
y= math.sqrt(r)

x1=(-(b)+(y))/(2*a)
#variable positiva

x2=(-(b)-(y))/(2*a)
#variable negativa

print("La raiz x1 es: ", x1)
print("La raiza x2 es: ", x2)