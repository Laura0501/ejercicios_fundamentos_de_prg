# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 14:05:19 2021

@author: laura
"""

estatura=int(input("ingrese su estatura en centimetros:"))
peso=int(input("ingrese su peso en kilos:"))
estaturaametros=estatura/100
masa_corporal=peso/(estaturaametros*estaturaametros)
print("su masa corporal es:", masa_corporal)
