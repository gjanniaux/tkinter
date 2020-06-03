import tkinter as tk
from tkinter import ttk
import random, time

class Morpion(tk.Canvas):

    def __init__(self, root):
        tk.Canvas.__init__(self, root,width=600, height = 600)
        self.bind("<Button-1>", self.__click)
        self.create_line(200, 0, 200, 600)
        self.create_line(400, 0, 400, 600)
        self.create_line(0, 200, 600, 200)
        self.create_line(0, 400, 600, 400)

        for row in range(3):
            for col in range(3):
                x = 0 + col * 200
                y = 0 + row * 200
                self.create_rectangle(x, y, x + 200, y+ 200, fill="yellow", tags=[str(row), str(col)])

    def __click(self, event):
        x, y = event.x, event.y
        print(x, y)
        case = self.find_closest(x, y)
        tags = self.gettags(case)
        print(tags)
        row, col = int(tags[0]), int(tags[1])
        x = 0 + col * 200
        y = 0 + row * 200
        self.create_oval(x, y, x + 200, y + 200, width=2)

    def start(self):
        print("Started !")

    def __add_shape(self):
        pass

if __name__ == "__main__":
    root = tk.Tk()
    morpion = Morpion(root)
    morpion.pack()
    root.mainloop()