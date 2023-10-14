import sqlite3

conexion = sqlite3.connect("usuarios_autoincremental.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM usuarios WHERE id=1")


usuario=cursor.fetchone()
print(usuario)

conexion.commit()
conexion.close()