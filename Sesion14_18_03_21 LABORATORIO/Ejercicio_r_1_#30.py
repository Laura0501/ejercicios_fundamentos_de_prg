def f_sumar(v_1,v_2,*lista):
    suma=v_1+v_2
    for x in range(len(lista)):
        suma=suma+lista[x]
    return suma


# bloque principal

print("La suma de 1+2")
print(f_sumar(1,2))
print("La suma de 1+2+3+4")
print(f_sumar(1,2,3,4))
print("La suma de 1+2+3+4+5+6+7+8+9+10")
print(f_sumar(1,2,3,4,5,6,7,8,9,10))

