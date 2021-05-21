# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 21:58:20 2021

@author: laura
"""

hora_t=float(input("Ingrese el numero de horas trabajadas: "))
#hora_t son horas trabajadas

valor_h=float(input("Ingrese el valor de la hora trabajada en dolares: "))
#valor_h es valor de la hora trabajada

sueldo_neto=hora_t*valor_h
#sueldo neto

sueldo_cons=sueldo_neto - (sueldo_neto*0.08)
#sueldo_cons es sueldo con seguridad social

if sueldo_cons<= 300:
    bonificación=sueldo_cons+(sueldo_cons*0.02)
    print("Su sueldo con la bonificacion del 2% es:", bonificación, "dolares")

elif sueldo_cons>300:
    print("su sueldo es:", sueldo_cons, "dolares")
    
else :
    ("INCORRECTO")


