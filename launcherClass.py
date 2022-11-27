import tkinter as tk
import os
from tkinter import *
class Launcher(tk.Tk):

    def open_file(event):
        os.startfile("snake\Snake.py")
    def __init__(self):
        tk.Tk.__init__(self)
        self.creer_widgets()

    def creer_widgets(self):
        self.bouton = tk.Button(self, text="snake", command=self.open_file)
        self.bouton.pack()


if __name__ == "__main__":
    app = Launcher()
    app.title("ASE Launcher")
    app.geometry("1280x720")
    app.mainloop()
