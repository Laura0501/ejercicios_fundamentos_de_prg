# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 18:34:21 2021

@author: laura
"""
"""
Programa que lee el nombre y la nota definitiva de tres materias(basic,fortran,pascal)
"""
#Area de declaracion de variables

var_nombre="***"
var_e_bas=0.0
var_e_for=0.0
var_e_pas=0.0

var_p_s_medEst=0.0
var_p_s_conEst=0

#Leer nombre
var_nombre=input("Digite el nombre del estudiante: ")

#Inicio el ciclo while

while(var_nombre!= "***"):
#Inicio del ciclo
    var_e_bas=float(input("Definitiva Basic: "))
    var_e_for=float(input("Definitiva Fortran: "))
    var_e_for=float(input("Definitiva Pascal: "))
    
#Proceso que calcula la media del estudiante
    var_p_s_medEst= (var_e_bas+var_e_for+var_e_pas)/3
    print("La media de",var_nombre," es:",var_p_s_medEst)
    var_nombre=input("Digite el nombre del estudiante: ")
    var_p_s_conEst=var_p_s_conEst+1
#Fin del ciclo
print("Cantidad de Estudiantes : ", var_p_s_conEst)
print("Adiós....")


