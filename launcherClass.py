import tkinter as tk
import os
import subprocess
import sys
from tkinter import *
import customtkinter


class Launcher(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.creer_widgets()
        
    def creer_widgets(self):
        self.bouton = tk.Button(self, text="snake", command=self.open_file)
        self.bouton.pack()

# Compatibilité avec l'os utilisé. (Windows, Ubuntu)

    def open_file(event):
        if sys.platform == "win32":
            os.startfile("snake\Snake.py")
        else:
            "python" if sys.platform == "darwin" else "xdg-open"
            subprocess.run([sys.executable, "snake/Snake.py"])


if __name__ == "__main__":
    app = Launcher()
    app.title("ASE Launcher")
    app.geometry("1280x720")
    app.mainloop()
    
