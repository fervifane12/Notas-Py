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
        cursor.execute("INSERT INTO categoria VALUES(null, ?)", (new_cat_name),)
    except:
        print(f"La categoría {new_cat_name} ya existe")
    
    conexion.commit()
    conexion.close()

agregar_categoria()