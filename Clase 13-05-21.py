#Ejercicio que almacena en listas-procesa en funciones
#Declarar las librerias a usar para la solucion 

import matplotlib.pyplot as plt 

#General las listas con los datos inicializados
nombreproducto=['Ron','Aguardiente','Vino','Cerveza','Tequila']
existenciaproducto=[75,50,100,150,40]

#Funciones que resuelven el problema 
def f_cal_tlexist():
    sumaexistencias=0
    for poslis in range (4):
        sumaexistencias=sumaexistencias+existenciaproducto[poslis]
    print("Total existencias:", sumaexistencias)
    
def f_cal_tlexist_2():
    sumaexistencias=0
    for poslis in range (4):
        sumaexistencias=sumaexistencias+existenciaproducto[poslis]
    return(sumaexistencias)
    

#Función que calcula el promedio de las existencias
def f_calc_promexis():
    proexistencias=0.0
    proexistencias=f_cal_tlexist_2()/len(existenciaproducto)
    return(proexistencias)

#Llamadoa las funciones
f_cal_tlexist()
print("Total existencias 2: ", f_cal_tlexist_2())
print("Promedio de existencias:",f_calc_promexis())




#Graficar información 
fig, ax=plt.subplots()
#Definir el titulo del grafico
ax.set_title('GRAFICO DE EXISTENCIAS')
ax.set_xlabel('PRODUCTOS')
ax.set_ylabel('EXISTENCIAS')

#Crear el grafico 
plt.bar(nombreproducto,existenciaproducto)

#Publico el grafico
plt.show()