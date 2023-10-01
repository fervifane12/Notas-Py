#Funciones generadoras

lista=[num for num in [1,2,3,4,5,6] if num%2==0]

#La función range--> es una función generadora, que proporciona dinámicamente una lista
#de acuerdo a los parámetros

lista=[num for num in range(0, 7) if num%2==0]

#Función generadora creada manualmente

def impares(num):
    for num in range(num):
        if num %2!=0:
            yield num

print(impares(10)) #Esta función nos devuelve un tipo de objeto que es iterable
#por lo que podemos usar un bucle for para recorrerlo

for num in impares(10):
    print(num)

#También se puede crear una lista con comprension de listas

lista=[num for num in impares(12)]
print (lista)

#Los generadores tienen muchas más funciones, ya que crean objetos con propiedades iterables
