def agregar_categoria():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    try:
        new_cat_name=[] 
        new_cat_name.append(input("Nombre: "))
        cursor.execute("INSERT INTO categoria VALUES(null, ?)", (new_cat_name),)
    except:
        print(f"La categoría {new_cat_name} ya existe")
    
    conexion.commit()
    conexion.close()
