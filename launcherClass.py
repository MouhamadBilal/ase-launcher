import tkinter as tk
import os

class Launcher(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.creer_widgets()

    def open_text(event):
            os.startfile("ase-launcher\snake\Snake.py")

    def creer_widgets(self):
        self.bouton = tk.Button(self, text="snake", command=self.open_text)
        self.bouton.pack()
        

if __name__ == "__main__":
    app = Launcher()
    app.title("ASE Launcher")
    app.geometry("1280x720")
    app.mainloop()