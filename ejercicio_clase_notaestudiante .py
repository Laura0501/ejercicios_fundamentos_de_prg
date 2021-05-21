# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 18:47:08 2021

@author: laura
"""

#Programa que calcula la nota de un estudiante 

#Entradas 
#Pedir nombre de estudiante y notas de los 3 parciales

canest=int(input("Cantidad de Estudiantes: "))
#inicializar la variable que controla el ciclo 
conrep=0

#variable real para sumar las definitivas del grupo
sumadefgrup=0.0

#Variable para calcular la nota promedio del grupo
notaprodefgrup=0.0

while(conrep < canest):
     #Instrucciones a repetir
     nomestudiante=input("Nombre del estudiante: ")
     not1_est=float(input("Parcial 1: "))
     not2_est=float(input("Parcial 2: "))
     not3_est=float(input("Parcial 3: "))

     #Calculos 
     notadef_est=(not1_est+not2_est+not3_est)/3
     
     #Acumular las definitivas del grupo
     sumadefgrup=sumadefgrup+notadef_est

     #Imprimir los resultados- Salida 
     print(f"La nota definitiva es :{notadef_est :.2f}")
     
     #Incrementar la variable que controla el ciclo
     conrep=conrep+1

