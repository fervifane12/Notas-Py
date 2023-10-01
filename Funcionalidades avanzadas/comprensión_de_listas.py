#Método tradicional

lista= []
for letra in "casa":
    lista.append(letra)

print(lista)

#Método comp listas

lista=[letra for letra in "casa"] #El valor que sale del bucle
#se guarda en la primer variable, y esta va a la lista.
print (lista)

#Método tradicional
lista=[]

for num in range(10):
    lista.append(2**num)
print (lista)

#MCL

lista=[2**num for num in range(10)]
print(lista)

#MT con una condición

lista=[]

for num in range(11):
    if num % 2 ==0:
        lista.append(num)
        
print (lista)

#MCL

lista=[num for num in range(11) if num%2==0] #la condición se pone al final
print(lista)

#También se pueden anidar listas dentro de las listas en el elemento a recorrer


multiples=[num for num in range(501) if num % 24==0]
