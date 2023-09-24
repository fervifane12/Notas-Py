import pickle
from io import open

"""

lista=[1, 2, 3, 4, 5]
fichero=open ("lista.pckl", "wb")
pickle.dump(lista, fichero)
fichero.close()

fichero=open ("lista.pckl", "rb")
print (fichero.read())#Se lee el contenido en binario
fichero.close()

fichero=open ("lista.pckl", "rb")
lista_2=pickle.load(fichero)#El contenido del fichero lo pasamos a la variable y se interpreta el contenido
print (lista_2)
fichero.close()

"""

class Libro:
    
    def __init__(self, nombre):
        self.nombre=nombre
        
    def __str__(self):
        return self.nombre

nombres=["Un saco de huesos", "Creepshow", "El gen egoista", "Mary terror"]
libros=[]

for l in nombres:
    p=Libro(l)
    libros.append(p)

print (libros)

fichero = open ("Libros.pckl", "wb")
pickle.dump(libros, fichero)
fichero.close()

fichero=open("Libros.pckl", "rb")
read=pickle.load(fichero)
fichero.close()

for i in read:
    print (i)