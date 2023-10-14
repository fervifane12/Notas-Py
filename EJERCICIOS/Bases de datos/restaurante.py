import sqlite3

def crear_bd():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    
    try:
        cursor.execute("""CREATE TABLE categoria (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR (100) UNIQUE NOT NULL)""")
        
        cursor.execute("""CREATE TABLE plato (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100) UNIQUE NOT NULL,
            categoria_id INTEGER NOT NULL,
            FOREIGN KEY (categoria_id) REFERENCES categoria(id))""")
    
    except:
        cursor.execute("SELECT * FROM categoria")
        categorias= cursor.fetchall()
        cursor.execute("SELECT * FROM plato")
        platos= cursor.fetchall() 
        print( f"Categorías registradas: {categorias} \nPlatos registrados: {platos}")
    
    conexion.commit()
    conexion.close()
    
def agregar_categoria():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    try:
        new_cat_name=input("Nombre: ")
        cursor.execute("INSERT INTO categoria VALUES(null, ?)", [new_cat_name],)
    except:
        print(f"La categoría {new_cat_name} ya existe")
    
    conexion.commit()
    conexion.close()

def primeros():
    conexion =sqlite3.connect("restaurante.db")
    cursor=conexion.cursor()
    
    cursor.execute("SELECT * FROM plato WHERE categoria_id=1")
    primeros_platos = cursor.fetchall()
    print(f"Los primeros platos son: \n{primeros_platos}")
    try:
        nuevo_plato = input("Ingresa el nuevo plato: ")
        cursor.execute("INSERT INTO plato VALUES(null, ?, 1)", [nuevo_plato],)
    except:
        print(f"El plato {nuevo_plato} ya existe")
    
    conexion.commit()
    conexion.close()

def segundos():
    conexion =sqlite3.connect("restaurante.db")
    cursor=conexion.cursor()
    
    cursor.execute("SELECT * FROM plato WHERE categoria_id=2")
    segundos_platos = cursor.fetchall()
    print(f"Los segundos platos son: \n{segundos_platos}")
    try:
        nuevo_plato = input("Ingresa el nuevo plato: ")
        cursor.execute("INSERT INTO plato VALUES(null, ?, 2)", [nuevo_plato],)
    except:
        print(f"El plato {nuevo_plato} ya existe")
    
    conexion.commit()
    conexion.close()
    
def postres():
    conexion =sqlite3.connect("restaurante.db")
    cursor=conexion.cursor()
    
    cursor.execute("SELECT * FROM plato WHERE categoria_id=3")
    postre = cursor.fetchall()
    print(f"Los postres son: \n{postre}")
    try:
        nuevo_plato = input("Ingresa el nuevo plato: ")
        cursor.execute("INSERT INTO plato VALUES(null, ?, 3)", [nuevo_plato],)
    except:
        print(f"El plato {nuevo_plato} ya existe")
    
    conexion.commit()
    conexion.close()

def agregar_plato():
    while True:
        opcion=int (input("""
 ¿Qué deseas cambiar?
[1] Primeros
[2] Segundos
[3] Postres
[4] Crear categoría
[5] Salir
                """))
        try:
            if opcion==1:
                primeros()
            elif opcion==2:
                segundos()
            elif opcion==3:
                postres()
            elif opcion==4:
                agregar_categoria()
            elif opcion==5:
                print ("Cerrando el aplicativo")
                break 
        except:
            print (f"""
                   El valor {opcion} no es válido.
                   Intenta nuevamente""")

def mostrar_menu():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    
    while True:
        opcion=int (input("""
    ¿Qué platos deseas ver?
[1] Primeros
[2] Segundos
[3] Postres
[4] Salir
                """))
        try:
            if opcion==1:
                cursor.execute("SELECT * FROM plato WHERE categoria_id=3")
                prim=cursor.fetchall()
                print (f"Primeros platos:\n{prim}")
            elif opcion==2:
                cursor.execute("SELECT * FROM plato WHERE categoria_id=1")
                segs=cursor.fetchall()
                print (f"Segundos platos:\n{segs}")
            elif opcion==3:
                cursor.execute("SELECT * FROM plato WHERE categoria_id=2")
                post=cursor.fetchall()
                print (f"Primeros platos:\n{post}")
            elif opcion==4:
                print ("Cerrando el aplicativo")
            break 

        except:
                print (f"""
                   El valor {opcion} no es válido.
                   Intenta nuevamente""")
    conexion.commit()
    conexion.close()


