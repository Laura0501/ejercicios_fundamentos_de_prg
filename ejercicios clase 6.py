# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 19:47:11 2021

@author: laura
"""
ordenar= int(input("elija 1 si lo quiere de mayor a menor y 2 si lo quiere de menor a mayor"))
#Esta variable permite al usuario escoger como ordenar sus numeros

print("ingrese 3 numeros enteros diferentes")
#Aqui el usuario va a conocer cuantos numeros va a ingresar y saber que son enteros

n_1 = int(input("ingrese el numero 1:"))
#Usuario ingresara un primer numero de los que se van a ordenar

n_2 = int(input("ingrese el numero 2:"))
#Usuario ingresara un segundo numero de los que se van a ordenar

n_3 = int(input("ingrese el numero 3:"))
#Usuario ingresara un tercer numero de los que se van a ordenar

if (ordenar == 1):
#Es la condicion en donde el usuario escoge ordenar de mayor a menor
    
    if (n_1 > n_2):
#Condicion donde el primer numero es mayor que el segundo

        if (n_1 > n_3):
#Condicion donde el primer numero es mayor que el tercero

            if(n_2 > n_3):
#Condicion donde el segundo numero es mayor que el tercero

               print(n_1, n_2, n_3)
#Si se cumplen las condiciones anteriores se imprimiran los valores de n_1, n_2, n_3 de mayor a menor
               
            else:
#Si no se da cumplimiento a las condiciones anteriores
               
             print(n_1, n_3, n_2)
#Se imprimiran las variables de n_1, n_3, n_2 de mayor a menor
    
    if (n_3> n_1):
#Condicion donde el tercer numero es mayor al primero
       
        if (n_3 > n_2):
#Condicion donde el tercer numero es mayor al segundo

            if(n_2 > n_1):
#Condicion donde el segundo numero es mayor al primero

               print(n_3, n_2, n_1)
#Se imprimiran las variables n_3, n_2, n_1 de mayor a menor  
    
            else:
#Condicion si no se da cumplimiento a las condiciones anteriores

               print(n_3, n_1, n_2)
#Si se cumple la condicion anterior se imprimiran los valores n_3,n_1,n_2 de mayor a menor

    if (n_2 > n_1):
#Condicion donde el segundo numero es mayor al primero

        if (n_2 > n_3):
#Condicion donde el segundo numero es mayor al tercero

            if(n_1 > n_3):
#Condicion donde el primer numero es mayor al tercero

               print(n_2, n_1, n_3)
#Se imprimiran las variables n_2, n_1, n_3 de mayor a menor  

            else:
#Condicion Si no se da cumplimiento a las condiciones anteriores

               print(n_2, n_3, n_1)
#Si se cumple la condicion anterior se imprimiran los valores n_2,n_3,n_1 de mayor a menor


if (ordenar == 2):
#Es la condicion en donde el usuario escoge ordenar de menor a mayor

    if (n_1 < n_2):
#Condicion donde el primer numero es menor que el segundo

        if (n_1 < n_3):
#Condicion donde el primer numero es menor al tercero

            if(n_2 < n_3):
#Condicion donde el segundo numero es menor al tercero

               print(n_1, n_2, n_3)
#Se imprimiran las variables n_1, n_2, n_3 de menor a mayor

            else:
#Condicion Si no se da cumplimiento a las condiciones anteriores

               print(n_1, n_3, n_2)
#Si se cumple la condicion anterior se imprimiran los valores n_2,n_3,n_1 de menor a mayor

    if (n_3 < n_1):
#Condicion donde el tercer numero es menor al primero

        if (n_3 < n_2):
#Condicion donde el tercer numero es menor que el segundo
            
            if(n_2< n_1):
#Condicion donde el segundo numero es menor que el primero

               print(n_3, n_2, n_1)
#Se imprimiran las variables n_3, n_2, n_31 de menor a mayor

            else:
#Condicion Si no se da cumplimiento a las condiciones anteriores

               print(n_3, n_1, n_2)
#Si se cumple la condicion anterior se imprimiran los valores n_3,n_1,n_2 de menor a mayor 
   
    if (n_2 < n_1):
#Condicion donde el segundo numero es menor que el primero

        if (n_2 < n_3):
#Condicion donde el segundo numero es menor que el tercero

            if(n_1 < n_3):
#Condicion donde el primer numero es menor que el tercero

               print(n_2, n_1, n_3)
#Se imprimiran las variables n_2, n_1, n_3 de menor a mayor

            else:
#Condicion Si no se da cumplimiento a las condiciones anteriores

               print(n_2, n_3, n_1)
#Si se cumple la condicion anterior se imprimiran los valores n_2,n_3,n_1 de menor a mayor

if (n_1 == n_2):
#Condicion donde n_1 y n_2 son iguales

    print("n_2 y n_1 son iguales")
#Se imprimira n_2 y n_1 donde se informara que son iguales

    if (n_1 == n_3):
#Condicion donde n_1 y n_3 son iguales

        print("n_1 y n_3 son iguales")
#Se imprimira n_1 y n_3 donde se informara que son iguales

        if(n_2 == n_3):
#Condicion donde n_1 y n_3 son iguales

           print(" n_2 y n_3 con iguales")
#Se imprimira n_2 y n_3 donde se informara que son iguales

           if(n_1 == n_2 == n_3):
#Condicion donde n_1,n_2,n_3 son iguales

              print("todos son iguales")
#Se imprimira n_1, n_" y n_3 donde se informara que son iguales
            
            
            
            
                