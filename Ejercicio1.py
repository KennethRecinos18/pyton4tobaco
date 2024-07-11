import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def mostrarmensaje():
    messagebox.showinfo("Negro Josue gay")

root = tk.Tk()
root.title("Negros Huecos")
root.geometry("600x500")

boton = tk.Button(root, text= "Apachame aqui vv", command= mostrarmensaje)
boton.pack(pady=5)

label = tk.Label(text = "hola mundo")
label.pack(pady=10)
root.mainloop()
