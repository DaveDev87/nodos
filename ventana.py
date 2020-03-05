
#Este archivo no es importante para el proyecto

from tkinter import *
from nodos import *

window = Tk()
window.geometry("1200x900")
window.title("Carrito")


t = Text(window)


for item in caminos[0]:
    t.insert(END,"Complejidad: " + str(item.status) + "\n")
    t.insert(END, "Tiempo: " + str(item.tiempo) + "\n")
    t.insert(END, "Tipo: " + str(item.tipo) + "\n")
    t.insert(END, "Longitud: " + str(item.longitud) + "\n")
    t.insert(END, "Status: " + str(item.status) + "\n")
    t.insert(END, "\n")


t.grid()
t.configure(state=DISABLED)




window.mainloop()