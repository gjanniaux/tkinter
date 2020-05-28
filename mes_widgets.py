# from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox as mbox
from tkinter import colorchooser as co

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
            #Suppression de l'objet
            reponse = mbox.askyesno("Suppression d'objet", "Êtes-vous certain de vouloir supprimer cet objet ?")
            if reponse:
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

#class MonCadre(tk.Frame):
class MonCadre(tk.Toplevel):
    def __init__(self, boss, *args, **kwargs):
        print(kwargs)   #Dictionnaire clé/valeur
        print(args)     #Tuple de paramètres
        tk.Toplevel.__init__(self, master=boss)
        self.__create_spinbox()
        self.__create_label()
        self.__layout()

    # Fonction privée
    def __create_spinbox(self):
        self.spin_boxes = []
        values = (400, 300, 200, 200)
        intervals = ((0, 800), (0, 800), (0, 800), (0, 600))

        for i in range(4):
            spin = ttk.Spinbox(self, from_=intervals[i][0], to=intervals[i][1])
            self.spin_boxes.append(spin)
            spin.set(values[i])

    def __create_label(self):
        self.labels = []
        values = ("X", "Y", "L", "H")
        for i in range(4):
            self.labels.append(tk.Label(self, text=values[i]))

    def __layout(self):
        values = ((1, 0), (1, 2), (1, 4), (1, 6))
        for i in range(4):
            self.labels[i].grid(row=values[i][0], column=values[i][1])

        spin_grid_tpl = ((1, 1), (1, 3), (1, 5), (1, 7))
        for i in range(4):
            self.spin_boxes[i].grid(row=spin_grid_tpl[i][0], column=spin_grid_tpl[i][1])

    def get_values(self):
        values = []
        for i in range(4):
            values.append(int(self.spin_boxes[i].get()))
        return values

#class MaGeometrie(tk.Frame):
class MaGeometrie(tk.Toplevel):
    def __init__(self, boss):
        tk.Toplevel.__init__(self, master=boss)

        self.formes = ttk.Combobox(self, values=["rectangle", "ovale"])
        # sticky values => w: ouest e: est n: nord s:sud
        self.formes.grid(row=2, columnspan=2, sticky="we")
        self.formes.set("rectangle")

        self.bouton_couleur = ttk.Button(self, text="Choisir une couleur", \
                                    command=self.__definir_couleur)
        self.bouton_couleur.grid(row=2, column=2, columnspan=2, sticky="e")

        # Frame
        self.frame_color = tk.Frame(self, width="60", height="20", bg="black")
        self.frame_color.grid(row=2, column=5, sticky="w")
        self.couleur = "white"

    def get_forme(self):
        return self.formes.get()

    def get_color(self):
        return self.couleur

    def __definir_couleur(self):
        couleur_tpl = co.askcolor()
        hexa_couleur = couleur_tpl[1]

        if hexa_couleur is not None:
            # print(hexa_couleur)
            self.couleur = hexa_couleur
            self.frame_color.configure(bg=hexa_couleur)
        else:
            print("Vous n'avez pas choisi de couleur")

if __name__ == '__main__':

    root = tk.Tk()
    geom = MaGeometrie(fen)
    #On démarre le gestionnaire d'événements
    root.mainloop()