from io import open



class Contador:
    
    contador=None
    
    def __init__(self, funcion):
        self.funcion=funcion
        fichero=open("contador.txt", "r+")
        
        if funcion == "inc":
            if len (fichero.read())==0:
                fichero=open("contador.txt", "r+")
                fichero.write("0")
                self.contador = fichero.read()
                fichero.close()
                print ("El contador es: " + str(self.contador))
                
            else:
                fichero=open("contador.txt", "r+")
                contador = int(fichero.read())
                contador= contador + 1
                fichero.seek(0)
                fichero.write(str(contador))
                print ("El contador es: " + str(contador))
                fichero.close()
            
        elif funcion == "dec":
            
            if len (fichero.read())==0:
                fichero=open("contador.txt", "r+")
                fichero.write("0")
                self.contador = fichero.read()
                fichero.close()
                print ("El contador es: " + str(self.contador))
            else:
                    fichero=open("contador.txt", "r+")
                    contador = int(fichero.read())
                    fichero.seek(0)
                    contador= contador - 1
                    fichero.write(str(contador))
                    print ("El contador es: " + str(contador))
                    fichero.close()
        else:
            fichero=open("contador.txt", "r+")
            self.contador = fichero.read()
            print ("El contador es: " + str(self.contador))
            fichero.close()

c=Contador("inc")
c.__init__(4)
