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
            print("Forme non définie!")
    else:
        print("Pas de dessin en mode suppression")

def update_mode():
    global mode
    global radio_buttons
    global varGr
    if varGr.get() == 'S':
        mode = True
    else:
        mode = False
    #mode = bool(mode_suppr.var.get())
    #print(mode)
    canvas.update_mode(mode)

# Fenêtre d'application principale
root = tk.Tk()
root.title("Mon canvas interactif")

# Canvas: zone de dessin
canvas = mes_widgets.MonCanvas(root, 800, 600, "white")
canvas.grid(row=0, columnspan=8)

# Fenêtres de type Toplevel, indépendantes, donc pas de placement
form_cadre = mes_widgets.MonCadre(root, 2, "test", width="100", height="200", bg="white")
form_cadre.title("Dimensions")
geom = mes_widgets.MaGeometrie(root)
geom.title("Géométrie")

bouton = ttk.Button(root, text="Dessiner!", command=dessiner)
bouton.grid(row=2, column=6)

#Radiobutton
#Edition/Suppression
vals = ['E', 'S']
etiqs = ['Edition', 'Suppression']
varGr = tk.StringVar()
#Se positionner par défaut sur le mode Edition
varGr.set(vals[0])
radio_buttons = []
radio_frame = tk.Frame(root)
for i in range(2):
    b = ttk.Radiobutton(radio_frame, variable=varGr, text=etiqs[i], value=vals[i], command=update_mode)
    b.pack(side=tk.LEFT)
radio_frame.grid(row=2, column=7)

# On démarre le gestionnaire d'événements
root.mainloop()