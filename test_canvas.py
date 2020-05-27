# from tkinter import *
import tkinter as tk
from tkinter import ttk
import mes_widgets

# Mode False quand on dessine
# Mode True quand on supprime
mode = False

def dessiner():
    global mode

    if mode is False:
        # Lancer le processus de dessin
        valeurs = form_cadre.get_values()
        x, y, l, h = valeurs[0], valeurs[1], valeurs[2], valeurs[3]

        forme = geom.get_forme()
        couleur = geom.get_color()

        if couleur is None:
            couleur = "white"

        # print(type(x), type(y), type(l), type(h), forme)
        if forme == "rectangle":
            canvas.create_rectangle(x, y, x + l, y + h, fill=couleur)
        elif forme == "ovale":
            canvas.create_oval(x, y, x + l, y + h, fill=couleur)
        else:
            #tk.Message(fen, text="Forme non définie!")
            print("Forme non définie!")
    else:
        print("Pas de dessin en mode suppression")

def update_mode():
    global mode
    mode = bool(mode_suppr.var.get())
    print(mode)
    canvas.update_mode(mode)

fen = tk.Tk()
fen.title("Mon canvas interactif")

canvas = mes_widgets.MonCanvas(fen, 800, 600, "white")
canvas.grid(row=0, columnspan=8)

form_cadre = mes_widgets.MonCadre(fen)
form_cadre.grid(row=1, columnspan=8)

geom = mes_widgets.MaGeometrie(fen)
geom.grid(row=2, columnspan=5)

bouton = ttk.Button(fen, text="Dessiner!", command=dessiner)
bouton.grid(row=2, column=6)

v = tk.IntVar()
mode_suppr = tk.Checkbutton(fen, text="Supprimer", command=update_mode, variable=v)
mode_suppr.grid(row=2, column=7)
mode_suppr.var = v
print(mode)
# On démarre le gestionnaire d'événements
fen.mainloop()