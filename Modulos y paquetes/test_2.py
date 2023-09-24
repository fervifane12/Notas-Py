from paquetes.hola.saludar import saludos, Hola #Si se desea importar más funciones, se hace con "," y si se desea importar todo con un "#"
from paquetes.adios.despedida import despedir, Despedir
from paquetes.modificar_nums.modificar import modificar

#De este modo importamos la función específica que deseamos
lista=[0,15,6,9,74,-5,-55,-12,4,-7]
#Para llamarla, solo se debe escribir el nombre de la función

saludos()
Hola()

despedir()
Despedir()

modificar(lista)
