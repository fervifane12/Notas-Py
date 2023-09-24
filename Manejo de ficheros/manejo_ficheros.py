from io import open

"""

fichero = open ("fichero.txt", "w")
fichero.write(texto)
fichero.close()



fichero= open("fichero.txt", "r")
texto= fichero.read()
print (texto)
fichero.close()

fichero= open ("fichero.txt", "r")
lineas=fichero.readlines()
print (lineas)
print (lineas[-1])
print (lineas[0])
fichero.close()

fichero= open ("fichero.txt", "r")
linea=fichero.readline()
print (linea)
linea=fichero.readline()
print (linea)
fichero.close()



fichero= open ("fichero.txt", "a")
fichero.write("\nTercera linea del fichero")
fichero.close()



fichero= open ("fichero.txt", "r+") #Sirve para abrir un fichero en modo lectura y a su vez en modo escritura
fichero.seek(0)#pone el cursor en el lugar 0 del fichero
print (fichero.read())
fichero.close()

fichero= open ("fichero.txt", "r+")
fichero.seek(10)#Me selecciona el caracter 10 del fichero y empieza a leer a partir de allí
print (fichero.read())
fichero.close()

"""

fichero= open ("fichero.txt", "r+")
fichero.write("Modificación linea 1\n")
print (fichero.read())#Lee apartir de donde se realizó la modificación
fichero.seek(0)
print (fichero.read())
fichero.close()