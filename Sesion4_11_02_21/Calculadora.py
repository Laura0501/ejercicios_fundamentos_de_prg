# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 19:45:15 2021

@author: laura
"""

while True: 
  print("""
    Que operación va a realizar 
    1.Sumar
    2.Restar
    3.Multiplicar
    4.Dividir
    5.Potenciar
    6.Salida
        """)
  opcion= int(input("Seleccione la operación: "))
  
  if opcion==1:
      n_1= float(input("Ingrese el primer numero a sumar:"))
      n_2=float(input("Ingrese el segundo numero a sumar:"))
      print("La suma de los numeros es: ", n_1+n_2)
     
  elif opcion==2:
       n_1= float(input("Ingrese el primer numero a restar: "))
       n_2= float(input("Ingrese el segundo numero a restar: "))
       print("La resta de los numeros es: ",n_1-n_2 )
       
  elif opcion==3:
      n_1= float(input("Ingrese el primer numero a multiplicar:"))
      n_2= float(input("Ingrese el segundo numero a multiplicar:"))
      print("La multiplicacion de los numeros es: ",n_1*n_2 )
      
  elif opcion==4:
      n_1= float(input("Ingrese el primer numero a dividir:"))
      n_2= float(input("Ingrese el segundo numero a dividir:"))
      print("La multiplicacion de los numeros es: ",n_1/n_2 )
      
  elif opcion==5:
      base= float(input("Ingrese el numero base: "))
      potenciar= float(input("Ingrese el numero a potenciar: "))
      resultado=base**potenciar
      print("La potencia de los numeros ingresados es: ",resultado )
          
  elif opcion == 6:
      print("Salida", 6)
        
  else:
      ("EXISTE ERROR")
      

   
  
     
          
    