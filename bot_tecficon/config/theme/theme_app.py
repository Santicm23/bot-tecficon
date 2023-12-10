
import tkinter as tk
import ttkbootstrap as ttkb


def set_theme(root: tk.Tk) -> None:
    root.config()

    ttkb.Style().theme_use('darkly')

    root.title("Sincronización de siniestros")
    root.geometry("500x500")
