import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def vvs():
    messagebox.showinfo("Mi first blowjob")


root = tk.Tk()
root.title("Oh, is so delicious")
root.geometry("600x500")

boton = tk.Button(root, text= "Botoncito", command= vvs)
boton.pack(pady=10)

boton = tk.Button(root, text= "No se que poner", command= vvs)
boton.pack(pady=10)

boton = tk.Button(root, text= "Paseme la materia", command= vvs)
boton.pack(pady=10)

progressbar = ttk.Progressbar(root, orient= "horizontal", length= 200, mode= "determinate")
progressbar.pack(pady = 10)

root.mainloop()
