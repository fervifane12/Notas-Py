from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

ruta= ""

def nuevo():
    global ruta
    mensaje.set("Nuevo archivo de texto")
    ruta=""
    texto.delete(1.0, "end")
    root.title("Archivo sin nombre - Editor F")

def abrir():
    global ruta
    mensaje.set("Abrir archivo")
    ruta= FileDialog.askopenfilename(initialdir=".",
            filetypes=(("Ficheros de texto", "*.txt"),),
            title="Abrir archivo de texto")
    if ruta != "":
        fichero= open(ruta, "r+")
        contenido= fichero.read()
        texto.delete(1.0, "end")
        texto.insert("insert", contenido)
        fichero.close()
        root.title(ruta + " - Editor F")

def guardar():
    
    mensaje.set("Guardar archivo")
    if ruta!= "":
        contenido=texto.get(1.0, "end-1c") #end-1c --> menos el último caracter que es un \n
        fichero=open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Guardar archivo")
    else:
        guardar_como()
    

def guardar_como():
    global ruta
    mensaje.set("Guardar archivo como")
    fichero= FileDialog.asksaveasfile(title="Guardar fichero", mode="w", defaultextension=".txt")
    if fichero is not None:
        ruta = fichero.name
        contenido = texto.get(1.0, "end-1c")
        fichero= open(ruta, "w+")
        fichero.write(contenido)
        fichero.close()
        mensaje.set("Guardado correctamente")
    else:
        mensaje.set("No se guardó")
        ruta=""
        
    

root=Tk()
root.title("Editor F")

#MENÚ DE OPCIONES

menubar= Menu(root)
root.config(menu=menubar)

filemenu=Menu(menubar, tearoff=0)
filemenu.add_command(label="Nuevo", command=nuevo)
filemenu.add_command(label="Abrir", command=abrir)
filemenu.add_command(label="Guardar", command=guardar)
filemenu.add_command(label="Guardar como", command=guardar_como)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)

menubar.add_cascade(label="Archivo", menu=filemenu)
#CUADRO DE TEXTO

texto=Text(root)
texto.pack(fill="both", expand=1)
texto.config(padx=15, pady=15, font=("Times New Roman", 12))

mensaje= StringVar()
mensaje.set("Bienvenido")
monitor=Label(root, textvar=mensaje, justify="left")
monitor.pack(side="left")

root.mainloop()