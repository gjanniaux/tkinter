import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

class MyWriter(tk.Frame):
    def __init__(self, boss):
        tk.Frame.__init__(self, boss)

        self.scrollbar = tk.Scrollbar(self)
        self.text = tk.Text(self, yscrollcommand=self.scrollbar.set, width=80, height=10)
        self.scrollbar.config(command=self.text.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill="y")
        self.text.pack(side=tk.LEFT)

    def getText(self):
        return self.text.get(1.0, tk.END)

    def setText(self, lines):
        print(lines)
        for line in lines:
            self.text.insert(tk.INSERT, line)

if __name__ == "__main__":

    def save():
        fname = file_name.get()
        bool_save = True
        if os.path.exists(fname):
            bool_save = messagebox.askyesno("Sauvegarde", "Le fichier existe déjà, souhaitez-vous l'écraser ?")
        if bool_save:
            with open(fname, "w") as file:
                lines = my_writer.getText()
                print(lines)
                file.writelines(lines)

    def open_file():
        file_list.get()
        with open(file_list.get(), "r") as file:
            lines = file.readlines()
            my_writer.setText(lines)
    def select_file():
        pass

    print(os.listdir())

    root = tk.Tk()
    root.title("Mon premier éditeur de texte")
    my_writer = MyWriter(root)
    my_writer.grid(row=0, columnspan=4)
    file_name = ttk.Entry(root)
    file_name.grid(row=1, column=0)
    but_save = ttk.Button(root, text="Enregistrer", command=save)
    but_save.grid(row=1, column=1)

    file_list = ttk.Combobox(root, values=os.listdir())
    file_list.grid(row=1, column=2)

    but_open = ttk.Button(root, text="Ouvrir", command=open_file)
    but_open.grid(row=1, column=3)
    root.mainloop()