import tkinter as tk
from typing import Any, Callable

import ttkbootstrap as ttkb
from requests.exceptions import ConnectTimeout

from ...domain.errors import Error
from ...domain.use_cases import (
    actualizar_victimas,
    crear_siniestro,
    sincronizar_eventos,
)


class HomeScreen(ttkb.Frame):
    def __init__(self, master: ttkb.Window, *args: Any, **kwargs: Any) -> None:
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.pack(fill=tk.BOTH, expand=True)

        self.create_widgets()

    def create_widgets(self) -> None:
        self.logo = tk.PhotoImage(file="./assets/images/HGD.png")

        self.label = ttkb.Label(
            self, text="Sincronización de siniestros", font=("Helvetica", 24)
        )

        self.numero_siniestro_label = ttkb.Label(
            self, text="Número de siniestro:", font=("Helvetica", 10)
        )

        self.sinester_input = ttkb.Entry(
            self,
            validate="all",
            validatecommand=(self.register(self.validate_sinester_input), "%P"),
        )

        self.error_label = ttkb.Label(
            self, text="", foreground="red", font=("Helvetica", 12)
        )

        self.crear_siniestro_button = ttkb.Button(
            self,
            text="Crear siniestro",
            command=lambda: self.start_bot(self.crear_siniestro),
        )

        self.crear_victimas_button = ttkb.Button(
            self,
            text="Crear víctimas FU",
            command=lambda: self.start_bot(self.actualizar_victimas),
        )

        self.sincronizar_eventos_button = ttkb.Button(
            self,
            text="Sincronizar eventos",
            command=lambda: self.start_bot(self.sincronizar_eventos),
        )

        self.logo_label = ttkb.Label(self, image=self.logo).pack()
        self.label.pack(pady=10)
        self.numero_siniestro_label.pack(pady=10)
        self.sinester_input.pack()
        self.error_label.pack(pady=5)
        self.crear_siniestro_button.pack(pady=10)
        self.crear_victimas_button.pack(pady=10)
        self.sincronizar_eventos_button.pack(pady=10)

    def validate_sinester_input(self, value: str) -> bool:
        if value == "":
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
            new_window, text=error.message, font=("Helvetica", 16), wraplength=350
        )

        close_button = ttkb.Button(
            new_window,
            text="Aceptar",
            command=new_window.destroy,
            style="danger.TButton",
        )

        error_label.pack(pady=50)
        close_button.pack()

    def create_succes_modal(self, msg: str) -> None:
        new_window = tk.Toplevel(self.master)

        new_window.title("Éxito")
        new_window.geometry("400x300")
        new_window.resizable(False, False)

        error_label = ttkb.Label(
            new_window, text=msg, font=("Helvetica", 16), wraplength=350
        )

        close_button = ttkb.Button(
            new_window,
            text="Aceptar",
            command=new_window.destroy,
            style="success.TButton",
        )

        error_label.pack(pady=50)
        close_button.pack()

    def start_bot(self, function: Callable[[int], None]) -> None:
        sinester_id = self.sinester_input.get()
        if sinester_id == "":
            self.error_label.config(text="El número de siniestro es requerido")
        else:
            self.error_label.config(text="")

            try:
                function(int(sinester_id))
            except Error as err:
                self.create_error_modal(err)
            except ConnectTimeout as err:
                self.create_error_modal(Error("No se pudo conectar con el servidor"))
            except Exception as err:
                print(err)
                self.create_error_modal(Error("Error inesperado, intente nuevamente"))

    def crear_siniestro(self, sinester_id: int) -> None:
        crear_siniestro(sinester_id)

        self.create_succes_modal("Siniestro creado con éxito")

    def actualizar_victimas(self, sinester_id: int) -> None:
        actualizar_victimas(sinester_id)

    def sincronizar_eventos(self, sinester_id: int) -> None:
        sincronizar_eventos(sinester_id)
