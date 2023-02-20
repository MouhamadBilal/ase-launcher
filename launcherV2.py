import tkinter as tk
import os
import subprocess
import sys
from tkinter import *
import customtkinter
from PIL import Image
import customtkinter as ctk
from PIL import Image, ImageTk


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("1280x720")
app.title("ASE Launcher")

def open_file():
        if sys.platform == "win32":
            os.startfile("snake\Snake.py")
        else:
            "python" if sys.platform == "darwin" else "xdg-open"
            subprocess.run([sys.executable, "snake/Snake.py"])

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text= "snake", command=open_file)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()