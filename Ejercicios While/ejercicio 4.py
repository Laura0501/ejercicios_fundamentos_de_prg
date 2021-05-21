#Declaraciòn de variables
cantidad=0
x=1

#Inicio ciclo while
piezas=int(input("Cuantas piezas va a cargar: "))

while x<=piezas:
    largo=float(input("Ingrese la medida de la pieza: "))
    if  largo>=1.2 and largo<=1.3 : 
      cantidad=cantidad+1
    x=x+1
    
print("La cantidad de piezas aptas son:", cantidad)
    
    
    
    