#Función lambda

#Las funciones lambda, sirven para crear funciones anónimas
#Una función anónima es una función sin nombre, y en este caso, debe 
#ser una única expresión en lugar de un bloque

#Las funciones lambda sirven para hacer tareas sencillas y las 
#def para realizar tareas más extensas

#Funcion con def

def doblar(num):
    return num*2

print(doblar(4))

#Funcion lambda
#Se debe guardar en una variable

doblar1=lambda num: num*2
print(doblar1(5))

par=lambda num: num%2==0 #Comprueba una condición
print(par(4))

"""--------------------------------------------------------------------------------------------------------------------------------"""
#FUNCION FILTER

#Como dice su nombre, realiza un filtro de acuerdo a una condición (la función), y una lista u objeto iterable.
#Ejemplo:

numeros=[1,2,3,5,10,49,12,50,55]

def filtro(num):
    if num%5==0:
        return True
lista=filter(filtro, numeros)
print (list (lista))

#Filter con objetos de varios valores

class Personas:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        
    def __str__(self):
        return f"{self.name} de {self.age}"

personas= [Personas("Fernando", 23), Personas("Andres", 45),
           Personas("Eddy", 14), Personas("Luisa", 15)]

filt=filter(lambda persona: persona.age<18, personas)

for i in filt:
    print (i)

"""--------------------------------------------------------------------------------------------------------------------------------"""
#FUNCION MAP