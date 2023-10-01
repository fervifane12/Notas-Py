 #Los ámbitos nos hacen referencia al nivel en el que se encuentra una función o un dato
 #Por ejemplo:
def func_global():
     
    def func_local():
         return "Hola"
     
    return func_local

#func_local() aparece NameError: name 'func_local' is not defined. Did you mean: 'func_global'?.
#Ya que la función no está definida globalmente

print (func_global())

"""----------------------------------------------------------------------------------------------------------------"""


def func_global1():
    
    def func_local1():
        return "Hola"
    print (locals()) #Imprime las definiciones locales que hay en la función

print (func_global1())

"""----------------------------------------------------------------------------------------------------------------"""

lista=[1,2,3,4]

def func_global2():
    
    num=50 #Se muestra como local
    
    def func_local2():
        return "Hola"
    
    print (locals())
    print (globals()) #Función que imprime todos los elementos del ámbito global
    
print(func_global2()) #La manera en que se enseñand los elementos es como un diccionario, por lo que es posible usar métodos de diccionarios
#Ejemplo

print (globals().keys())

"""----------------------------------------------------------------------------------------------------------------"""

def func_global3():
    
    def func_local3():
        print ("Hola")
    
    return func_local3
print (func_global3())

"""----------------------------------------------------------------------------------------------------------------"""

#Funciones como variables

#Ya que al ejecutar una función estamos llamando directamente a la función local, podemos guardar su valor en una variable
#Ejemplo:

def func_global00():
    
    def func_local00():
        return "Hola"
    
    return func_local00()

funcion= func_global00() #En este caso, el valor de la variable no es dependiente de la original, por lo que si se llegase a borrar esta
#no se llegaría a eliminar el valor de la variable "funcion"
print (funcion)

"""----------------------------------------------------------------------------------------------------------------"""

#Funciones como args

def func00():
    return "Hola"

def func_con_arg(funcion):
    print (funcion)
    
func_con_arg(func00())

"""----------------------------------------------------------------------------------------------------------------"""

#FUNCIONES DECORADORAS

#Estas funciones sirven para envolver la ejecución de una función. Están pensadas para reutilizarse
#EJEMPLO

def func_prueba():
    print("Hola!")

def monitor(funcion):
    
    def decorar():
        
        print ("\t Ejecución iniciada de", funcion.__name__)
    
        funcion()
    
        print("\t Finalizando ejecucion de ", funcion.__name__)
    
    return decorar

#Usaré la función del punto anterior func00()

monitor(func_prueba)() #El segundo paréntesis hace referencia a la ejecución de la función interna

#Esta sintaxis es muy complicada por lo que se simplifica de la siguiente manera

@monitor
def func_prueba1():
    print("Hola!")

@monitor
def func_prueba2():
    print("Adios!")
    
#Ya cuando se ejecuten las funciones, el decorador "monitor", estará presente
print("\n")
func_prueba1()
func_prueba2()

#Hasta el momento, no se pueden pasar argumentos a la función, para ello debemos hacer uso de la siguiente herramienta

def monitor_args(funcion):
    
    def decorar(*args, **kwargs):
        print ("\t Ejecución iniciada de", funcion.__name__)
        
        funcion(*args, **kwargs)
        
        print ("\t Ejecución iniciada de", funcion.__name__)
    
    return decorar

@monitor_args
def func_prueba1(nombre):
    print(f"Hola! {nombre}")

@monitor_args
def func_prueba2(nombre):
    print(f"Adios! {nombre}")

func_prueba1("Fernando")
func_prueba2("Fernando")

