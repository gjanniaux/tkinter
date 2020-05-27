import tkinter as tk
from tkinter import ttk
import random

class MyCanvas(tk.Canvas):
    def __init__(self, parent, w=200, h=200, background='black'):
        tk.Canvas.__init__(self, parent, width=w, height=h, bg=background)
        self.bind("<Button-1>", self.mouseDown)
        self.bind("<Button1-ButtonRelease>", self.mouseUp)
        self.bind("<Button1-Motion>", self.mouseMove)
        self.suppression = False

    def setMode(self, sup):
        self.suppression = sup
        print("Canvas en mode suppression: ", self.suppression)

    def getMode(self):
        return self.suppression

    def mouseDown(self, event):
        # print(event.x, ", ", event.y)
        self.down_x, self.down_y = event.x, event.y
        self.selObject = self.find_closest(event.x, event.y)
        if self.suppression:
            canvas.delete(self.selObject)
        else:
            self.itemconfig(self.selObject, width=5)
            # Passer au premier plan l'objet selectionné
            self.lift(self.selObject)

    def mouseUp(self, event):
        print(self.selObject)
        if self.selObject:
            self.itemconfig(self.selObject, width=1)
            self.selObject = None

    def mouseMove(self, event):
        new_x, new_y = event.x, event.y
        # Décalage entre le point de clic et le point actuel de souris
        dx, dy = new_x - self.down_x, new_y - self.down_y
        # Déplacer l'objet selectionné du décalage calculé
        if self.selObject:
            self.move(self.selObject, dx, dy)
            self.down_x, self.down_y = new_x, new_y

        print(new_x, new_y)

print(__name__)

if __name__ == '__main__':
    # Variables globales
    valeurs = {}
    forme = ""
    couleur = ""
    print(id(forme))
    def draw_object():
        if not canvas.getMode():
            global couleur
            x = int(valeurs["x"].get())
            y = int(valeurs["y"].get())
            w = int(valeurs["w"].get())
            h = int(valeurs["h"].get())
            forme = formes.get()
            print("draw", id(forme), couleur)
            if forme == "rectangle":
                canvas.create_rectangle(x, y, x + w, y + h, fill=couleur)
            else:
                canvas.create_oval(x, y, x + w, y + h, fill=couleur)
        else:
            print("Dessin non autorisé en mode suppression!")

    def sel_forme(event):
        global forme
        forme = formes.get()
        print("sel", id(forme))
        print(forme)

    def sel_couleur(event):
        global couleur
        couleur = couleurs.get()
        print(couleur)

    def sel_mode():
        print(check_del.var.get())
        canvas.setMode(bool(check_del.var.get()))
        if check_del.var.get() == 1:
            canvas.configure(bg="red")
        else:
            canvas.configure(bg="black")

    fen = tk.Tk()
    canvas = MyCanvas(fen, 800, 600)
    canvas.grid(row=0, columnspan=9)

    formes = ttk.Combobox(fen, values=["rectangle", "ellipse"])
    formes.bind("<<ComboboxSelected>>", sel_forme)
    formes.set("rectangle")
    sel_forme(None)
    formes.grid(row=1)

    couleurs = ttk.Combobox(fen, values=["white", "blue", "red", "orange", "grey", "yellow"])
    couleurs.bind("<<ComboboxSelected>>", sel_couleur)
    couleurs.set("white")
    sel_couleur(None)
    couleurs.grid(row=2)

    # width: nombre caractères affichés
    # x_dep = ttk.Entry(fen, width=3)
    # y_dep = ttk.Entry(fen, width=3)
    # width = ttk.Entry(fen, width=3)
    # height = ttk.Entry(fen, width=3)
    x_dep = ttk.Spinbox(fen, from_=0, to=600, width=4)
    y_dep = ttk.Spinbox(fen, from_=0, to=600, width=4)
    width = ttk.Spinbox(fen, from_=0, to=400, width=4)
    height = ttk.Spinbox(fen, from_=0, to=400, width=4)
    # x_dep.configure(width=4)
    x_dep.insert(0, "100")
    y_dep.insert(0, "100")
    width.insert(0, "300")
    height.insert(0, "300")

    x_label = ttk.Label(fen, text="X")
    y_label = ttk.Label(fen, text="Y")
    w_label = ttk.Label(fen, text="L")
    h_label = ttk.Label(fen, text="H")

    valeurs["x"] = x_dep
    valeurs["y"] = y_dep
    valeurs["w"] = width
    valeurs["h"] = height

    x_label.grid(row=1, column=1, sticky="w")
    x_dep.grid(row=1, column=2, sticky="w")
    y_label.grid(row=1, column=3, sticky="w")
    y_dep.grid(row=1, column=4, sticky="w")
    w_label.grid(row=1, column=5, sticky="w")
    width.grid(row=1, column=6, sticky="w")
    h_label.grid(row=1, column=7, sticky="w")
    height.grid(row=1, column=8, sticky="w")

    draw = ttk.Button(fen, text="Dessiner", command=draw_object)
    draw.grid(row=2, column=3, columnspan= 2, sticky="we")

    del_label = ttk.Label(fen, text="Suppression")
    # variable qui porte la valeur True ou False
    v = tk.IntVar()
    check_del = ttk.Checkbutton(fen, command=sel_mode, variable=v)
    check_del.var = v

    del_label.grid(row=2, column=8)
    check_del.grid(row=2, column=7)

    # canvas.create_line(0,0, 500, 500, fill="white")
    # canvas.create_rectangle(100, 100, 500, 400, fill="orange")
    # canvas.create_oval(100, 100, 500, 400, fill="green")
    # canvas.create_text(200, 200, text="Ceci est un texte", fill="purple")
    # canvas.create_polygon(120, 20, 150, 50, 50, 100, fill="blue")

    # couleurs = ("white", "orange", "green", "purple", "blue", "grey", "cyan")
    # random.randrange(400)

    # Dessiner 10 rectangles de dimensions et couleur aléatoires
    # for nb in range(0, 10):
    #     couleur = couleurs[random.randrange(7)]
    #     x_dep, y_dep = random.randrange(300), random.randrange(200)
    #     x_fin = x_dep + random.randrange(200)
    #     y_fin = y_dep + random.randrange(300)
    #     canvas.create_rectangle(x_dep, y_dep, x_fin, y_fin, fill=couleur)
    fen.mainloop()
