def saludos():
    print ("Función desde saludar.saludos()")
#saludos() 
#se llama la funcion desde el otro fichero
#Para evitar esto se debe usar:
if __name__ == "__main__":
    saludos()

class Hola:
    def __init__(self):
        print ("Desde Hola.__init__")