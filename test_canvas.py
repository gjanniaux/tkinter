# from tkinter import *
import tkinter as tk
from tkinter import ttk
import mon_canvas

# Mode False quand on dessine
# Mode True quand on supprime
mode = False

def dessiner():
    global mode
    if mode is False:
        # Lancer le processus de dessin
        x = int(x_depart.get())
        y = int(y_depart.get())
        l = int(largeur.get())
        h = int(hauteur.get())
        forme = formes.get()
        couleur = couleurs.get()
        print("Couleur:", couleur, type(couleur))
        if len(couleur) > 0:
            # print(type(x), type(y), type(l), type(h), forme)
            if forme == "rectangle":
                canvas.create_rectangle(x, y, x + l, y + h, fill=couleur)
            elif forme == "ovale":
                canvas.create_oval(x, y, x + l, y + h, fill=couleur)
            else:
                #tk.Message(fen, text="Forme non définie!")
                print("Forme non définie!")
        else:
            print("Couleur non définie!!")
    else:
        print("Pas de dessin en mode suppression")

def update_mode():
    global mode
    mode = bool(mode_suppr.var.get())
    print(mode)
    canvas.update_mode(mode)

fen = tk.Tk()
fen.title("Mon canvas interactif")

canvas = mon_canvas.MonCanvas(fen, 800, 600, "white")
canvas.grid(row=0, columnspan=8)

# x_depart = tk.Entry(fen)
# x_depart.insert(0, "100")
# y_depart = tk.Entry(fen)
# y_depart.insert(0, "100")
# largeur = tk.Entry(fen)
# largeur.insert(0, "200")
# hauteur = tk.Entry(fen)
# hauteur.insert(0, "200")
x_depart = ttk.Spinbox(fen, from_=0, to=800)
x_depart.set(400)
y_depart = ttk.Spinbox(fen, from_=0, to=800)
y_depart.set(300)
largeur = ttk.Spinbox(fen, from_=0, to=800)
largeur.set(200)
hauteur = ttk.Spinbox(fen, from_=0, to=600)
hauteur.set(200)

x_label = tk.Label(fen, text="X")
y_label = tk.Label(fen, text="Y")
l_label = tk.Label(fen, text="L")
h_label = tk.Label(fen, text="H")

x_label.grid(row=1, column=0)
x_depart.grid(row=1, column=1)
y_label.grid(row=1, column=2)
y_depart.grid(row=1, column=3)
l_label.grid(row=1, column=4)
largeur.grid(row=1, column=5)
h_label.grid(row=1, column=6)
hauteur.grid(row=1, column=7)

formes = ttk.Combobox(fen, values=["rectangle", "ovale"])
# sticky values => w: ouest e: est n: nord s:sud
formes.grid(row=2, columnspan=2, sticky="we")
formes.set("rectangle")

couleurs = ttk.Combobox(fen, values=["white", "green", "blue", \
                                     "cyan", "red", "grey", "pink"])
couleurs.grid(row=2, column=2, columnspan=2)
couleurs.set("white")

bouton = ttk.Button(fen, text="Dessiner!", command=dessiner)
bouton.grid(row=2, column=5)

v = tk.IntVar()
mode_suppr = tk.Checkbutton(fen, text="Supprimer", command=update_mode, variable=v)
mode_suppr.grid(row=2, column=7)
mode_suppr.var = v
print(mode)
# On démarre le gestionnaire d'événements
fen.mainloop()