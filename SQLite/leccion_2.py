import sqlite3

conexion = sqlite3.connect("productos.db")
cursor= conexion.cursor()

#LLAVES PRIMARIAS--> db usuarios.db

#cursor.execute("""CREATE TABLE usuarios (
#        cedula INTEGER(10) PRIMARY KEY, #Esta clave primaria tiene una restricción de que
#no se puede repetir
#        nombre VARCHAR(100),
#        edad INTEGER,
#        email VARCHAR(100)
#    )
#   """)

#usuarios= [ #Lista con las correspondientes tuplas de datos
#    (1000539725, "Fernando", 23, "fernando@ejemplo.com"),
#    (1000204770, "Luisa", 21, "luisa@ejemplo.com"),
#    (4389284736, "Guillermina", 76, "guille@ejemplo.com"),
#    (8736154090, "Ivan", 78, "ivan@ejemplo.com")
#]

#cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)", usuarios)

#DATOS AUTOINCREMENTABLES--> db productos.db

#cursor.execute("""CREATE TABLE productos(
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    nombre VARCHAR(100) NOT NULL,
#    marca VARCHAR(50) NOT NULL,
#    precio FLOAT NOT NULL
#    )""")

#productos = [
#    ("Teclado", "Logitech", 85000),
#    ("Audifonos", "Redragon", 57000),
#    ("Mouse", "Lenovo", 38600),
#    ("Monitor", "Asus", 123000)
#]

#cursor.executemany("INSERT INTO productos VALUES (null, ?,?,?)", productos)

#Es posible crear una tabla que tenga un dato autoincrementable como PK y a su vez que otros
#datos sean únicos, esto se hace con el comando UNIQUE al frente de la creación del atributo
#SINTAXIS: 
#cursor.execute("""CREATE TABLE usuarios(
#    id INTEGER PRIMARY KEY AUTOINCREMENT,
#    cedula INTEGER(10) UNIQUE NOT NULL,--> UNIQUE para que el campo sea irrepetible
#    nombre VARCHAR(100) NOT NULL,
#    edad INTEGER NOT NULL,
#    email VARCHAR(50) NOT NULL,
#    )""")

conexion.commit()
conexion.close()