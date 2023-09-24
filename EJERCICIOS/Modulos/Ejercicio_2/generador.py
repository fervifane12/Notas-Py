import random
import math
def leer_numero(ini,fin,mensaje):
    while True:
        try:
            num = int( input(mensaje) )
        except:
            print (f"Debe ser un número entre {ini} y {fin}")
        else:
            if num >= ini and num <= fin:
                break
    return num


def generador():
    numeros= leer_numero(1,20, "¿Cuantos números quieres generar?")
    modo = leer_numero(1, 3, """ 
¿Como quieres que se redondee?
[1]Al alza
[2]A la baja
[3]Normal\n""")
    lista=[]
    lista_2=[]
    for x in range(numeros):
        lista.append(random.uniform(1,100))
    if modo==1:
        for i, v in enumerate(lista):
            lista_2.append(math.ceil(lista[i]))
            print(f"{v} redondeado {lista_2[i]}")
    elif modo==2:
        for i, v in enumerate(lista):
            lista_2.append(math.floor(lista[i]))
            print(f"{v} redondeado {lista_2[i]}")
    elif modo==3:
        for i, v in enumerate(lista):
            lista_2.append(round(lista[i]))
            print(f"{v} redondeado {lista_2[i]}")
    else:
        print ("Introduzca un valor correcto")
    print (lista)
    print (lista_2)
generador()