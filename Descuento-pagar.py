# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 13:32:39 2021

@author: laura
"""
compra=int(input("Ingrese el valor de la compra: "))
iva_pais=float(input("Ingrese el valor del iva de su pais: "))
iva=compra*iva_pais     
compra_con_iva=compra+iva
descuento=compra_con_iva*0.05    
elvalorapagar=compra_con_iva-descuento
print("El valor a pagar es: ", elvalorapagar)


