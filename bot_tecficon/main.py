
import tkinter as tk

import ttkbootstrap as ttkb

from bot_tecficon.config import set_theme
from bot_tecficon.presentation.screens import HomeScreen


def main() -> None:

    root = ttkb.Window()
    set_theme(root)

    HomeScreen(root).place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    root.mainloop()


if __name__ == '__main__':
    main()
