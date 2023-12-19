
import tkinter as tk
# import time
# import threading

import ttkbootstrap as ttkb

from ..helpers import iniciar_sesion, get_all_sinesters


class HomeScreen(ttkb.Frame):
    def __init__(self, master: ttkb.Window, *args, **kwargs) -> None:
        super().__init__(master, *args, **kwargs)
        self.master = master

        self.pack(fill=tk.BOTH, expand=True)

        self.create_widgets()

    def create_widgets(self) -> None:
        self.label = ttkb.Label(
            self,
            text="Sincronización de siniestros",
            font=("Helvetica", 24)
        )

        # self.follow_bot = tk.BooleanVar()

        # self.follow_bot_checker = ttkb.Checkbutton(
        #     self,
        #     text="Visualizar procedimiento",
        #     onvalue=True,
        #     offvalue=False,
        #     variable=self.follow_bot
        # )

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

        self.label.pack(pady=10)
        # self.follow_bot_checker.pack(pady=10)
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

    def start_bot(self) -> None:
        if self.sinester_input.get() == '':
            self.error_label.config(text="Sinester is required")
        else:
            self.error_label.config(text="")

            self.master.destroy()
            # self.master.quit()

            iniciar_sesion()
