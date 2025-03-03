import tkinter as tk 
import random as rd



window = tk.Tk()
window.title("interface exo 2")
canva = tk.Canvas(window, width=800, height=600, bg="black")

wi=800
he=600

def choix_couleur():
    tk.Entry("couleur")
def cercle(): 
    x=rd.randint(50, wi -50)
    y=rd.randint(50, he -50)
    canva.create_oval(x-50, y-50, x+50, y+50, fill=color)
    

def carre():
    canva.create_rectangle()

def croix():
    canva.create_oval()


b1 = tk.Button(window, text="choisir la couleur", padx=50, pady=10, 
                       bg="lightgrey")
b2 = tk.Button(window, text="cercle", padx=25, pady=5, 
                       bg="lightgrey", command=cercle)
b3 = tk.Button(window, text="carré", padx=25, pady=5,
                       bg="lightgrey", command=carre)
b4 = tk.Button(window, text="croix", padx=25, pady=5, 
                       bg="lightgrey", command=croix)

b1=b1.grid(column=1, row=0)
b2=b2.grid(column=0, row=1)
b3=b3.grid(column=0, row=2)
b4=b4.grid(column=0, row=3)

canva.grid(row=1, column=1, rowspan=3)
window.mainloop()
