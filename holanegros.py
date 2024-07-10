import tkinter as tk
from tkinter import messagebox


def xd():
    messagebox.showinfo("Cajita","Mensajito")

    root = tk.tk()
    root.title("interfas simple")
    root.geometry("300x200")

    boton = tk.button(root, text="Haz click aaqui", comand=Mensajito)
     boton.pack(pady=20)

     root.mainloop()