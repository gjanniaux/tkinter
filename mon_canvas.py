# from tkinter import *
import tkinter as tk
import random

class MonCanvas(tk.Canvas):
    # Constructeur de la sous-classe/classe fille
    def __init__(self, conteneur, largeur, hauteur, couleur_fond):
        # Appeler le constructeur de la classe mère
        tk.Canvas.__init__(self, conteneur, width=largeur, height=hauteur, bg=couleur_fond)
        self.bind("<Button-1>", self.mouse_down)
        self.bind("<Button1-ButtonRelease>", self.mouse_up)
        self.bind("<Button1-Motion>", self.mouse_move)
        self.mode = False

    def mouse_down(self, event):
        self.sel_object = self.find_closest(event.x, event.y)
        if not self.mode:
            self.x_dep, self.y_dep = event.x, event.y
            self.itemconfig(self.sel_object, width=5)
            self.lift(self.sel_object)
        else:
            self.delete(self.sel_object)
    def mouse_up(self, event):
        self.itemconfig(self.sel_object, width=1)

    def mouse_move(self, event):
        dx = event.x - self.x_dep
        dy = event.y - self.y_dep
        self.move(self.sel_object, dx, dy)
        self.x_dep, self.y_dep = event.x, event.y

    def update_mode(self, mode_suppr):
        self.mode = mode_suppr
        if self.mode:
            self.configure(bg="red")
        else:
            self.configure(bg="white")

if __name__ == '__main__':
    # J'éxecute le fichier présent
    fen = tk.Tk()
    canvas = MonCanvas(fen, 500, 300, "black")
    canvas.pack()

    couleurs = ("white", "royal blue", "yellow", "green", "pink", "purple")

    for i in range(15):
        couleur = couleurs[random.randrange(6)]
        x_dep = random.randrange(400)
        y_dep = random.randrange(200)
        largeur = random.randrange(300)
        hauteur = random.randrange(300)
        canvas.create_rectangle(x_dep, y_dep, x_dep+largeur, y_dep+hauteur, \
                                fill=couleur)

    # On démarre le gestionnaire d'événements
    fen.mainloop()