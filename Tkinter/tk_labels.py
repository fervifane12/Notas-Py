from tkinter import *

"""
--------------------------------------------------------
#Popups avanzados

from tkinter import messagebox as MessageBox #as, cambia el nombre del fichero que importamos
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

root= Tk()

def test():
    #ColorChooser.askcolor(title="Elige un color") #Devuelve el código del color en RGB y hexadecimal
    #FileDialog.askopenfilename(title="Abre un fichero",
    #    filetypes=(("Ficheros de texto", "*.txt"), # si se pone solo un archivo se debe dejar una coma luego del primer filetype
    #    ("Archivos PNG", "*.png")))#Restringe los tipos de ficheros a los seleccionados
    fichero=FileDialog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension=".txt") #Devuelve el fichero con la ruta y el modo ("w" por defecto)
    if fichero is not None:
        fichero.write("Texto de prueba") #Me crea el fichero con el texto
        fichero.close()
    
Button(root, text="Click", command=test).pack()


--------------------------------------------------------
#popups

from tkinter import messagebox as MessageBox

root= Tk()

def test():
    #MessageBox.showinfo("Istalación de mi juego","¿Deseas continuar con la instalación?")
    MessageBox.showwarning("Aviso", "Sección solo para administradores")
    #showerror es igual que los anteriores
    #askquestion permite elegir entre dos opciones "Si" o "No" y guarda el valor
    #askokcancel es igual que el anterior, pero devuelve un valor bool
    #askretrycancel devuelve el valor en bool igual que el anterior, pero las opciones son diferentes

Button(root, text="Click", command=test).pack()


--------------------------------------------------------
#Menus
root=Tk()

menubar=Menu(root)
root.config(menu=menubar)

filemenu=Menu(menubar, tearoff=0) #Tearoff quita la opción por defecto
filemenu.add_command(label="Nuevo archivo")
filemenu.add_command(label="Abrir")
filemenu.add_command(label="Guardar")
filemenu.add_command(label="Cerrar")
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

editmenu=Menu(menubar, tearoff=0)

helpmenu=Menu(menubar, tearoff=1)


menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)



--------------------------------------------------------
#Check buttons

def solucion():
    como=""
    
    if (queso.get()):
        como+="Con queso"
    else:
        como+="Sin queso"
    if (chocolate.get()):
        como+=" y con chocolate"
    else:
        como+=" y sin chocolate"
        
    monitor.config(text=como)

root= Tk()
root.title("Panadería")
root.config(bd=15)

queso=IntVar()      #1 para sí, 0 para no
chocolate=IntVar()  # //    //

Label(root, text="¿Cómo quieres tu pan?").pack()
Checkbutton(root, text="Con queso", variable=queso, onvalue=1, offvalue=0, command=solucion).pack()
Checkbutton(root, text="Con chocolate", variable=chocolate, onvalue=1, offvalue=0, command= solucion).pack()

monitor=Label(root)
monitor.pack()

--------------------------------------------------------
#Botones radiales

def seleccionar():
    monitor.config(text=f"{opcion.get()}") #Hace que el label monitor muestre el valor de la opción seleccionada

def reiniciar():
    opcion.set(None) #Deselecciona el Radio button 
    monitor.config(text="") #Borra el contenido del monitor

root = Tk()

opcion=IntVar() #Tipo de variable que configuramos para el radiobutton

Radiobutton(root, text="Opcion 1", variable=opcion, value=234, command=seleccionar).pack() #value es el valor que toma la variable (float en este caso)
Radiobutton(root, text="Opcion 2", variable=opcion, value=12, command=seleccionar).pack() #variable es la variable 
Radiobutton(root, text="Opcion 3", variable=opcion, value=43, command=seleccionar).pack()

monitor=Label(root)
monitor.pack()

Button(root, text="Reiniciar", command=reiniciar).pack()

#Ejecución del bucle de la aplicación
root.mainloop()

--------------------------------------------------------
#Botones
#1
def hola():
    print ("Hola mundo")

def crear_label():
    Label(root, text="Label creada").pack()

root = Tk()

Button(root, text="Continuar", command=hola).pack() #realiza lo que dice la función(imprime en el terminal)
Button(root, text="Opcion 2", command=crear_label).pack() #crea un label en el archivo


#Ejecución del bucle de la aplicación
root.mainloop()

#2
#Operaciones
def suma():
    r.set(float(n1.get())+float(n2.get()))
    borrar()

#Para que se borren los resultados luego de copiar
def borrar():
    n1.set("")
    n2.set("")

root = Tk()

n1= StringVar()
n2= StringVar()
r= StringVar()

Entry(root, justify="center", textvariable=n1).pack()
Entry(root, justify="center", textvariable=n2).pack()
Entry(root, justify="center", textvariable=r, state="disabled").pack()
Button(root, text="Sumar", command=suma).pack() 

#Ejecución del bucle de la aplicación
root.mainloop()

--------------------------------------------------------

#Cuadro grande de texto

texto=Text(root)
texto.pack(side="left")
texto.config(width=30, height=10, font=("Times New Roman", 11))

--------------------------------------------------------

#Entry (campos de texto)

#1
#Campo Nombre
frame=Frame(root)
frame.pack()

entry= Entry(frame) #Sirve para introducir un campo de texto
entry.pack(side="right")

label=Label(frame, text="Nombre\t")
label.pack(side="left")
#Campo apellido
frame2=Frame(root)
frame2.pack()

entry= Entry(frame2) #Sirve para introducir un campo de texto
entry.pack(side="right")

label=Label(frame2, text="Apellido\t")
label.pack(side="left")

#2
#Campo Nombre

entry= Entry(root) 
entry.grid(row=0, column=1) #Arriba a la derecha
entry.grid(sticky="w", padx=3, pady=3) #pad, da un espacio = al # de pixeles mencionados
entry.config(justify="right", state="disabled") #Justificar y seleccionar el estado del cuadro

label=Label(root, text="Nombre")
label.grid(row=0, column=0) # Arriba a la izquierda
label.grid(sticky="w", padx=3, pady=3)# Justifica hacia la orientación brindada

#Campo apellido

entry1= Entry(root) 
entry1.grid(row=1, column=1, sticky="w", padx=3, pady=3)#Abajo a la derecha 
entry1.config(justify="center", show="*")#Muestra el caracter que seleccionamos

label1=Label(root, text="Apellido")
label1.grid(row=1, column=0, sticky="w", padx=3, pady=3) #Abajo a la izq

--------------------------------------------------------

#Para poner una imagen como un .gif

imagen=PhotoImage(file="imagen.gif")
Label(root, image=imagen, bd=10).pack(side="bottom")

#Variables dinámicas

texto=StringVar()
texto.set("Un texto nuevo")

#Configuración de un marco

frame=Frame(root, width=480, height=320)
frame.pack()

Label(root, text="Primera linea").pack(anchor="nw")
label = Label(root, text="Segunda linea")
label.pack(anchor="center")
Label(root, text="Tercera linea").pack(anchor="se")


label.config(bg="green", fg="white", font=("Verdana", 20))
label.config(textvariable=texto)

--------------------------------------------------------

label= Label(frame, text="Hola mundo")
label.place(x=200, y=200)

#Si no usamos el frame (o marco)

Label(root, text="Primera linea").pack(anchor="nw")
Label(root, text="Segunda linea").pack(anchor="center")
Label(root, text="Tercera linea").pack(anchor="se")

Label(root, text="Primera linea").pack(side="left")
Label(root, text="Segunda linea").pack(side="top")
Label(root, text="Tercera linea").pack(side="right")
--------------------------------------------------------


"""