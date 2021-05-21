#Factura de venta

def f_titulo():
    print("Calculo el valor de la factura ")
    
def f_despedida():
    print(".....ADIOS.....")

def f_valorfactura(): #Encabezado de la funcion
   #Desarrolo de la funcion 

   #Definicion de variables
   ve_nom_art="a"
   ve_cant_art=0
   ve_valor_uniart=0.0

   cons_porc_iva=0.19
 
   vps_netopagar=0.0
   vps_ivapagar=0.0
   vps_totalpag=0.0


   #Entrada de articulos
   ve_nom_art=input("Articulo: ")
   ve_cant_art=int(input("Cantidad: "))
   ve_valor_uniart=float(input("Valor unitario: "))

   #Procesos
   vps_netopagar=ve_cant_art*ve_valor_uniart
   vps_ivapagar=vps_netopagar*cons_porc_iva
   vps_totalpag=vps_netopagar+vps_ivapagar

   #Salidas 
   print("El neto es: ", vps_netopagar)
   print("El iva a pagar es: ", vps_ivapagar)
   print("El total a pagar es:", vps_totalpag)

#Llamado a la funcion
f_titulo()
f_valorfactura()
f_despedida()
