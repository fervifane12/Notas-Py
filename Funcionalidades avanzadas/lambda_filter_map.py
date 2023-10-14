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

# Como dice su nombre, realiza un filtro de acuerdo a una condición (la función), y una lista u objeto iterable.

# Definimos una función que va a devolver un valor bool, y si se cumple la condición se va a devolver ese valor.
# Devuelve un objeto de tipo filter el cual es iterable, por lo que puede usarse la función next() para mostrar los valores.
# Estructura variable=filter(función filtro, iterador)

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

#La función map aplica una función definida a todos los elementos de un objeto iterable y devuelve un iterable de tipo map
#Ejemplo:

numeros= [2,4,6,8,10,12,14]

def doblar(nums):
    return nums*2

doble= list(map( doblar, numeros )) #Estructura: map(funcion, obj iterable/s), se utiliza la variable para guardar el resultado que se guarda
#como una lista para poder recorrerlo completo o también se puede usar la función next()
print (doble)

#Operar dos listas de la misma longitud

numeros1= [2,4,6,8,10,12,14]

numeros2= [1,2,3,4,5,6,7]

out=list( map (lambda a, b: a*b, numeros1, numeros2 )  ) #lambda val1, val2: operation, related variables(var1, var2, etc)
#
#  Change to list, function with the vars,
print(out)

class Personas:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        
    def __str__(self):
        return f"{self.name} de {self.age}"

personas= [Personas("Fernando", 23), Personas("Andres", 45),
           Personas("Eddy", 14), Personas("Luisa", 15)]

#Creando la función

def incrementar(persona):
    persona.age+=1
    return persona

personas= map( incrementar, personas )

for p in personas:
    print(p)

#Utilizando lambda

class Personas:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        
    def __str__(self):
        return f"{self.name} de {self.age}"

personas= [Personas("Fernando", 23), Personas("Andres", 45),
           Personas("Eddy", 14), Personas("Luisa", 15)]

personas= map( lambda persona: Personas(persona.name ,persona.age+1), personas)

for p in personas:
    print(p)