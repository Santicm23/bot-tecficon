
from typing import Any
import tkinter as tk

import ttkbootstrap as ttkb
from requests.exceptions import ConnectTimeout

from ...domain.use_cases import crear_siniestro
from ...domain.errors import Error


class HomeScreen(ttkb.Frame):
    def __init__(self, master: ttkb.Window, *args: Any, **kwargs: Any) -> None:
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.pack(fill=tk.BOTH, expand=True)

        self.create_widgets()

    def create_widgets(self) -> None:
        self.logo = tk.PhotoImage(
            file="./bot_tecficon/presentation/assets/images/HGD.png")

        self.label = ttkb.Label(
            self,
            text="Sincronización de siniestros",
            font=("Helvetica", 24)
        )

        self.sinester_input = ttkb.Entry(
            self,
            validate='all',
            validatecommand=(self.register(self.validate_sinester_input), '%P')
        )

        self.button = ttkb.Button(
            self,
            text="Start Bot",
            command=self.start_bot
        )

        self.error_label = ttkb.Label(
            self,
            text="",
            foreground="red",
            font=("Helvetica", 8)
        )

        self.logo_label = ttkb.Label(
            self,
            image=self.logo
        ).pack()
        self.label.pack(pady=10)
        self.sinester_input.pack()
        self.error_label.pack()
        self.button.pack(pady=10)

    def validate_sinester_input(self, value: str) -> bool:
        if value == '':
            return True

        try:
            int(value)
            return True
        except ValueError:
            return False
    
    def create_error_modal(self, error: Error) -> None:
        new_window = tk.Toplevel(self.master)

        new_window.title("Error")
        new_window.geometry("400x300")
        new_window.resizable(False, False)

        error_label = ttkb.Label(
            new_window,
            text=error.message,
            font=("Helvetica", 16),
            wraplength=350
        )

        close_button = ttkb.Button(
            new_window,
            text="Aceptar",
            command=self.master.destroy,
            style="danger.TButton",
        )

        error_label.pack(pady=50)
        close_button.pack()

    def start_bot(self) -> None:
        sinester_id = self.sinester_input.get()
        if sinester_id == '':
            self.error_label.config(text="Sinester is required")
        else:
            self.error_label.config(text="")

            try:
                crear_siniestro(int(sinester_id))
            except Error as err:
                self.create_error_modal(err)
            except ConnectTimeout as err:
                self.create_error_modal(Error("No se pudo conectar con el servidor"))
            except Exception as err:
                self.create_error_modal(Error("Error inesperado, intente nuevamente"))
