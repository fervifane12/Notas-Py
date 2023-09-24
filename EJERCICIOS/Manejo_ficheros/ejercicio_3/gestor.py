from io import open
import pickle

fichero=open ("Personajes.pckl", "ab")
fichero.close()

class Personaje:
    
    
    caract=[]
    
    def __init__(self, nombre, vida, ataque, defensa, alcance):
        self.nombre=nombre
        self.vida=vida
        self.ataque=ataque
        self.defensa=defensa
        self.alcance=alcance
        
        self.caract.append({"Nombre":self.nombre, "Vida": self.vida, "Ataque": self.ataque,
                            "Defensa": self.defensa, "Alcance": self.alcance})
        
        #SAVE
        fichero= open ("Personajes.pckl", "rb+")
        
        pickle.dump(self.caract, fichero)
        
        fichero.close()
        return self.caract
    
    
    def __str__(self):
        return f"""características: 
    Vida: \t{self.vida} 
    Ataque: \t{self.ataque} 
    Defensa: \t{self.defensa} 
    Alcance: \t{self.alcance}"""
    
    def __del__(self):
        pass
        
        

class Caballero(Personaje):
    
    def __init__(self, nombre, vida, ataque, defensa, alcance):
        super().__init__(nombre, vida, ataque, defensa, alcance)
        print(f"Se ha creado el Caballero {self.nombre} con " + super().__str__())
    
    def __str__(self):
        return "Caballero con " + super().__str__()

class Guerrero(Personaje):
    
    def __init__(self, nombre, vida, ataque, defensa, alcance):
        super().__init__(nombre, vida, ataque, defensa, alcance)
        print(f"Se ha creado el Guerrero {self.nombre} con " + super().__str__())
        
    def __str__(self):
        return "Guerrero con " + super().__str__()

class Arquero(Personaje):
    
    def __init__(self, nombre, vida, ataque, defensa, alcance):
        super().__init__(nombre, vida, ataque, defensa, alcance)
        print(f"Se ha creado el Arquero {self.nombre} con " + super().__str__())
        
    def __str__(self):
        return "Arquero con " + super().__str__()

"""
c=Caballero("Lae'zel", 4, 2, 4, 2)
g=Guerrero("Brook", 2, 4, 2, 4)
a=Arquero("Looter", 2, 4, 1, 8)
b=Arquero("Prueba", 2, 4, 1, 8)


fichero= open ("Personajes.pckl", "rb")
read=pickle.load(fichero)
fichero.close()
for i in read:
    print (i)
"""


#Para el gestor solo es necesario retirar los datos del pckl y modificar los dict


def eliminar(nombre):
    personajes=[]
    c=0
    
    fichero=open("Personajes.pckl", "rb")
    personajes= pickle.load(fichero)
    fichero.close()
    
    for i in personajes:
        if i[]


eliminar("Prueba")

"""
fichero= open ("Personajes.pckl", "rb")
read=pickle.load(fichero)
fichero.close()

for i in read:
    print (i)
    
"""