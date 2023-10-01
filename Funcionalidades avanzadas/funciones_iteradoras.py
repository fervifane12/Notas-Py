#Funciones iteradoras

#Las funciones generadoras devuelven un objeto con propiedades iterables, 
#esto nos permite controlar el proceso de generación.
#Teniendo en cuenta que cada vez que la función generadora
#cede un elemento, queda suspendida y se retoma el control hasta que
#se le pide generar el siguiente valor.

def impares(num):
    for num in range(num):
        if num %2!=0:
            yield num
            
impar = impares(6)

print(next(impar))
print(next(impar))
print(next(impar)) #Si se acaban los elementos iterables, genera un error
#StopIteration

#La función next, solo se puede usar para objetos que tengan cualidad iterable
#Las listas o strings no entran allí
#Pero podemos modificarlas para que tengan cualidad iterable
#Ejemplo:

lista=[1,2,3,4,5]
#next(lista) Genera error

#Usamos la función iter()

lista=iter(lista)

print (next(lista)) #Ahora sí permite recorrer los elementos con la función next()

#El mismo proceso se puede usar para str's


