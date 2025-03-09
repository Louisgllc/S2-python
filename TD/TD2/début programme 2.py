import tkinter as tk 
import random as rd

window = tk.Tk()
window.title("interface exo 2")
canva = tk.Canvas(window, width=720, height=480, bg="black", bd=7,
                          relief="raised", highlightthickness=10)

wi=720
he=480
#choisir la couleur
def choix_couleur():
    color= tk.Entry(window, width=25)
    color.pack()
    print("couleur changé !")

def cercle(): 
    x=rd.randint(67, wi -67)
    y=rd.randint(67, he -67)
    canva.create_oval(x-50, y-50, x+50, y+50, fill="blue")
    

def carre():
    L=rd.randint(100, wi -100)
    l=rd.randint(100, he -100)
    canva.create_rectangle(L, l, L+100, l+100, fill="red")

def croix():
    z=rd.randint(100, wi-100)
    q=rd.randint(100, he-100)
    canva.create_line(z, q, z+100,  fill="yellow")



b1 = tk.Button(window, text="choisir la couleur", font=("Georgia"), padx=50, pady=10, 
                       bg="lightgrey", bd=3, relief="ridge", command=choix_couleur)
b2 = tk.Button(window, text="cercle", font=("Georgia"), padx=25, pady=5, 
                       bg="lightgrey", bd=3, relief="raised", command=cercle)
b3 = tk.Button(window, text="carré", font=("Georgia"), padx=25, pady=5,
                       bg="lightgrey", bd=3, relief="raised", command=carre)
b4 = tk.Button(window, text="croix", font=("Georgia"), padx=25, pady=5, 
                       bg="lightgrey",bd=3, relief="raised", command=croix)

b1=b1.grid(column=1, row=0)
b2=b2.grid(column=0, row=1)
b3=b3.grid(column=0, row=2)
b4=b4.grid(column=0, row=3)

canva.grid(row=1, column=1, rowspan=3)

#pour afficher la fenetre
window.mainloop()
