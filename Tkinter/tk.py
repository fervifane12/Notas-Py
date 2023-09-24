from tkinter import *

root = Tk()

root.title("Hola mundo")
root.resizable(1,1)#Permite redimencionar el cuadro
root.iconbitmap("icono.ico")


#FRAME

frame= Frame(root, width=240, height=240)#una porción del cuadro
frame.pack(side="bottom", anchor="center")
#(anchor= "e"--este; "w"--oeste;-- y todas las direcciones)
#(fill="x"-- expande en eje x)(fill="y", expand=1--expande en eje y)(fill="both"-- se adapta al tamaño)
frame.config(cursor="Pirate")
frame.config(bg="lightgreen")
frame.config(bd=12)
frame.config(relief="sunken")

root.config(cursor="arrow")#Todo el marco
root.config(bg="lightpink")
root.config(bd=5)
root.config(relief="sunken")


root.mainloop()