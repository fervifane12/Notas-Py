import sqlite3

conexion = sqlite3.connect("ejemplo.db")

cursor= conexion.cursor()

#Crear una tabla

#cursor.execute("""CREATE TABLE usuarios (nombre VARCHAR(100), 
#               edad INTEGER, 
#               email VARCHAR(100))""")

#INSERTAR UN VALOR A LA TABLA

#cursor.execute("INSERT INTO usuarios VALUES ('Fernando', 23, 'fernando@ejemplo.com')") #Agregar valors a una tabla

#CONSULTAR UNO A UNO

#cursor.execute("SELECT * FROM usuarios") #Selecciona el primer dato presente en la base
#user=cursor.fetchone() #Transforma el dato en una tupla que sea legible
#print(user) 

#INSERTAR DATOS DE MANERA MASIVA

#usuarios= [ #Lista con las correspondientes tuplas de datos
#    ("Luisa", 21, "luisa@ejemplo.com"),
#    ("Guillermina", 76, "guille@ejemplo.com"),
#    ("Ivan", 78, "ivan@ejemplo.com")
#]

#cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios) #executemany sirve para hacer el proceso con varios elementos
#Primero el argumento de lo que se de desea hacer (?,?,?)-->Para los campos que tiene la tabla
#luego el segundo argumento es la lista con los datos que se van a agregar.

#CONSULTAR DE MANERA MASIVA DATOS

#cursor.execute("SELECT * FROM usuarios")

#users= cursor.fetchall()
#print(users)

conexion.commit() #Permite que se ejecute el código o el query anterior

conexion.close()