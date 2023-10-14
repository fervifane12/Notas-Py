#Se conocen como "regex" o "regexp", son patrones de búsqueda definidos con una sintaxis regular.
import re

#re.search() busca un patrón en una cadena
#Ejemplos:

cadena= "Cadena de texto con una frase especial"

palabra= "especial"

found= re.search ( palabra, cadena ) #Se deben definir ambas variables, el patrón que se busca, y la cadena donde se va a buscar

print (found.start()) #Donde empieza el match
print (found.end()) #Donde termina el match
print (found.span()) #Rango donde está el match
print (found.string) #Devuelve el string

print (found) # se crea un objeto de tipo re.match, 

#re.match("palabra", cadena), encuentra match al inicio de la cadena

cadena= "Cadena de texto"

print(re.match("Cadena", cadena))
print(re.match("de", cadena))

#re.split("caracter a partir del cual dividir", cadena de texto)

cadena= "Dividir la cadena de texto "

print(re.split(" ", cadena))

#re.sub("coincidencia", "reemplazo", cadena de texto)

cadena= "Sustitución de una cadena: perro"

print(re.sub("perro", "gato", cadena))

#re.findall("(coincidencia_1|coincidencia_2)", cadena de texto)

cadena= "Cadena repetida tiene repetida la palabra repetida"

print (re.findall("repetida", cadena))#Encuentra las veces que está repetida una palabra o cadena y las pone en una lista

print(re.findall("(Cadena|repetida|la)", cadena))

