from tkinter import *
from tkinter import messagebox as MessageBox 
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

def fuente():
    pass

root=Tk()
root.title("Editor de texto")

#BARRA DE CONFIGURACIONES



#CONFIGURACIÓN DEL TEXTO

frame=Frame(root, height=90, bg="#E1E0DC")
frame.pack(fill="x", side="top")
frame.config(bd=10)

#Cambio fuente

fuente=list()

frame_1=Frame(frame, height=60, width=150)
frame_1.grid(row=0, column=0)
frame_1.config(bd=10)

#Cambio de tamaño de letra

frame_2=Frame(frame, height=60, width=150)
frame_2.grid(row=1, column=0)
frame_2.config(bd=10)

#Cambio del color

frame_3=Frame(frame, height=60, width=150)
frame_3.grid(row=2, column=0)
frame_3.config(bd=10)

#CAMPO DE ESCRITURA

texto=Text(root, height=700)
texto.pack(anchor="center")
texto.config(bd=15)
root.mainloop()