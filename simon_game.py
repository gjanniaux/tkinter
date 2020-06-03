import tkinter as tk
from tkinter import ttk
import random, time

class Simon(tk.Canvas):
    def __init__(self, root):
        tk.Canvas.__init__(self, root,width=400, height = 400)
        self.create_rectangle(0,0,200,200, fill="green", tags="green")
        self.create_rectangle(200, 0, 400, 200, fill="red", tags="red")
        self.create_rectangle(0, 200, 200, 400, fill="yellow", tags="yellow")
        self.create_rectangle(200, 200, 400, 400, fill="blue", tags="blue")
        self.color_list = ["green", "red", "yellow", "blue"]
        # On fait correspondre le click gauche à la méthode click
        self.bind("<Button-1>", self.__click)
        self.info = tk.Toplevel(root)
        self.info.title("Info")
        info_frame = tk.LabelFrame(self.info, text="Niveau ", width=100, height= 100)
        info_frame.pack()
        self.level = tk.Label(info_frame, text="0")
        self.level.pack()

    def __click(self, event):
        clicked_item = self.find_closest(event.x, event.y, 1)
        tags = self.gettags(clicked_item)
        color_clicked = tags[0]
        # Index = 0 au premier click de l'utilisateur
        index = len(self.clicks)
        print(color_clicked, self.colors[index])
        if color_clicked == self.colors[index]:
            self.clicks.append(color_clicked)
            print(len(self.clicks))
            print("SUCCESS!")
        else:
            print("GAME OVER")
            self.colors.clear()
            self.clicks.clear()
        if len(self.clicks) == len(self.colors):
            print("Level up")
            self.__add_color()

    def start(self):
        print("Started !")
        self.colors = []
        self.clicks = []
        # Ajouter une première couleur
        self.__add_color()

    def __add_color(self):
        # Nombre au hasard entre 0 et 3
        color_index =  random.randrange(4)
        # On récupère la couleur à l'index défini par le tirage au sort
        color = self.color_list[color_index]
        # On mémorise la couelur dans la liste
        self.colors.append(color)
        self.level.configure(text = str(len(self.colors)))
        # On flashe la séquence de couleurs à reproduire
        print(self.colors)
        for color in self.colors:
            self.__flash_color(color)
        self.clicks.clear()


    def __flash_color(self, color):
        #Carré à flasher
        item = self.find_withtag(color)
        # On le passe en blanc
        time.sleep(0.5)
        self.itemconfig(item, fill="white")
        self.update()
        time.sleep(0.5)
        self.itemconfig(item, fill= color)
        self.update()




if __name__ == "__main__":
    root = tk.Tk()
    simon = Simon(root)
    simon.pack()
    start = ttk.Button(root, text="Start", command=simon.start)
    start.pack()
    root.mainloop()