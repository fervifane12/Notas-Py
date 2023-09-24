from io import open
c=0
personas=[]
fichero=open("personas.txt", "r", encoding="utf8")
for i in fichero:
    personas.append((i.split(";")))
for id, nombre, apellido, nacimiento in personas:
    personas[c]= ({"id":id, "nombre" :nombre, "apellido" :apellido, "nacimiento": nacimiento})
    print (id, nombre, apellido, nacimiento)
    c=c+1
print (personas)
fichero.close()