import tkinter as tk
from tkinter import ttk
from tkinter import colorchooser as co

class MyFrame(tk.Toplevel):
    def __init__(self, boss):
        tk.Toplevel.__init__(self, master=boss)
        self.create_spinboxes()
        self.create_labels()
        self.create_layout()
    def __del__(self):
        print("Bye from Frame")

    def create_spinboxes(self):
        self.x_dep = ttk.Spinbox(self, from_=0, to=600, width=4)
        self.y_dep = ttk.Spinbox(self, from_=0, to=600, width=4)
        self.width = ttk.Spinbox(self, from_=0, to=400, width=4)
        self.height = ttk.Spinbox(self, from_=0, to=400, width=4)
        self.x_dep.insert(0, "100")
        self.y_dep.insert(0, "100")
        self.width.insert(0, "300")
        self.height.insert(0, "300")

    def create_labels(self):
        self.x_label = ttk.Label(self, text="X")
        self.y_label = ttk.Label(self, text="Y")
        self.w_label = ttk.Label(self, text="L")
        self.h_label = ttk.Label(self, text="H")

    def create_layout(self):
        self.x_label.grid(row=1, column=1, sticky="w")
        self.x_dep.grid(row=1, column=2, sticky="w")
        self.y_label.grid(row=1, column=3, sticky="w")
        self.y_dep.grid(row=1, column=4, sticky="w")
        self.w_label.grid(row=1, column=5, sticky="w")
        self.width.grid(row=1, column=6, sticky="w")
        self.h_label.grid(row=1, column=7, sticky="w")
        self.height.grid(row=1, column=8, sticky="w")

    def get_dimensions(self):
        return {"x":self.x_dep.get(), "y":self.y_dep.get(), "w": self.width.get(), "h":self.height.get()}

class MyStyleFrame(tk.Toplevel):
    def __init__(self, boss):
        tk.Toplevel.__init__(self, master=boss)
        self.formes = ttk.Combobox(self, values=["rectangle", "ellipse"])
        self.formes.bind("<<ComboboxSelected>>", self.select_forme)
        self.formes.set("rectangle")
        self.forme = "rectangle"
        self.formes.grid(row=0)

        self.bouton_couleur = ttk.Button(self, text="Couleur", command=self.set_color)
        self.bouton_couleur.grid(row=0, column=1)
        self.couleur = ((255, 255, 255), "white")

        self.color_frame = tk.Frame(self)
        self.color_frame.configure(width="60", height="20")
        self.color_frame.grid(row=0, column=2)
    def __del__(self):
        print("Bye from StyleFrame")
    def select_forme(self, event):
        self.forme = self.formes.get()

    def set_color(self):
        self.couleur = co.askcolor()
        self.color_frame.configure(background=self.couleur[1])

    def get_forme(self):
        return self.forme

    def get_color(self):
        return self.couleur[1]

if __name__ == "__main__":
    # Fenêtre principale d'application
    root = tk.Tk()
    root.title("Dimensions de l'objet")
    # my_frame = MyFrame(root)
    # my_frame.pack()
    my_style_frame = MyStyleFrame(root)
    my_style_frame.pack()
    root.mainloop()